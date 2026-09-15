from .domains import DOMAINS
def build(name,source):
 return f"site:{DOMAINS.get(source,source)} {name}"
