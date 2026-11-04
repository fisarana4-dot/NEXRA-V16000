from app.saas.auth.service import AuthService
def test_user(): a = AuthService(); u = a.create_user("1","a@b.com","t1"); assert u.email == "a@b.com"
