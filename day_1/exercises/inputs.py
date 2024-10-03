#dizer quantos numeros tem um um input

def calc_size(name):
    name_separeted = name.replace(" ", "")
    size = len(name_separeted)
    return size

def ask_name():
    while True:
        name = input("Digite o seu nome: ")
        if name == "" or name.isdigit():
            print("nome inválido\n\n")
            continue
        else:
            size = calc_size(name)
            print(size)
            break

ask_name()