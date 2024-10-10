def validade_input_size(input):
    if input.upper() not in ['S', 'M', 'L']:
        return False
    else:
        return True
    
def validade_input_extra(input):
    if input.upper() not in ['Y', 'N']:
        return False
    else:
        return True

def menu():
    small_pizza = 15.00
    medium_pizza = 20.00
    large_pizza = 25.00
    add_pepperoni_small = 2.00
    add_pepperoni_not_small = 3.00
    add_cheese = 1.00
    value_to_pay=0


    print("Bem vindo ao pizza Delivery")
    while True:
        size = input("Qual o tamanho de pizza desejado? S, M, L\n")
        pepperoni_extra = input("Deseja adicionar Pepperoni? Y ou N\n")
        cheese_extra = input("Deseja adicionar queijo? Y ou N\n")

        if validade_input_size(size) != True:
            print("Informe um valor válido para o tamanho da pizza\n\n")
            continue
        elif validade_input_extra(pepperoni_extra) != True:
            print("Informe um valor válido para a adição de pepperoni Y ou N\n\n")
            continue      
        elif validade_input_extra(cheese_extra) != True:
            print("Informe um valor válido para a adição de queijo Y ou N\n\n")
            continue        
        else:
            break
    
    if size.upper() == "S":
        value_to_pay += small_pizza
    elif size =="M":
        value_to_pay += medium_pizza
    else:
        value_to_pay += large_pizza

    if pepperoni_extra.upper() == "Y":
        if size == "S":
            value_to_pay += add_pepperoni_small
        else:
            value_to_pay += add_pepperoni_not_small

    if cheese_extra.upper() == "Y":
        value_to_pay += add_cheese

    print(f"O valor total da pizza é igual a {value_to_pay}")


menu()