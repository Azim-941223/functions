

def menu():
    f = open("menu.txt", 'w')
    print("Что вы хотели заказать? ")
    eat = input("Что вы хотите есть: ")
    water = input("Что вы хотите пить: ")
    f.write(f"{eat}, {water}")
    f.close()
menu()