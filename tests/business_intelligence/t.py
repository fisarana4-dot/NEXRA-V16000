import hashlib
def test_c():
 assert len(hashlib.sha256(b"A").hexdigest())==64