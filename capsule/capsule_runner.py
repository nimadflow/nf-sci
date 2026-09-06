import hashlib, json, os, stat, subprocess, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
SCOPE = "ADMISSION_CORE_EXTERNAL_REPRODUCTION_V1"
RESULT_KEYS = {"schema", "state", "part_state", "request_sha256", "errors", "actuation_performed", "monetary_authority_present"}
CASES = [
    ("PC", "fixtures/PC.json", "ADMITTED", []),
    ("NC1", "fixtures/NC1_FORBIDDEN_SHELL.json", "REJECTED", ["FORBIDDEN_KEYS:shell", "EXTRA_KEYS:shell"]),
    ("NC2", "fixtures/NC2_REQUESTER_UID.json", "REJECTED", ["REQUESTER_UID"]),
    ("NC3", "fixtures/NC3_MONETARY_ORDER.json", "REJECTED", ["MONETARY_EFFECT_FORBIDDEN", "VERB_EFFECT_MISMATCH"]),
    ("NC4", "fixtures/NC4_QUALIFIED_VERB_SHA.json", "REJECTED", ["QUALIFIED_VERB_SHA"]),
    ("NC5", "fixtures/NC5_MISSING_ROLLBACK.json", "REJECTED", ["MISSING_KEYS:rollback_contract_sha"]),
]
class Stop(Exception): pass
def need(value, code):
    if not value: raise Stop(code)
def canon(value): return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
def sha(raw): return hashlib.sha256(raw).hexdigest()
def read_rel(name):
    need(isinstance(name, str) and name and not name.startswith("/") and "\\" not in name, "BAD_RELATIVE_PATH")
    need(all(part not in ("", ".", "..") for part in name.split("/")), "BAD_RELATIVE_PATH")
    path = os.path.join(ROOT, *name.split("/"))
    st = os.lstat(path)
    need(stat.S_ISREG(st.st_mode) and not stat.S_ISLNK(st.st_mode), "NONREGULAR_OR_LINK:" + name)
    with open(path, "rb") as handle: return handle.read(), st
def load_canon(name):
    raw, _ = read_rel(name)
    try:
        value = json.loads(raw)
    except Exception:
        raise Stop("JSON_INVALID:" + name)
    need(raw == canon(value), "JSON_NONCANONICAL:" + name)
    return value, raw
def verify_manifest():
    manifest, raw = load_canon("MANIFEST.json")
    need(set(manifest) == {"schema", "scope", "files"}, "MANIFEST_SCHEMA")
    need(manifest["schema"] == "CAPSULE_V1_MANIFEST" and manifest["scope"] == SCOPE, "MANIFEST_CONSTANT")
    need(isinstance(manifest["files"], list), "MANIFEST_FILES")
    declared = {}
    for item in manifest["files"]:
        need(isinstance(item, dict) and set(item) == {"path", "sha256", "bytes"}, "MANIFEST_RECORD")
        name = item["path"]
        need(name not in declared and name not in ("MANIFEST.json", "MUST_MATCH.json"), "MANIFEST_PATH")
        data, st = read_rel(name)
        need(st.st_size == item["bytes"] and len(data) == item["bytes"] and sha(data) == item["sha256"], "MANIFEST_MISMATCH:" + name)
        declared[name] = item
    need({"admission_core.py", "capsule_runner.py"} <= set(declared), "MANIFEST_REQUIRED_FILE")
    for base, dirs, files in os.walk(ROOT, followlinks=False):
        for entry in dirs + files:
            path = os.path.join(base, entry)
            st = os.lstat(path)
            need(not stat.S_ISLNK(st.st_mode), "CAPSULE_SYMLINK")
            rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
            if stat.S_ISREG(st.st_mode) and (rel.endswith(".py") or st.st_mode & 0o111):
                need(rel in declared, "UNDECLARED_EXECUTABLE_OR_SOURCE:" + rel)
    return declared, raw
def write_exclusive(name, raw):
    path = os.path.join(ROOT, name)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags, 0o400)
    with os.fdopen(fd, "wb") as handle: handle.write(raw); handle.flush(); os.fsync(handle.fileno())
