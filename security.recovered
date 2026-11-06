from app.core.security.integrity import sha256
def test_sha256():
    assert sha256(b"NEXRA")=="9184f5acdbcfcc7f459954c578c0b05a63697ab8893d91f67fc2575689b46ddb"
from app.core.security.integrity import chain_hash
def test_chain_hash():
    assert chain_hash({"a":1})=="015abd7f5cc57a2dd94b7590f04ad8084273905ee33ec5cebeae62276a97f862"
from app.core.security.integrity import verify_chain
def test_verify_chain():
    r={"payload":{"a":1}}; r["hash"]=chain_hash(r["payload"]); assert verify_chain([r])
def test_tamper():
    r={"payload":{"a":1}}; r["hash"]=chain_hash(r["payload"]); r["payload"]["a"]=2; assert not verify_chain([r])
def test_verify_chain_missing_hash():
    assert not verify_chain([{"payload": {"a": 1}}])
def test_verify_chain_multiple_records():
    a = {"payload": {"id": 1}}
    a["hash"] = chain_hash(a["payload"])
    b = {"payload": {"id": 2}}
    b["hash"] = chain_hash(b["payload"], a["hash"])
   
    assert verify_chain([a, b])
def test_verify_chain_tampered_hash():
    r = {"payload": {"id": 1}}
    r["hash"] = chain_hash(r["payload"])
    r["hash"] = "0" * 64
    assert not verify_chain([r])
def test_verify_chain_empty():
    assert verify_chain([])
def test_verify_chain_missing_payload():
    assert not verify_chain([{"hash": "0" * 64}])
def test_verify_chain_invalid_payload():
    r = {"payload": {1, 2}}
    r["hash"] = "0" * 64
    assert not verify_chain([r])
def test_verify_chain_reordered_records():
    a = {"payload": {"id": 1}}
    a["hash"] = chain_hash(a["payload"])
    b = {"payload": {"id": 2}}
    b["hash"] = chain_hash(b["payload"], a["hash"])
  
    assert not verify_chain([b, a]) 
def test_verify_chain_previous_hash_tampered():
    a = {"payload": {"id": 1}}
    a["hash"] = chain_hash(a["payload"])
    b = {"payload": {"id": 2}}
    b["hash"] = chain_hash(b["payload"], a["hash"])
    a["hash"] = "0" * 64
    assert not verify_chain([a, b])
