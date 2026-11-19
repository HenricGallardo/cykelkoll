import math


def headwind(wind_speed_ms: float, wind_from_deg: float, bike_direction_deg: float) -> float:
    """How much of the wind hits you head-on while cycling.

    wind_from_deg: where the wind comes FROM (0 = north, 90 = east, 180 = south, 270 = west).
    bike_direction_deg: the direction you are cycling TOWARDS, on the same scale.

    Returns m/s: positive = headwind, negative = tailwind, around 0 = crosswind.
    """
    angle = math.radians(wind_from_deg - bike_direction_deg)
    return wind_speed_ms * math.cos(angle)
    