import time, os, random

print("------------------------------------------------------------------------------------------\n")
print("Bem vindo! Deseja começar o quiz?\nTema: DC\n")
print("------------------------------------------------------------------------------------------\n")

querIniciar = input("Digite (Sim ou Não): ")

globalScore = 0

def checarResposta(respostaCorreta):
    resposta = input("Digite sua resposta: ")

    score = globalScore

    if resposta == respostaCorreta:
        score = score + 1

        print(f"\nPontução: {score}\n")
        print("Resposta correta!\n")
    else:
        print(f"\nPontuação: {score}\n")
        print("Resposta incorreta! (Resposta Correta: " + respostaCorreta + ")\n")

    return score

# Começar Quiz
if querIniciar == "Sim":
    print("\n------------------------------------------------------------------------------------------\n")
    print("O quiz vai começar!\n")
else:
    quit()

#Pergunta 1
print("------------------------------------------------------------------------------------------\n")
print("1) Qual o nome do Batman?\n\n(A) Bruce Williams\n(B) Bruce Banner\n(C) Bruce Wayne\n(D) Clark Kent\n")
# Resposta é C
globalScore = checarResposta("C")

#Pergunta 2
print("------------------------------------------------------------------------------------------\n")
print("2) Qual vilão é conhecido como o 'Príncipe Palhaço do Crime'\n\n(A) Lex Luthor\n(B) Coringa\n(C) Pinguim\n(D) Exterminador\n")
# Resposta é B
globalScore = checarResposta("B")
    
#Pergunta 3
print("------------------------------------------------------------------------------------------\n")
print("3) De qual planeta a Mulher-Maravilha é originária?\n\n(A) Krypton\n(B) Themyscira\n(C) Oa\n(D) Apokolips\n")
# Resposta é B
globalScore = checarResposta("B")

#Pergunta 4
print("------------------------------------------------------------------------------------------\n")
print("4) Em qual história o Superman morre lutando contra o Monstro Doomsday?\n\n(A) Crise nas Infinitas Terras\n(B) A Morte do Superman\n(C) Batman: Cavaleiro das Trevas\n(D) Injustiça: Deuses Entre Nos\n")
# Resposta é B
globalScore = checarResposta("B")

#Pergunta 5
print("------------------------------------------------------------------------------------------\n")
print("5) Qual arqueiro se tornou líder da Liga da Justiça em algumas versões?\n\n(A) Arqueiro Verde (Oliver Queen)\n(B) Arqueiro Vermelho (Roy Harper)\n(C) Gavião Negro (Carter Hall)\n(D) Esquadrão Suicida\n")
# Resposta é A
globalScore = checarResposta("A")

#Pergunta 6
print("------------------------------------------------------------------------------------------\n")
print("6) Quem interpretou o Batman nos filmes de Christopher Nolan?\n\n(A) Ben Affleck\n(B) Christian Bale\n(C) Michael Keaton\n(D) Robert Pattinson\n")
# Resposta é B
globalScore = checarResposta("B")

#pergunta 7
print("------------------------------------------------------------------------------------------\n")
print("7) Quem é o Flash mais rápido de todos os tempos?\n\n(A) Barry Allen\n(B) Wally West\n(C) Jay Garrick\n(D) Savitar\n")
# Resposta é B
globalScore = checarResposta("B")

#Pergunta 8
print("------------------------------------------------------------------------------------------\n")
print("8) Qual vilão é conhecido por roubar a velocidade dos outros?\n\n(A) Zoom (Hunter Zolomon)\n(B) Capitão Frio\n(C) Flash Reverso\n(D) Gorila Grodd\n")
# Resposta é A
globalScore = checarResposta("A")

#Pergunta 9
print("------------------------------------------------------------------------------------------\n")
print("9) Qual é a principal fraqueza do Superman?\n\n(A) Magia\n(B) Kryptonita\n(C) Chumbo\n(D) Água\n")
# Resposta é B
globalScore = checarResposta("B")

#Pergunta 10
print("------------------------------------------------------------------------------------------\n")
print("10) Qual desses personagens NÃO é kryptoniano?\n\n(A) Supergirl\n(B) General Zod\n(C) Power Girl\n(D) Martian Manhunter\n")
# Resposta é D
globalScore = checarResposta("D")

#Pergunta 11
print("------------------------------------------------------------------------------------------\n")
print("11) Quem matou os pais de Bruce Wayne?\n\n(A) Joe Chill\n(B) Coringa\n(C) Pinguim\n(D) Carmine Falcone\n")
# Resposta é A
globalScore = checarResposta("A")

#Pergunta 12
print("------------------------------------------------------------------------------------------\n")
print("12) Em que quadrinho a Liga da Justiça foi formada pela primeira vez?\n\n(A) Justice League #1 (1987)\n(B) Justice League of America #1 (1960)\n(C) Crisis on Infinite Earths #1\n(D) DC Universe Rebirth #1\n")
# Resposta é B
globalScore = checarResposta("B")

#Pergunta 13
print("------------------------------------------------------------------------------------------\n")
print("13) Qual heroína é conhecida como Princesa das Amazonas?\n\n(A) Supergirl\n(B) Zatanna\n(C) Mullher-Maravilha\n(D) Hera Venenosa\n")
# Resposta é C
globalScore = checarResposta("C")

#Pergunta 14
print("------------------------------------------------------------------------------------------\n")
print("14) Qual é o nome da cidade protegida pelo Superman?\n\n(A) Gotham City\n(B) Central City\n(C) Metrópolis\n(D) Star City\n")
# Resposta é C
globalScore = checarResposta("C")

#Pergunta 15
print("------------------------------------------------------------------------------------------\n")
print("15) Qual membro da Liga da Justiça tem um anel com poderes construídos pela força de vontade?\n\n(A) Lanterna Verde\n(B) Aquaman\n(C) Shazam\n(D) Flash\n")
# Resposta é A
globalScore = checarResposta("A")

#Pergunta 16
print("------------------------------------------------------------------------------------------\n")
print("16) Quem é o alter ego do Flash mais conhecido?\n\n(A) Wally West\n(B) Jay Garrick\n(C) Bart Allen\n(D) Barry Allen\n")
# Resposta é D
globalScore = checarResposta("D")

#Pergunta 17
print("------------------------------------------------------------------------------------------\n")
print("17) Qual herói da DC é conhecido por conversar com animais marinhos?\n\n(A) Superman\n(B) Ciborgue\n(C) Batman\n(D) Aquaman\n")
# Resposta é D
globalScore = checarResposta("D")

#Pergunta 18
print("------------------------------------------------------------------------------------------\n")
print("18) Quem é a parceira e interesse romântico recorrente do Coringa?\n\n(A) Mulher-Gato\n(B) Arlequina\n(C) Hera Venenosa\n(D) Zatanna\n")
# Resposta é B
globalScore = checarResposta("B")

#Pergunta 19
print("------------------------------------------------------------------------------------------\n")
print("19) Quem foi o segundo Robin?\n\n(A) Tim Drake\n(B) Jason Todd\n(C) Damian Wayne\n(D) Terry McGinnis\n")
# Resposta é B
globalScore = checarResposta("B")

#Pergunta 20
print("------------------------------------------------------------------------------------------\n")
print("20) Qual é o nome do planeta natal do Superman?\n\n(A) Marte\n(B) Oa\n(C) Apokolips\n(D) Krypton\n")
# Resposta é D
globalScore = checarResposta("D")

print("------------------------------------------------------------------------------------------\n")

print(f"Pontuação Final: {globalScore}\n")

input("Tecle Enter para sair...")