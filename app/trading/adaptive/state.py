STATES=("ARMED" "ACTIVE" "PROFIT" "PROTECTED" "EXTENDING" "EXHAUSTION" "EXIT")
def state(profit,risk,weak=False):
 if profit<=-risk:return "EXIT"
 if profit<=0:return "ARMED"
 if weak:return "EXHAUSTION"
 if profit>=risk*2:return "EXTENDING"
 if profit>=risk:return "PROTECTED"
 return "ACTIVE"
