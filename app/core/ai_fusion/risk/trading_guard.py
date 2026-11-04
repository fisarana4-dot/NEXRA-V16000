def allow_sl(old,new): return new>=old
def trail(entry,profit): return entry+profit
def safe_trail(old,entry,profit): return max(old,trail(entry,profit))
def allow_manual(): return False
def gate(manual=False): return not manual
