def name_file(a):
    y = open(f'{a}.txt', 'w') 
    y.close()

x = input()
name_file(x)
