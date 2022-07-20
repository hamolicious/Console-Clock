from math import cos, floor, radians, sin
from vector import Vec2d
from os import system
from time import gmtime
from utils import translate


def generate_screen(width: int, height: int) -> list[list[int]]:
	screen = []
	for _ in range(floor(height)):
		temp = []
		for _ in range(floor(width)):
			temp.append(0)
		screen.append(temp)

	return screen


def display(screen: list[list[int]]) -> None:
	display_string = ''

	for y in range(len(screen)):
		for x in range(len(screen[0])):
			pixel = '  '
			if screen[y][x] != 0 : pixel = screen[y][x]

			display_string += pixel
		display_string += '\n'

	system('cls')
	print(display_string)


