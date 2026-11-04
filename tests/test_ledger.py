from ledger.evidence import Ledger
def test_seal():
    assert Ledger.seal({"a":1}) is not None
