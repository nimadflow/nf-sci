import argparse,hashlib,json,os,re
SCHEMA="DRNIMAD_ACTUATION_REQUEST_V1"; PART_STATE="ADMISSION_ONLY__NO_ACTUATION"
HEX64=re.compile(r"^[0-9a-f]{64}$"); RID=re.compile(r"^[A-Z0-9_:-]{3,96}$")
MONEY={"CAPITAL","ORDER","PAYMENT","POSITION"}; EFFECTS={"READ","APPEND_STATE","MUTATE_STATE","LIVE_BIND"}; AUTH={"BLUE_NONMONETARY"}; VERB_EFFECTS={"NOOP_RECEIPT":{"APPEND_STATE"},"B3_PROBE_APPEND_V1":{"APPEND_STATE"}}; VERB_SHA_BINDINGS={"B3_PROBE_APPEND_V1":"2ae328b5781cc7f135aef998913e6ec3e13ab32c65f7dba3ae262a9ee8706f89"}
REQ={"schema","request_id","requester_uid","mission_ir_sha","body_selected_receipt_sha","route_proof_sha","verb_id","qualified_verb_sha","operand","expected_prestate_sha","effect_class","authority_class","exact_env_manifest_sha","timeout_ms","rollback_contract_sha"}
OPREQ={"kind","locator","identity_sha256","parent_identity_sha256"}; FORBID={"raw_shell_text","shell","argv","arbitrary_argv","executable_path","arbitrary_executable_path","env","arbitrary_env","sudo","red_authority_receipt","private_key","order_credential","capital_handle"}
def canon(o): return (json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False)+"\n").encode()
def shaok(v): return isinstance(v,str) and HEX64.fullmatch(v) is not None
def validate(q,uid):
 e=[]
 if not isinstance(q,dict): return ["REQUEST_NOT_OBJECT"]
 k=set(q); f=sorted(k&FORBID); m=sorted(REQ-k); x=sorted(k-REQ)
 if f:e.append("FORBIDDEN_KEYS:"+",".join(f))
 if m:e.append("MISSING_KEYS:"+",".join(m))
 if x:e.append("EXTRA_KEYS:"+",".join(x))
 if e:return e
 if q["schema"]!=SCHEMA:e.append("SCHEMA")
 if not isinstance(q["request_id"],str) or RID.fullmatch(q["request_id"]) is None:e.append("REQUEST_ID")
 if q["requester_uid"]!=uid:e.append("REQUESTER_UID")
 for z in ("mission_ir_sha","body_selected_receipt_sha","route_proof_sha","qualified_verb_sha","expected_prestate_sha","exact_env_manifest_sha","rollback_contract_sha"):
  if not shaok(q[z]):e.append("SHA:"+z)
 if q["verb_id"] not in VERB_EFFECTS:e.append("VERB_ID")
 if q["effect_class"] in MONEY:e.append("MONETARY_EFFECT_FORBIDDEN")
 elif q["effect_class"] not in EFFECTS:e.append("EFFECT_CLASS")
 if q["verb_id"] in VERB_EFFECTS and q["effect_class"] not in VERB_EFFECTS[q["verb_id"]]:e.append("VERB_EFFECT_MISMATCH")
 if q["verb_id"] in VERB_SHA_BINDINGS and q["qualified_verb_sha"]!=VERB_SHA_BINDINGS[q["verb_id"]]:e.append("QUALIFIED_VERB_SHA")
 if q["authority_class"] not in AUTH:e.append("AUTHORITY_CLASS")
 t=q["timeout_ms"]
 if not isinstance(t,int) or isinstance(t,bool) or not 1<=t<=5000:e.append("TIMEOUT_MS")
 o=q["operand"]
 if not isinstance(o,dict) or set(o)!=OPREQ:e.append("OPERAND_SCHEMA")
 else:
  if o["kind"]!="OBJECT_IDENTITY_V1":e.append("OPERAND_KIND")
  p=o["locator"]
  if not isinstance(p,str) or not p.startswith("/") or ".." in p.split("/"):e.append("OPERAND_LOCATOR")
  if not shaok(o["identity_sha256"]):e.append("OPERAND_IDENTITY_SHA")
  if not shaok(o["parent_identity_sha256"]):e.append("OPERAND_PARENT_SHA")
 return e
def main():
 p=argparse.ArgumentParser(); p.add_argument("--request-json",required=True); p.add_argument("--allowed-requester-uid",required=True,type=int); p.add_argument("--output",required=True); a=p.parse_args()
 try:q=json.loads(a.request_json); e=validate(q,a.allowed_requester_uid)
 except Exception as z:q=None;e=["REQUEST_JSON:"+type(z).__name__]
 out={"schema":"DRNIMAD_ACTUATION_ADMISSION_RESULT_V1","state":"ADMITTED" if not e else "REJECTED","part_state":PART_STATE,"request_sha256":hashlib.sha256(canon(q)).hexdigest() if isinstance(q,dict) else None,"errors":e,"actuation_performed":False,"monetary_authority_present":False}
 b=canon(out); fd=os.open(a.output,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o400)
 with os.fdopen(fd,"wb") as f:f.write(b);f.flush();os.fsync(f.fileno())
 return 0
if __name__=="__main__": raise SystemExit(main())
