import pytest, hashlib
def test_sha256_audit_ledger():
    assert len(hashlib.sha256(b"x").hexdigest())==64
@pytest.mark.parametrize("i",range(10))
def test_sha256_payloads(i):
    assert len(hashlib.sha256(str(i).encode()).hexdigest())==64
def test_sha256_known_digest():
    assert hashlib.sha256(b"abc").hexdigest()=="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
