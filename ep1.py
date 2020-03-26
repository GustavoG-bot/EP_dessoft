#Exercício Programa – Design de Software 2020.1 - “Craps Insper”



































































































nome = input("Digite seu nome caro padawan: ")
print ("{0},seja bem-vindo ao Quarentena's Vegas Licit (not so much) House!".format(nome))
print ("Nesse jogo você ganha ou perde! É simples!")
from random import randint 
fichas = 1000
#Fase Come Out 
while (fichas>0):  
    #Fase Come Out
    primeiro_dado = randint(1,6)
    segundo_dado = randint(1,6)
    soma = primeiro_dado+segundo_dado
    print ("{0},você está com {1} fichas!".format(nome,fichas))
    print ("Você está na fase Come Out! ")
    apostar_ou_sair = input("{0},você deseja apostar ou sair?: ".format(nome))
    if apostar_ou_sair == "sair":
        break 
    else: 
        tipo_aposta = input("Escolha o tipo da aposta, lembre-se que você pode apostar em mais de um tipo por vez . Tipos: Pass Line Bet (plb), Field (f), Any Craps (ac), Twelve(t): ")
        aposta = int(input("Quantas fichas você quer apostar: "))
        #Pass line bet
        if tipo_aposta=="plb":                        
            if soma == 7 or soma == 11:
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou! A soma foi igual a 7 ou 11!")
                print ("O jogo será reiniciado!")
                fichas = fichas + aposta
            elif soma == 2 or soma == 3 or soma == 12: 
                fichas = fichas - aposta 
                print ("A soma é {0} ".format(soma))
                print ("Você perdeu! A soma foi igual a 2,3 ou 12!")
                print ("O jogo será reiniciado!")
            else: 
                #Fase Point 
                print ("Você passou para a fase Point!")
                print ("Novos dados serão ressorteados!")
                point = primeiro_dado+segundo_dado
                novo_dado = randint(1,6)
                novo_dado_2 = randint(1,6)
                nova_soma = novo_dado+novo_dado_2
                a = 0 
                while a!=1:
                    novo_dado = randint(1,6)
                    novo_dado_2 = randint(1,6)
                    nova_soma = novo_dado+novo_dado_2
                    if point == nova_soma:
                        fichas = fichas + aposta
                        print ("O point é {0} ".format(point))
                        print ("A nova soma é {0} ".format(nova_soma))
                        print ("Você ganhou! A soma point foi igual ao dos novos dados!")
                        print ("O jogo será reiniciado!")
                        a=1
                    elif nova_soma == 7: 
                        fichas = fichas - aposta 
                        print ("A nova soma é {0} ".format(nova_soma))
                        print ("Você perdeu! A nova soma deu 7!")
                        print ("O jogo será reiniciado!")
                        a = 1
        #Field
        if tipo_aposta=="f": 
            if soma == 5 or soma == 6 or soma == 7 or soma == 8:
                fichas = fichas - aposta
                print ("A soma é {0} ".format(soma))
                print ("Você perdeu! A soma foi igual a 5,6,7 ou 8!")
                print ("O jogo será reiniciado!")
            elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                fichas = fichas + aposta
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou! A soma foi igual a 3,4,9,10 ou 11!")
                print ("O jogo será reiniciado!")
            elif soma == 2:
                fichas = fichas + 2*aposta
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou! A soma foi igual a 2! Que sortudo!")
                print ("O jogo será reiniciado!")
            else:
                fichas = fichas + 3*aposta
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou! A soma foi igual a 12! UAU!")
                print ("O jogo será reiniciado!")
        #Any Craps 
        if tipo_aposta=="ac":
            if soma == 2 or soma == 3 or soma == 12:
                fichas = fichas + aposta*7
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou! A soma foi igual a 2,3 ou 12! Ta com sorte! Joga mais muahahah!")
                print ("O jogo será reiniciado!")
            else: 
                fichas = fichas - aposta
                print ("A soma é {0} ".format(soma))
                print ("Você perdeu! Quem mandou você jogar mais em! Quem avisa amigo é!")
                print ("O jogo será reiniciado!")
        #Twelve
        if tipo_aposta=="t":
            if soma == 12:
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou! A soma foi igual a 12! Sorte de principiante {0}".format(nome))
                print ("O jogo será reiniciado!")
                fichas = fichas + fichas*30
            else:
                print ("A soma é {0} ".format(soma))
                print ("Mas que ganancioso {0}! Claro que perdeu! A soma não deu 12!".format(nome))
                print ("O jogo será reiniciado!")
                fichas = fichas - aposta 
