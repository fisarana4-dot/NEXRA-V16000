import os
class ICMConfig:
 enabled=os.getenv("ICM_ENABLED","false").lower()=="true"
 server=os.getenv("ICM_SERVER","")
