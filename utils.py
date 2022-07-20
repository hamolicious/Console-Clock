from math import cos, floor, radians, sin
from vector import Vec2d

def translate(value: float, leftMin: float, leftMax: float, rightMin: float, rightMax: float) -> float:
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def deg_to_xy(deg: float, rad: int, offset=Vec2d.zero()) -> Vec2d:
	theta = radians(deg)
	return Vec2d(
		floor(rad * cos(theta) + offset.x),
		floor(rad * sin(theta) + offset.y)
	)

def get_screen_size(screen: list[list[int]]) -> Vec2d:
	return Vec2d(len(screen[0]), len(screen))

