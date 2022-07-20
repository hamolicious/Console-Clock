from vector import Vec2d
from clock import display, generate_screen
from draw import draw_border, draw_circle, draw_hours, draw_minutes, draw_seconds, draw_numbers
from time import time
import os

if __name__ == '__main__':
	prev_time = time()
	prev_screen_size = Vec2d(0, 0)
	refresh = False

	while True:
		terminal_size = os.get_terminal_size()

		screen_size = Vec2d(
			(terminal_size.columns / 2) - 2,
			terminal_size.lines - 2
		)
		half_screen_size = screen_size.copy().div(2)
		circle_rad = min(screen_size.w, screen_size.h) * 0.45
		sec_rad = circle_rad * 0.5
		min_rad = circle_rad * 0.75
		hour_rad = circle_rad * 0.9

		screen = generate_screen(screen_size.x, screen_size.h)

		draw_border(screen, '| ', ' |', '__', '--', 0)
		draw_circle(screen, half_screen_size.copy(), circle_rad, '  ', 138)
		draw_hours(screen, half_screen_size.copy(), hour_rad, '  ', 12)
		draw_minutes(screen, half_screen_size.copy(), min_rad, '  ', 10)
		draw_seconds(screen, half_screen_size.copy(), sec_rad, '  ', 11)
		draw_numbers(screen, half_screen_size.copy(), circle_rad - 3)

		if time() - prev_time > 1:
			refresh = True
			prev_time = time()

		if prev_screen_size.sub(screen_size).as_ints() != [0, 0]:
			refresh = True
			prev_screen_size = screen_size.copy()

		if refresh:
			display(screen)
			refresh = False

