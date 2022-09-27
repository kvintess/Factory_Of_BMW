from FactoryOfCars import stock

my_car=stock[299]
#я купил 300-ю машину у этого завода. Единственная белая машина из партии
my_car.go()
#я на ней поехал
print(my_car.current_velocity, 'км в час после старта')
#текущая скорость
my_car.is_clean = 'машина стала грязной'
#создал аттрибут, который говорит,чистая машина или нет
print(my_car.is_clean)
#я проехался на ней и она стала грязной
while my_car.current_velocity < 100:
    my_car.current_velocity += 1
#разгоню её до 100
print(my_car.current_velocity, 'км в час после разгона')

my_car.error_attribute = 'я хочу удалить этот аттрибут'
del my_car.error_attribute

#установим новые attr для нашей машины с помощью цикла
new_attributes= ['weight','height']
for new_attr in new_attributes:
    setattr(my_car, new_attr, '3meters')
print(my_car.weight)
print(getattr(my_car, "height"))

#поедем в другую страну в какой-либо город
my_car.travel('Лондон', 'Англия')

