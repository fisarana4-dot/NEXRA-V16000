def normalize(q,i):
 q=max(i.volume_min,min(q,i.volume_max))
 return round(q/i.volume_step)*i.volume_step
