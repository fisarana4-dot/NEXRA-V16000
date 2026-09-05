from dataclasses import dataclass
@dataclass
class Instrument:
 symbol:str;tick_size:float;tick_value:float
 volume_min:float;volume_max:float;volume_step:float
