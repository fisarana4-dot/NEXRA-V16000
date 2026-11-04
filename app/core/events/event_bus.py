class EventBus:
 def __init__(self):
  self.handlers={}
 def subscribe(self,event_type,handler):
  self.handlers.setdefault(event_type,[]).append(handler)
 def publish(self,event_type,payload):
  return [h(payload) for h in self.handlers.get(event_type,[])]
