#Escolha do tema e palavra
import random
import teste
#Variável para armazenar a palavra escolhida
palavra = ""
#Listas dos temas
print("🎮  Bem-Vindo ao JOGO DA FORCA  🎮")
print("Você quer jogar quantas vezes? ")
quantidadejogos = int(input())
for numero_partidas in range(quantidadejogos):
    tecnologia = ["processador", "teclado", "mouse", "celular"]
    espaco = ["cometa", "gravidade", "nebulosa", "astronauta"]
    mitologia = ["zeus", "ragnarok", "olimpo", "grega"]
 # Usuário escolherá o tema
    print("Escolha um dos 3 temas: \n")
    print("Digite 1 para Tecnologia""\n""Digite 2 para Espaço""\n""Digite 3 para Mitologia")
    choicetheme = int(input())

 #Verificação caso o usuário digite errado o tema
    while choicetheme != 1 and choicetheme != 2 and choicetheme != 3:
        print("🎮  Bem-Vindo ao JOGO DA FORCA  🎮")
        print("Escolha um dos 3 temas: \n")
        print("Digite 1 para Tecnologia""\n""Digite 2 para Espaço""\n""Digite 3 para Mitologia")
        choicetheme = int(input())
        if choicetheme == "Tecnologia" or choicetheme == "Espaço" or choicetheme == "Mitologia":
            break
 #Armazena a palavra aleatória
    if choicetheme == 1:
        palavra = random.choice(tecnologia)
    elif choicetheme == 2:
        palavra = random.choice(espaco)
    elif choicetheme == 3:
        palavra = random.choice(mitologia)

 #Parte principal do jogo
    print(f"Quantidade de partidas: {numero_partidas}")
    teste.jogo_da_forca(palavra)
