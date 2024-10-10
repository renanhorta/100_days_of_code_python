while True:
    user_number = input("Insira um valor para saber se é par ou impar: ")
    if user_number.isdigit() != True:
        print("Insira um valor numérico. \n\n")
        continue
    elif int(user_number) <= 0:
        print("Insira um valor maior que zero. \n\n")
        continue
    else:
        result = int(user_number) % 2
        if result == 0:
            print(f"O número {user_number} é um número PAR.")
        else:
            print(f"O número {user_number} é um número IMPAR.")
        break