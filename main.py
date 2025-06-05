import time, os, random

print("------------------------------------------------------------------------------------------\n")
print("Bem vindo! Deseja começar o quiz?\nTema: DC\n")
print("------------------------------------------------------------------------------------------\n")

querIniciar = input("Digite (Sim ou Não): ")

if querIniciar == "Sim":
    print("\n------------------------------------------------------------------------------------------\n")
    print("O quiz vai começar!\n")
else:
    os.system(exit)

#Pergunta 1
print("------------------------------------------------------------------------------------------\n")
print("1) Qual o nome do Batman?\n\n(A) Bruce Williams\n(B) Bruce Banner\n(C) Bruce Wayne\n(D) Clark Kent\n")
resposta1 = input("Digite sua resposta: ")

if resposta1 == "C":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")

#Pergunta 2
print("------------------------------------------------------------------------------------------\n")
print("2) Qual vilão é conhecido como o 'Príncipe Palhaço do Crime'\n\n(A)Lex Luthor\n(B)Coringa\n(C)Pinguim\n(D)Exterminador\n")
resposta2 = input("Digite sua resposta: ")
if resposta2 == "B":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")
    
#Pergunta 3
print("------------------------------------------------------------------------------------------\n")
print("3) De qual planeta a Mulher-Maravilha é originária?\n\n(A)Krypton\n(B)Themyscira\n(C)Oa\n(D)Apokolips\n")
resposta3 = input("Digite sua resposta: ")
if resposta3 == "B":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")

#Pergunta 4
print("------------------------------------------------------------------------------------------\n")
print("4) Em qual história o Superman morre lutando contra o Monstro Doomsday?\n\n(A)Crise nas Infinitas Terras\n(B)A Morte do Superman\n(C)Batman: Cavaleiro das Trevas\n(D)Injustiça: Deuses Entre Nos\n")
resposta4 = input("Digite sua resposta: ")
if resposta4 == "B":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")

#Pergunta 5
print("------------------------------------------------------------------------------------------\n")
print("5) Qual arqueiro se tornou líder da Liga da Justiça em algumas versões?\n\n(A)Arqueiro Verde (Oliver Queen)\n(B) Arqueiro Vermelho (Roy Harper)\n(C)Gavião Negro (Carter Hall)\n(D)Esquadrão Suicida\n")
resposta5 = input("Digite sua resposta: ")
if resposta5 == "A":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")

#Pergunta 6
print("------------------------------------------------------------------------------------------\n")
print("6) Quem interpretou o Batman nos filmes de Christopher Nolan?\n\n(A)Ben Affleck\n(B)Christian Bale\n(C)Michael Keaton\n(D)Robert Pattinson\n")
resposta6 = input("Digite sua resposta: ")
if resposta6 == "B":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")

#pergunta 7
print("------------------------------------------------------------------------------------------\n")
print("7) Quem é o Flash mais rápido de todos os tempos?\n\n(A)Barry Allen\n(B)Wally West\n(C)Jay Garrick\n(D)Savitar\n")
resposta7 = input("Digite sua resposta: ")
if resposta7 == "B":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")

#Pergunta 8
print("------------------------------------------------------------------------------------------\n")
print("8) Qual vilão é conhecido por roubar a velocidade dos outros?\n\n(A)Zoom (Hunter Zolomon)\n(B)Capitão Frio\n(C)Flash Reverso\n(D)Gorila Grodd\n")
resposta8 = input("Digite sua resposta: ")
if resposta8 == "A":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")

#Pergunta 9
print("------------------------------------------------------------------------------------------\n")
print("9) Qual é a principal fraqueza do Superman?\n\n(A)Magia\n(B)Kryptonita\n(C)Chumbo\n(D)Água\n")
resposta9 = input("Digite sua resposta: ")
if resposta9 == "B":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")

#Pergunta 10
print("------------------------------------------------------------------------------------------\n")
print("10) Qual desses personagens NÃO é kryptoniano?\n\n(A)Supergirl\n(B)General Zod\n(C)Power Girl\n(D)Martian Manhunter\n")
resposta10 = input("Digite sua resposta: ")
if resposta10 == "D":
    print("\nResposta correta!\n")
else:
    print("\nResposta incorreta!\n")

print("------------------------------------------------------------------------------------------\n")

input("Tecle Enter para sair...")