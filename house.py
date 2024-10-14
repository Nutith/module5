class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return isinstance(other, House) and self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return isinstance(other, House) and self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return isinstance(other, House) and self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return isinstance(other, House) and self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return isinstance(other, House) and self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors += other

        return self

    def __radd__(self, other):
        return House.__add__(self, other)

    def __iadd__(self, other):
        return House.__add__(self, other)

    def __sub__(self, other):
        if isinstance(other, int):
            if other < self.number_of_floors:
                self.number_of_floors -= other
            else:
                self.number_of_floors = 1  # допустим, что сдание не может иметь меньше одного этажа

        return self

    def __rsub__(self, other):
        if isinstance(other, int):
            if self.number_of_floors < other:
                self.number_of_floors = other - self.number_of_floors
            else:
                self.number_of_floors = 1  # допустим, что сдание не может иметь меньше одного этажа

        return self

    def __isub__(self, other):
        return House.__sub__(self, other)

    def __mul__(self, other):
        if isinstance(other, int) and other > 0:  # не будем умножать на ноль и отрицательные числа
            self.number_of_floors *= other

        return self

    def __rmul__(self, other):
        return House.__mul__(self, other)

    def __imul__(self, other):
        return House.__mul__(self, other)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
            return

        for floor in range(1, new_floor+1):
            print(floor)