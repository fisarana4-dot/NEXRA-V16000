class CHoCHEngine:
    def detect(self,d):
        if "swing_high" not in d or "swing_low" not in d: return ""
        close=d.get("close",d.get("Close",0))
        t=str(d.get("trend","")).upper()
        if t=="DOWN": return "CHoCH_UP" if close>d["swing_high"] else ""
        if t=="UP": return "CHoCH_DOWN" if close<d["swing_low"] else ""
        return "CHoCH_UP" if close>d.get("swing_high",0) else "CHoCH_DOWN" if close<d.get("swing_low",0) else ""
choch_engine=CHoCHEngine()
