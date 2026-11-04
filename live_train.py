LIVE_CASE="XAUUSD 4641.46 M15: decide BUY/SELL/NO_TRADE; give entry,SL,TP,reasons"
print(LIVE_CASE)
print("LIVE_PRICE",4641.46);print("DECISION_RULE: STRUCTURE+VSA+M15+MTF+LEVEL")
print("REQUIRED:STRUCTURE,VSA,TREND,RSI,LEVEL,MTF,INVALIDATION")
import subprocess;print("STRUCTURE_EVIDENCE");print(subprocess.getoutput("python m1_struct_events.py|tail -3"))
print("VSA_EVIDENCE");print(__import__("subprocess").getoutput("python m1_vsa.py|tail -6"))
