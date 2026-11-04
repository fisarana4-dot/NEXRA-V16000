from app.core.events.event_bus import EventBus
def test_event_bus():
 b=EventBus()
 b.subscribe("x",lambda p:p["ok"])
 assert b.publish("x",{"ok":1})==[1]
