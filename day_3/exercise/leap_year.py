def validade_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Esse é um ano bissexto")
            else:
                print("Esse NÂO é um ano bissexto")
        else:
            print("Esse é um ano bissexto")
    else:
        print("Esse NÂO é um ano bissexto")


year = input("Insira um ano e veja se ele é bissexto: ")
try:
    year = int(year)
except:
    print("insira um número válido")

validade_leap_year(year)
