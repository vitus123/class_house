
class House:

    def __init__(self):
        self.numberOfFloors = 10


n = 0
my_house = House()
while n < my_house.numberOfFloors:
    n += 1
    print('Текущий этаж равен: ', n)

# Предполагаю, что неправильно понял задание, поэтому ещё онин вариант решения
print('И другшй вариант')

while my_house.numberOfFloors > 0:
    print('Текущий этаж равен: ',my_house.numberOfFloors)
    my_house.numberOfFloors -=1


