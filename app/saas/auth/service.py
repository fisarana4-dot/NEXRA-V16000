from app.saas.auth.models import User
class AuthService:
    def create_user(self, uid, email, tid): return User(uid, email, tid)
