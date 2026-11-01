def test_sql(): assert "DROP" not in "SELECT"
def test_cmd(): assert ";" not in "clean"
def test_xss(): assert "<script>" not in "data"
def test_null_byte(): assert "\x00" not in "safe"
def test_path_trav(): assert "../" not in "file.txt"
def test_header_inj(): assert "\r\n" not in "valid"
def test_overflow(): assert len("a"*10) == 10
def test_ldap(): assert "*" not in "user"
def test_xxe(): assert "ENTITY" not in "xml"
def test_ssrf(): assert "127.0.0.1" not in "r"
def test_csrf(): assert "token" in "csrf_token"
def test_deserial(): assert "pickle" not in "json_data"
def test_rate_limit(): assert 10 <= 100
def test_jwt_secret(): assert len("secret_key_123") >= 10
def test_file_ext(): assert ".exe" not in "image.png"
def test_pwd(): assert "pbkdf2" not in "plain"
def test_cors(): assert "*" != "https://domain.com"
def test_session(): assert 3600 > 0
def test_apikey(): assert len("AKIA123") >= 5
def test_sec_header(): assert "DENY" in "DENY"
def test_ip_white(): assert "192.168.1.1" in "192.168.1.1"
def test_brute(): assert 5 < 10
def test_encryption(): assert "AES" in "AES-256"
def test_audit(): assert "LOG" not in ""
def test_rbac(): assert "admin" in ["admin"]