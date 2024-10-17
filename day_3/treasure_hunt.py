print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo à ilha do Tesouro.")
print("Sua missão é encontrar um tesouro.")

# Loop para a primeira escolha
while True:
    first_choice = input("Escolha entre direita ou esquerda\n").lower()
    if first_choice == "esquerda":
        print("Ótima escolha.")
        break  # Sai do loop se a escolha for válida
    elif first_choice == "direita":
        print("O jogo acabou.\nVocê foi pego em uma emboscada de piratas cegos")
        exit()  # Finaliza o jogo
    else:
        print("Insira um valor correto")

# Loop para a segunda escolha
while True:
    second_choice = input("Agora você deseja esperar ou nadar no riacho à sua frente?\n").lower()
    if second_choice == "esperar":
        print("Ótima escolha.")
        break  # Sai do loop se a escolha for válida
    elif second_choice == "nadar":
        print("O jogo acabou.\nVocê entrou em um riacho cheio de piranhas e tubarões e todos os animais te atacaram.")
        exit()  # Finaliza o jogo
    else:
        print("Insira um valor correto")

# Loop para a terceira escolha
while True:
    third_choice = input("Você encontrou um castelo com três portas. Qual você escolhe?\nA vermelha, a amarela ou a azul?\n").lower()
    if third_choice == "amarela":
        print("Ótima escolha.")
        print("Parabéns! Após a sua jornada, você encontrou um baú lotado de joias e ouro, aproveite.")
        break  # Sai do loop após o final do jogo
    elif third_choice == "vermelha":
        print("O jogo acabou.\nVocê entrou em uma sala cheia de armadilhas mortais.")
        exit()  # Finaliza o jogo
    elif third_choice == "azul":
        print("O jogo acabou.\nVocê entrou em uma sala com todos os guardas reunidos em uma reunião.")
        exit()  # Finaliza o jogo
    else:
        print("Insira um valor correto")

