user_heigth = input("Insira a sua altura. Em cm: ")
user_age = input("Insira a sua idade: ")
ticket_value = 0

try:
    user_heigth = int(user_heigth)
    user_age = int(user_age)
except:
    print("Entradas inválidas. Insira os números corretos.")

if user_heigth < 120:
    print("Você não pode andar por ser menor que 1.20 metros.")
else:
    print("Pode entrar no brinquedo. Sua altura é válida.")
    if user_age < 12:
        ticket_value = 5
        print("o preço do seu ingresso é de: R$5.00")
    elif user_age <= 18:
        ticket_value = 7
        print("o preço do seu ingresso é de: R$7.00")
    else:
        ticket_value = 12
        print("o preço do seu ingresso é de: R$12.00")

    response_photo = input("Você deseja uma foto do momento, a foto custa R$3.00? Y ou N\n")
    if response_photo.upper() == 'Y':
        ticket_value += 3
        print(f"Foto adicionada. Valor a pagar R${ticket_value} ")
    else:
        print(f"Agradeçemos sua participção, não será adicionada uma foto.. Valor a pagar R${ticket_value} ")