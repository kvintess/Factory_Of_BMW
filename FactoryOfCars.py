#we need to create 1000 cars in our Factory
from CharacteristicsOfCars import Bmw

current_number_of_cars, plan_of_making_cars = 0, 1000
stock = []

while current_number_of_cars < plan_of_making_cars:
    new_car = Bmw()
    stock.append(new_car)
    current_number_of_cars += 1

# we produced 1000 cars in our Factory

stock[299].color='white'
#эта мишина из всей партии будет белой
