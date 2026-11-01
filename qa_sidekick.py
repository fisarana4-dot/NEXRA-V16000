import re

class QASidekick:
    @staticmethod
    def audit_draft(text: str) -> dict:
        has_placeholders = bool(re.search(r'\[VERIFY:.*?\]', text))
        return {"has_placeholders": has_placeholders}
