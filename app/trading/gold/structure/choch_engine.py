class CHoCHEngine:
    def detect(self,d):
        close=d.get("close",d.get("Close",0))
        return "CHoCH_UP" if close>d.get("swing_high",0) else "CHoCH_DOWN" if close<d.get("swing_low",0) else ""
choch_engine=CHoCHEngine()
