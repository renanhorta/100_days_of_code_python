#adicine um input de 2 digitos e faça a soma dos valores do input. se entrar com 35 o valor total é 3+ 5 = 8 retornando 8


while True:
    num_input = input("Digite um número de 2 digitos: ")
    if num_input.isdigit() == False:
        print("Insira um número válido somente com números")
        continue
    elif len(num_input) != 2:
        print("Insira um número válido de somente 2 digitos")
        continue
    else:
        result_num = int(num_input[0]) + int(num_input[1])
        print("A soma é igual a: " + str(result_num) + ".")
        break
