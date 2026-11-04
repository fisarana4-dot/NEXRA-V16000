def allow(direction,open_direction=None,losing=False):
 if open_direction is None:return True
 if direction==open_direction and losing:return False
 return True
