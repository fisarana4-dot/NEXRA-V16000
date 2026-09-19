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
