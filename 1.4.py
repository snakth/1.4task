from pprint import pprint


# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование,
# определить общие методы взаимодействия с животными и дополнить их в дочерних классах,
# если потребуется.
class Animal:
	legs = 4
	has_fur = True
	hunger = True
	name = None
	weight = None
	animal_type = None

	def __init__(self, name, weigth):
		self.name = name
		self.weight = weigth

	def feeding(self, amount_of_food):
		if amount_of_food > 10:
			self.hunger = False
			print("{} '{}': Животное покормлено".format(self.animal_type, self.name))


class Flying(Animal):
	legs = 2
	wings = 2
	has_fur = "plumage"
	fly = "on ground"
	gathered_resources = ["feather", "eggs"]
	eggs_collected = False

	def flying(self, fly):
		if fly is True:
			self.fly = "ariborne"
			print("{} '{}': Животное взлетело".format(self.animal_type, self.name))
		else:
			self.fly = "on ground"
			print("{} '{}': Животное приземлилось".format(self.animal_type, self.name))

	def collect_eggs(self):
		self.eggs_collected = True
		print("{} '{}': Яйца собраны".format(self.animal_type, self.name))


class Ground(Animal):
	has_horns = True
	gathered_resources = ["leather", "meat", "horn"]
	run = False
	has_fur = True
	milked = None
	wool_collected = None

	def running(self, run):
		if run is True:
			self.run = "running"
			print("{} '{}': Животное побежало".format(self.animal_type, self.name))
		else:
			self.run = "stopped"
			print("{} '{}': Животное остановилось".format(self.animal_type, self.name))

	def milk(self):
		self.milked = True
		print("{} '{}': Подоена".format(self.animal_type, self.name))

	def collect_fur(self):
		self.has_fur = False
		self.wool_collected = True
		print("{} '{}': Шерсть собрана".format(self.animal_type, self.name))


class Goose(Flying):
	animal_type = "Гусь"
	make_sound = "Honk!"


class Cow(Ground):
	animal_type = "Корова"
	make_sound = "Муу!"
	has_fur = False
	milked = False


class Sheep(Ground):
	animal_type = "Овца"
	make_sound = "Бее!"
	wool_collected = False


class Hen(Flying):
	animal_type = "Курица"
	make_sound = "Кудах!"

	def flying(self, fly):
		print("{} '{}': Это животное не умеет летать".format(self.animal_type, self.name))


class Goat(Ground):
	animal_type = "Коза"
	make_sound = "Бее!"
	milked = False


class Duck(Flying):
	animal_type = "Утка"
	make_sound = "Квак!"


# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса.
# Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.


goose1 = Goose("Серый", 10)
goose1.flying(True)
pprint("Goose has a {}".format(goose1.has_fur))
pprint(goose1.__dict__)

goose2 = Goose("Белый", 12)
goose2.feeding(100)
goose2.collect_eggs()
pprint(goose2.__dict__)

cow = Cow("Манька", 530)
cow.milk()
pprint(cow.__dict__)

sheep1 = Sheep("Барашек", 150)
sheep1.collect_fur()
pprint(sheep1.__dict__)

sheep2 = Sheep("Кудрявый", 240)
sheep2.running(True)
pprint(sheep2.__dict__)
sheep2.running(False)
pprint(sheep2.__dict__)

hen1 = Hen("Ко-Ко", 4)
hen1.flying(True)
hen1.collect_eggs()
pprint(hen1.__dict__)

hen2 = Hen("Кукареку", 2)

goat1 = Goat("Рога", 30)
goat2 = Goat("Копыта", 42)

duck = Duck("Кряква", 30)


# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.


animal1 = [goose1.animal_type, goose1.name, goose1.weight]
animal2 = [goose2.animal_type, goose2.name, goose2.weight]
animal3 = [cow.animal_type, cow.name, cow.weight]
animal4 = [sheep1.animal_type, sheep1.name, sheep1.weight]
animal5 = [sheep2.animal_type, sheep2.name, sheep2.weight]
animal6 = [hen1.animal_type, hen1.name, hen1.weight]
animal7 = [hen2.animal_type, hen2.name, hen2.weight]
animal8 = [goat1.animal_type, goat1.name, goat1.weight]
animal9 = [goat2.animal_type, goat2.name, goat2.weight]
animal10 = [duck.animal_type, duck.name, duck.weight]

animals = [animal1, animal2, animal3, animal4, animal5, animal6, animal7, animal8, animal9, animal10]

weights_list = 0
heaviest_animal = None
for animal in animals:
	if animal[2] > weights_list:
		weights_list = animal[2]
		heaviest_animal = animal[0], animal[1]
print(heaviest_animal)

