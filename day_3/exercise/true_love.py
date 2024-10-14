name1 = input("Insira o seu nome: ")
name2 = input("Insira o nome de quem você ama: ")

def count_points(name1,name2):
    """TRUE LOVE (count of T, R, U, E, L, O, V)"""
    points =0
    points2 =0
    names = name1 + name2
    names = names.lower()
    points += names.count("t")
    points += names.count("r")
    points += names.count("u")
    points += names.count("e")
    points2 += names.count("l")
    points2 += names.count("o")
    points2 += names.count("v")
    points2 += names.count("e")

    return str(points) +str(points2)

def verify_love(name1, name2):

    total_love_points = int(count_points(name1,name2))

    if total_love_points <= 10 or total_love_points >= 90:
        print(f"Vocês tem {total_love_points} pontos. Vão ficar juntos igual coca e mentos")
    elif 40 >= total_love_points <= 50:
        print(f"Vocês tem {total_love_points} pontos. Vão ficar bem.")
    else:
        print(f"Vocês tem {total_love_points} pontos.")
    
verify_love(name1, name2)