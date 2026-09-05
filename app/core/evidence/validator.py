def validate(e):
 return bool(e.source and e.domain and e.timestamp and isinstance(e.data,dict))