def run_cases():
    need(not os.path.lexists(os.path.join(ROOT, "case_outputs")), "RESULT_PATH_EXISTS")
    os.mkdir(os.path.join(ROOT, "case_outputs"), 0o700)
    rows = {}
    for case, fixture, state, errors in CASES:
        request, request_raw = load_canon(fixture)
        text = request_raw[:-1].decode()
        output = "case_outputs/" + case + ".json"
        argv = [sys.executable, "-I", "-S", "admission_core.py", "--request-json", text, "--allowed-requester-uid", "995", "--output", output]
        proc = subprocess.run(argv, cwd=ROOT, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10, shell=False, env={"LANG": "C", "LC_ALL": "C"})
        exists = os.path.lexists(os.path.join(ROOT, output))
        need(exists, "CORE_OUTPUT_MISSING:" + case)
        decision_raw, _ = read_rel(output)
        try:
            decision = json.loads(decision_raw)
        except Exception:
            raise Stop("CORE_OUTPUT_JSON:" + case)
        valid = proc.returncode == 0 and proc.stdout == b"" and proc.stderr == b"" and decision_raw == canon(decision)
        valid = valid and set(decision) == RESULT_KEYS and decision.get("schema") == "DRNIMAD_ACTUATION_ADMISSION_RESULT_V1"
        valid = valid and decision.get("state") == state and decision.get("errors") == errors
        valid = valid and decision.get("part_state") == "ADMISSION_ONLY__NO_ACTUATION"
        valid = valid and decision.get("actuation_performed") is False and decision.get("monetary_authority_present") is False
        valid = valid and decision.get("request_sha256") == sha(request_raw)
        need(valid, "CASE_CONTRACT:" + case)
        rows[case] = {"expected_state": state, "expected_ordered_errors": errors, "request_sha256": decision["request_sha256"], "decision_sha256": sha(decision_raw), "rc": proc.returncode, "stdout": "", "stderr": "", "output_exists": True}
    return rows
def main():
    need(len(sys.argv) == 2 and sys.argv[1] in ("record", "verify"), "CLI")
    need(not os.path.lexists(os.path.join(ROOT, "CAPSULE_RECEIPT.json")), "RECEIPT_PATH_EXISTS")
    declared, manifest_raw = verify_manifest()
    rows = run_cases()
    fixtures = {name: declared[name]["sha256"] for _, name, _, _ in CASES}
    seal_cases = {name: {key: row[key] for key in ("expected_state", "expected_ordered_errors", "request_sha256", "decision_sha256")} for name, row in rows.items()}
    seal = {"schema": "CAPSULE_V1_MUST_MATCH", "scope": SCOPE, "core_sha256": declared["admission_core.py"]["sha256"], "runner_sha256": declared["capsule_runner.py"]["sha256"], "manifest_sha256": sha(manifest_raw), "fixtures": fixtures, "cases": seal_cases, "CORE_EXTERNAL_REPRODUCTION_N": 0, "EXPECTED_DIVERGENT": ["host", "path", "time", "uid", "inode", "mtime_ns"]}
    equal = None
    if sys.argv[1] == "verify":
        expected, _ = load_canon("MUST_MATCH.json")
        equal = expected == seal
        need(equal, "MUST_MATCH_DIVERGENCE")
    receipt = {"schema": "CAPSULE_V1_RECEIPT", "scope": SCOPE, "mode": sys.argv[1], "result": True, "rc": 0, "cases": rows, "must_match_candidate": seal, "must_match_all_equal": equal}
    write_exclusive("CAPSULE_RECEIPT.json", canon(receipt))
    return True, 0
try:
    result, rc = main()
except Stop as exc:
    result, rc = False, 1
    if not os.path.lexists(os.path.join(ROOT, "CAPSULE_RECEIPT.json")):
        try:
            write_exclusive("CAPSULE_RECEIPT.json", canon({"schema": "CAPSULE_V1_RECEIPT", "scope": SCOPE, "result": False, "rc": 1, "first_false": str(exc)}))
        except Exception:
            pass
except Exception as exc:
    result, rc = False, 1
    if not os.path.lexists(os.path.join(ROOT, "CAPSULE_RECEIPT.json")):
        try:
            write_exclusive("CAPSULE_RECEIPT.json", canon({"schema": "CAPSULE_V1_RECEIPT", "scope": SCOPE, "result": False, "rc": 1, "first_false": type(exc).__name__}))
        except Exception:
            pass
sys.stdout.write("RESULT=" + str(result) + "\nRC=" + str(rc) + "\n")
raise SystemExit(rc)
