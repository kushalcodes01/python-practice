class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(45)
n2 = Number(55)

print(n1 + n2)