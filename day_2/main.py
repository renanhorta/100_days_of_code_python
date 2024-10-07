#Tip calculator

def tip_calculator():
    total_bill = float(input("Qual o valor total da conta? "))
    total_people = int(input("Quantas pessoas tem na mesa? "))
    tip_percentage = int(input("Qual a porcentagem de gorgeta? 10, 12 ou 15? "))

    total_bill = round(total_bill * ((tip_percentage/100)+1),2)
    each_person = round((total_bill/ total_people), 2)

    print(f"Cada pessoa deve pagar R${each_person}.")

tip_calculator()