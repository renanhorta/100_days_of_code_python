def BMI(height, weight):
    height = float(height)
    weight = float(weight)
    if height or weight != None or "":
        result = float((weight) / (height **2))
        return round(result, 2)
    else:
        return "Informe os valores corretos"


height = input("Insira o valor da sua altura: ")
weight = input("Insira o valor do seu peso: ")

print(BMI(float(height), float(weight)))