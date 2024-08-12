from module.mylib import food

print("이름: ", food.name)
food.cook()
food.eat()

from module.mylib.food import name, cook, eat


print("이름: ", name)
cook()
eat()