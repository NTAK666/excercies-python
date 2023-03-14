import random
import sys
import uuid

from pandas._libs.internals import defaultdict


class Shape:
	def __init__(self, name):
		self.name = name

	def area(self):
		pass

	def perimeter(self):
		pass

	def overlaps(self, other):
		pass


class Circle(Shape):
	def __init__(self, radius, x, y, name):
		super().__init__(name)
		self.radius = radius
		self.x = x
		self.y = y

	def area(self):
		return 3.14 * self.radius ** 2

	def perimeter(self):
		return 2 * 3.14 * self.radius

	def overlaps(self, other):
		if isinstance(other, Circle):
			distance_between_centers = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
			sum_of_radii = self.radius + other.radius
			if distance_between_centers <= sum_of_radii:
				return True
			else:
				return False
		elif isinstance(other, Rectangle):
			return other.overlaps(other)
		elif isinstance(other, Triangle):
			return other.overlaps(other)


class Rectangle(Shape):
	def __init__(self, width, height, x, y, name):
		super().__init__(name)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	def area(self):
		return self.width * self.height

	def perimeter(self):
		return 2 * (self.width + self.height)

	def overlaps(self, other):
		if isinstance(other, Circle):
			return other.overlaps(other)
		elif isinstance(other, Rectangle):
			x_overlap = (self.x < other.x + other.width) and (other.x < self.x + self.width)
			y_overlap = (self.y < other.y + other.height) and (other.y < self.y + self.height)
			return x_overlap and y_overlap
		elif isinstance(other, Triangle):
			return other.overlaps(other)


class Triangle(Shape):
	def __init__(self, a, b, c, y, x, name):
		super().__init__(name)
		self.a = a
		self.b = b
		self.c = c
		self.x = y
		self.y = x

	def area(self):
		return abs((self.a * (self.b - self.c) + self.b * (self.c - self.a) + self.c * (self.a - self.b)) / 2)

	def perimeter(self):
		return self.a + self.b + self.c

	def overlaps(self, other):
		if isinstance(other, Circle):
			return other.overlaps(other)
		elif isinstance(other, Rectangle):
			return other.overlaps(other)
		elif isinstance(other, Triangle):
			min_x = min(self.x, other.x, self.x + self.a, other.x + other.a, self.x + self.a + self.b,
									other.x + other.a + other.b, self.x + self.a + self.c, other.x + other.a + other.c)
			max_x = max(self.x, other.x, self.x + self.a, other.x + other.a, self.x + self.a + self.b,
									other.x + other.a + other.b, self.x + self.a + self.c, other.x + other.a + other.c)
			min_y = min(self.y, other.y, self.y + self.b, other.y + other.b, self.y + self.b + self.c,
									other.y + other.b + other.c, self.y + self.c + self.a, other.y + other.c + other.a)
			max_y = max(self.y, other.y, self.y + self.b, other.y + other.b, self.y + self.b + self.c,
									other.y + other.b + other.c, self.y + self.c + self.a, other.y + other.c + other.a)

			if max_x < (min_x + max(self.a, other.a)) and max_y < (min_y + max(self.b, other.b)):
				return True
			else:
				return False


def random_shape():
	with open('input.txt', 'w') as f:
		for i in range(1000):
			shape = random.choice(['CIRCLE', 'RECTANGLE', 'TRIANGLE'])
			if shape == 'CIRCLE':
				radius = random.randint(1, 10000)
				x = random.randint(1, 10000)
				y = random.randint(1, 10000)
				f.write(f'#{shape}\n{get_random_unique_name_for_shape()}\n{radius}\n{x} {y}\n')
			elif shape == 'RECTANGLE':
				x = random.randint(1, 10000)
				y = random.randint(1, 10000)
				width = random.randint(1, 10000)
				height = random.randint(1, 10000)
				f.write(f'#{shape}\n{get_random_unique_name_for_shape()}\n{width} {height}\n{x}  {y}\n')
			elif shape == 'TRIANGLE':
				a, b, c = random.randint(1, 10000), random.randint(1, 10000), random.randint(1, 10000)
				x = random.randint(1, 10000)
				y = random.randint(1, 10000)

				while a + b <= c or a + c <= b or b + c <= a:
					a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
					x = random.randint(1, 100)
					y = random.randint(1, 100)

				f.write(f'#{shape}\n{get_random_unique_name_for_shape()}\n{a} {b} {c}\n{x} {y}\n')


def get_random_unique_name_for_shape():
	return uuid.uuid4()


def get_shapes():
	shapes = []
	with open('input.txt', 'r') as f:
		lines = f.readlines()
		i = 0
		while i < len(lines):
			shape_type = lines[i].strip()[1:]  # skip the '#'
			if shape_type == 'CIRCLE':
				name = lines[i + 1].strip()
				radius = int(lines[i + 2].strip())
				x, y = map(int, lines[i + 3].strip().split())
				shapes.append(Circle(radius, x, y, name))
				i += 4
			elif shape_type == 'TRIANGLE':
				name = lines[i + 1].strip()
				a, b, c = map(int, lines[i + 2].strip().split())
				x, y = map(int, lines[i + 3].strip().split())
				shapes.append(Triangle(a, b, c, x, y, name))
				i += 4
			elif shape_type == 'RECTANGLE':
				name = lines[i + 1].strip()
				width, height = map(int, lines[i + 2].strip().split())
				x, y = map(int, lines[i + 3].strip().split())
				shapes.append(Rectangle(width, height, x, y, name))
				i += 4
	return shapes


def get_max_overlaps(shapes):
	overlaps = defaultdict(int)
	for i, shape1 in enumerate(shapes):
		for j, shape2 in enumerate(shapes):
			if i == j:
				continue
			if shape1.overlaps(shape2):
				overlaps[shape1.name] += 1
	if not overlaps:
		return 0
	return max(overlaps.values())


if __name__ == '__main__':
	sys.setrecursionlimit(100000)
	random_shape()
	shapes = get_shapes()
	max_area = max(shapes, key=lambda x: x.area())
	max_perimeter = max(shapes, key=lambda x: x.perimeter())
	print(f'''
    The shape with the largest area is {max_area.name} x: {max_area.x} y: {max_area.y} with area {max_area.area()}
    The shape with the largest perimeter is {max_perimeter.name} x: {max_area.x} y: {max_area.y} with perimeter {max_perimeter.perimeter()}
		The maximum number of overlaps is {get_max_overlaps(shapes)}
	''')
