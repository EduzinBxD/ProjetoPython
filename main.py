import time, os, random

print("------------------------------------------------------------------------------------------\n")
print("Bem vindo! Deseja começar o quiz?\nTema: DC\n")
print("------------------------------------------------------------------------------------------\n")

querIniciar = input("Digite (Sim ou Não): ")



def checarResposta(respostaCorreta):

    score = 0

    resposta = input("Digite sua resposta: ")

    if resposta == respostaCorreta:
<<<<<<< HEAD
        print("\nResposta correta!\n")
    
=======
        score = score + 1

        print("\nScore: " + str(score) +"\n")
        print("Resposta correta!\n")
>>>>>>> 30e22ea711e5c16c2ce37c194e6795daa784471b
    else:
        print("\nScore: " + str(score) +"\n")
        print("\nResposta incorreta! (Resposta Correta: " + respostaCorreta + ")\n")

if querIniciar == "Sim":
    print("\n------------------------------------------------------------------------------------------\n")
    print("O quiz vai começar!\n")
else:
    os.system(exit)

#Pergunta 1
print("------------------------------------------------------------------------------------------\n")
print("1) Qual o nome do Batman?\n\n(A) Bruce Williams\n(B) Bruce Banner\n(C) Bruce Wayne\n(D) Clark Kent\n")
# Resposta é C
checarResposta("C")

#Pergunta 2
print("------------------------------------------------------------------------------------------\n")
print("2) Qual vilão é conhecido como o 'Príncipe Palhaço do Crime'\n\n(A) Lex Luthor\n(B) Coringa\n(C) Pinguim\n(D) Exterminador\n")
# Resposta é B
checarResposta("B")
    
#Pergunta 3
print("------------------------------------------------------------------------------------------\n")
print("3) De qual planeta a Mulher-Maravilha é originária?\n\n(A) Krypton\n(B) Themyscira\n(C) Oa\n(D) Apokolips\n")
# Resposta é B
checarResposta("B")

#Pergunta 4
print("------------------------------------------------------------------------------------------\n")
print("4) Em qual história o Superman morre lutando contra o Monstro Doomsday?\n\n(A) Crise nas Infinitas Terras\n(B) A Morte do Superman\n(C) Batman: Cavaleiro das Trevas\n(D) Injustiça: Deuses Entre Nos\n")
# Resposta é B
checarResposta("B")

#Pergunta 5
print("------------------------------------------------------------------------------------------\n")
print("5) Qual arqueiro se tornou líder da Liga da Justiça em algumas versões?\n\n(A) Arqueiro Verde (Oliver Queen)\n(B) Arqueiro Vermelho (Roy Harper)\n(C) Gavião Negro (Carter Hall)\n(D) Esquadrão Suicida\n")
# Resposta é A
checarResposta("A")

#Pergunta 6
print("------------------------------------------------------------------------------------------\n")
print("6) Quem interpretou o Batman nos filmes de Christopher Nolan?\n\n(A) Ben Affleck\n(B) Christian Bale\n(C) Michael Keaton\n(D) Robert Pattinson\n")
# Resposta é B
checarResposta("B")

#pergunta 7
print("------------------------------------------------------------------------------------------\n")
print("7) Quem é o Flash mais rápido de todos os tempos?\n\n(A) Barry Allen\n(B) Wally West\n(C) Jay Garrick\n(D) Savitar\n")
# Resposta é B
checarResposta("B")

#Pergunta 8
print("------------------------------------------------------------------------------------------\n")
print("8) Qual vilão é conhecido por roubar a velocidade dos outros?\n\n(A) Zoom (Hunter Zolomon)\n(B) Capitão Frio\n(C) Flash Reverso\n(D) Gorila Grodd\n")
# Resposta é A
checarResposta("A")

#Pergunta 9
print("------------------------------------------------------------------------------------------\n")
print("9) Qual é a principal fraqueza do Superman?\n\n(A) Magia\n(B) Kryptonita\n(C) Chumbo\n(D) Água\n")
# Resposta é B
checarResposta("B")

#Pergunta 10
print("------------------------------------------------------------------------------------------\n")
print("10) Qual desses personagens NÃO é kryptoniano?\n\n(A) Supergirl\n(B) General Zod\n(C) Power Girl\n(D) Martian Manhunter\n")
# Resposta é D
checarResposta("D")

#Pergunta 11
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

#Pergunta 12
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

#Pergunta 13
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

#Pergunta 14
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

#Pergunta 15
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

#Pergunta 16
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

#Pergunta 17
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

#Pergunta 18
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

#Pergunta 19
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

#Pergunta 20
print("------------------------------------------------------------------------------------------\n")
print("0) Template?\n\n(A) Null\n(B) Null\n(C) Null\n(D) Null\n")
# Resposta é D
checarResposta("D")

print("------------------------------------------------------------------------------------------\n")

input("Tecle Enter para sair...")