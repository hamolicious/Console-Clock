from math import floor
from vector import Vec2d
from time import gmtime
from utils import deg_to_xy, get_screen_size, translate


def draw_pixel(screen: list[list[int]], pos: Vec2d, char: str, xterm: int) -> None:
	x_overflow = pos.x >= 0 and pos.x < get_screen_size(screen).w
	y_overflow = pos.y >= 0 and pos.y < get_screen_size(screen).h

	if x_overflow and y_overflow:
		screen[floor(pos.y)][floor(pos.x)] = f'\u001b[48;5;{xterm}m{char}\u001b[0m'


def draw_circle(screen: list[list[int]], pos: Vec2d, rad: int, char: str, xterm=0) -> None:
	for angle in range(0, 360, 1):
		dest = deg_to_xy(angle + 90, rad, offset=pos)
		draw_pixel(screen, dest, char, xterm)


def draw_line(screen: list[list[int]], from_pos: Vec2d, to_pos: Vec2d, char: str, xterm: int) -> None:
	direction = to_pos.sub(from_pos).normalised()
	while from_pos.dist(to_pos) > 2:
		draw_pixel(screen, from_pos, char, xterm)
		from_pos.iadd(direction)


def draw_line_from_deg(screen: list[list[int]], from_pos: Vec2d, deg: float, length: float, char: str, xterm=0) -> None:
	dest = deg_to_xy(deg, int(length), offset=from_pos)
	draw_line(screen, from_pos, dest, char, xterm)


def draw_seconds(screen: list[list[int]], pos: Vec2d, rad: int, char: str, xterm=0) -> None:
	angle = translate(gmtime().tm_sec, 0, 61, 0, 360) - 90
	draw_line_from_deg(screen, pos, angle, rad, char, xterm)


def draw_minutes(screen: list[list[int]], pos: Vec2d, rad: int, char: str, xterm=0) -> None:
	angle = translate(gmtime().tm_min, 0, 59, 0, 360) - 90
	draw_line_from_deg(screen, pos, angle, rad, char, xterm)


def draw_hours(screen: list[list[int]], pos: Vec2d, rad: int, char: str, xterm=0) -> None:
	angle = translate((gmtime().tm_hour + 1) % 12, 0, 12, 0, 360) - 90
	draw_line_from_deg(screen, pos, angle, rad, char, xterm)


def draw_numbers(screen: list[list[int]], pos: Vec2d, rad: int) -> None:
	number = 1
	offset = int(360/12) - 90
	for angle in range(0, 360, int(360/12)):
		dest = deg_to_xy(angle + offset, rad, offset=pos)
		draw_pixel(screen, dest, f'{number:02}', 0)
		number += 1


def draw_border(
	screen: list[list[int]],
	char_left: str,
	char_right: str,
	char_top: str,
	char_bottom: str,
	xterm=0
) -> None:
	screen_size = get_screen_size(screen)
	for y in range(len(screen)):
		for x in range(len(screen[0])):
			if x == 0                 : draw_pixel(screen, Vec2d(x, y), char_left, xterm)
			if x == screen_size.w - 1 : draw_pixel(screen, Vec2d(x, y), char_right, xterm)
			if y == 0                 : draw_pixel(screen, Vec2d(x, y), char_top, xterm)
			if y == screen_size.h - 1 : draw_pixel(screen, Vec2d(x, y), char_bottom, xterm)
