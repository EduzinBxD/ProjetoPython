import time, os, random

print("Bem vindo! Deseja começar o quiz?\nTema: DC")

resposta1 = input("Digite (Sim ou Não): ")

if resposta1 == "Sim":
    print("O quiz vai começar!")
else:
    os.system(exit)

#Pergunta 1:
print("Primeira Pergunta: Qual o nome do Batman?\n(A) Bruce Williams\n(B) Bruce Banner\n(C) Bruce Wayne\n(D) Clark Kent")
resposta2 = input("Digite sua resposta: ")

if resposta2 == "C":
    print("Resposta correta!")
else:
    print("Resposta incorreta!")