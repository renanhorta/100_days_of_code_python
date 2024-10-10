
def validate_result(result):
    if result < 18.5:
        print(f"Seu IMC é igual a {result}.\nVocê está com o peso abaixo da média")
    elif result < 25.0:
        print(f"Seu IMC é igual a {result}.\nVocê está com o na média")
    elif result < 30.0:
        print(f"Seu IMC é igual a {result}.\nVocê está com o peso acima da média")
    elif result < 35.0:
        print(f"Seu IMC é igual a {result}.\nVocê está obeso")
    else:
        print(f"Seu IMC é igual a {result}.\nVocê está com obesidade clinica")

def BMI(height, weight):   
    try:
        height = float(height)
        weight = float(weight)
    except:
        print("insira valores válidos, separados comm '.' \n")
        return
    
    result = weight / (height ** 2)
    validate_result(round(result, 2))



height = input("Insira o valor da sua altura: ")
weight = input("Insira o valor do seu peso: ")

BMI(height,weight)

