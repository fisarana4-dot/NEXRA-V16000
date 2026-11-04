def detect(slope,vol,base):
 if vol>base*2:return "EXPANSION"
 if vol<base*.5:return "COMPRESSION"
 if abs(slope)>0:return "TREND"
 return "RANGE"
