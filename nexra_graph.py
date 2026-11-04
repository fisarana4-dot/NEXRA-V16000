import pandas as p
from PIL import Image,ImageDraw
d=p.read_csv('data/gold/full/xauusd-d1-bid-2026-01-01-2026-08-08.csv')
v=d.close.tolist();w,h=1200,700
im=Image.new('RGB',(w,h),'white');dr=ImageDraw.Draw(im)
lo,hi=min(v),max(v);pts=[]
for i,x in enumerate(v):pts.append((50+i*1100/(len(v)-1),650-(x-lo)*600/(hi-lo)))
dr.line(pts,fill='blue',width=3);im.save('nexra_d1.png')
