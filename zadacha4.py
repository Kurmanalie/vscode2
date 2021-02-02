def menu(a,b):
    y = open('/home/sezim/Рабочий стол/menu.txt', 'w')
    y.write(f'{a} \n{b}')

a=input("Chto vy hoteliby zakazt': ")
b=input("Chto vy hoteliby vypit': ")

menu(a,b)