from FactoryOfCars import stock

my_car=stock[299]
#я купил 300-ю машину у этого завода. Единственная белая машина из партии

print(my_car.color)

print(my_car.price)

print(my_car.engine_rpm)

my_car.start()
#завели машину

my_car.go()
#поехали

print(my_car.engine_rpm,'Это значит,мы тронулись')

