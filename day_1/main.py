while True:
    city_name = input("insira o nome da sua cidade: ")
    if city_name == "" or city_name.isdigit():
        print("nome de cidade inválida.")
        continue
    else:
        break

while True:
    pet_name = input("insira o nome do seu pet: ")
    if pet_name == "" or pet_name.isdigit():
        print("nome de pet inválido.")
        continue
    else:
        break


print(f"\n\nO nome da sua banda poderia ser. \n {city_name} {pet_name}")