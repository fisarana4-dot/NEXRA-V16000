ALLOWED={"image","3d","shape","diagram","video"}
def validate(kind,prompt):
 return kind in ALLOWED and bool(prompt)
