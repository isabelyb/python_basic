import turtle


def main():
	window = turtle.Screen()
	tortoise = turtle.Turtle()

	make_square(tortoise)

	turtle.mainloop()

def make_square(tortoise):
	length = int(input('Tamano de cuadrado: '))

	for i in range(4):
		make_line_and_turn(tortoise, length)

def make_line_and_turn(tortoise, length):
	tortoise.forward(length)
	tortoise.left(90)


if __name__ == '__main__':
	main()
