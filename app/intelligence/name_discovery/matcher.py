def score(candidate,signals):
 return min(100,sum(signals.values()))
def classify(score):
 return 'HIGH' if score>=80 else 'MEDIUM' if score>=60 else 'LOW'
