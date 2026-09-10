import json
def build(rows):
 out=[]
 for r in rows: out.append(f"ID={r[0]} SOURCE={r[1]} DOMAIN={r[2]} DATA={r[3]}")
 return "\n".join(out)
