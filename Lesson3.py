age = 25 #integer\# инициализация переменной типа int
print("Возраст: " + str(age)) # Вывод переменной age после преобразования в тип str
print("Возраст: ", age) #Вывод переменной age

temp = 5.9 #float #Инициализация переменной типа float
print("Температура:", temp, "градусов") #Вывод переменной temp

username = "Alex" #string\str #Инициализация переменной типа str
print("Имя пользователя:", username); print("Имя пользователя:", username) #Вывод переменной username дважды

isexists = True #boolean # Инициализация переменной типа bool
print('Существует:', isexists) # Вывод переменной isexistr
isexists = False #boolean\bool # Изминение значения переменной isexistr 
print('Существует:', isexists) ## Вывод переменной isexistr

age = "18.5" # Изминение значения и типа переменной age
print("Возраст: " + age) # Вывод переменной age

'''Выводим типы переменных
с помощью функции print и type'''

print("Тип переменной age: ", type(age))
print("Тип переменной temp: ", type(temp))
print("Тип переменной isexists: ", type(isexists))
print("Тип переменной integer: ", type(10))

#Создание многострочного значения строковой переменной
text = '''Первая страка
Вторая строка
Третья строка'''

print(text) #Вывод переменной text