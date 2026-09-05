class BOSEngine:
    def detect(self,d):
        close=d.get("close",d.get("Close",0))
        return "BOS_UP" if close>d.get("swing_high",0) else "BOS_DOWN" if close<d.get("swing_low",0) else ""
bos_engine=BOSEngine()
