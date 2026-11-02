class LeadScorer:
    def score(self, lead, mx_valid=False):
        def val(key):
            return lead.get(key) if isinstance(lead, dict) else getattr(lead, key, None)
        import re
        email = val("email") or ""
        valid = bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))
        checks = {
            "company_name": (10, bool(val("company_name"))),
            "website": (20, bool(val("website"))),
            "email": (15, valid),
            "mx": (20, valid and mx_valid),
            "country": (10, bool(val("country"))),
            "industry": (15, bool(val("industry"))),
            "phone": (10, bool(val("phone"))),
        }
        score = sum(p for p, ok in checks.values() if ok)
        breakdown = {
            k: {"points": p if ok else 0, "max": p}
            for k, (p, ok) in checks.items()
        }
        return {"score": score, "max_score": 100, "breakdown": breakdown, "mx_means_mailbox_verified": False}
