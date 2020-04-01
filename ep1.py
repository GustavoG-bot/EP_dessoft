
#Exercício Programa – Design de Software 2020.1 - “Craps Insper” - Gustavo Guedes e Filippo Ferraro.
#Professor, eu e o Filippo fizemos separadamente dois códigos para aprendermos como funciona o jogo e os comandos
#Assim, verifique os vários commits que realizamos para provar que não foi somente um aluno que realizou todo o código
#Para fins de avaliação considere o código que começa na linha 101. O código abaixo é fruto de um mero esforço dos
#alunos para sedimentar a matéria. Obrigado pela compreensão!

#Código 1

from random import randint 
fichas = 1000
continuar=0
nome=input("Qual seu nome?")
print("Bem vindo ao Craps Insper!".format(nome))
while fichas>0:
    #Fase Come Out
    primeiro_dado=randint(1,6)
    segundo_dado=randint(1,6)
    soma_dados=primeiro_dado + segundo_dado 
    print("Você está com {0} fichas.".format(fichas))
    apostar_ou_sair=input("Você deseja apostar ou sair (apostar/sair)?")
    if apostar_ou_sair=="sair":
        break
    else:
        print ("Você está na fase Come Out.")
        while not continuar:
            tipo_aposta=input("Escolha seu tipo de aposta: Pass Line Bet(plb), Field(f), Any Craps(ac) ou Twelve(t). Ou jogar os dados (jogar).")
            if tipo_aposta=="plb":
                aposta_plb=int(input("Quantas fichas você deseja apostar?"))
            if tipo_aposta=="f":
                aposta_f=int(input("Quantas fichas você deseja apostar?"))
            if tipo_aposta=="ac":
                aposta_ac=int(input("Quantas fichas você deseja apostar?"))
            if tipo_aposta=="t":
                aposta_t=int(input("Quantas fichas você deseja apostar?"))
            if tipo_aposta=="jogar":
                continuar=True
        #Pass line bet:
        if aposta_plb>0:
            if soma_dados== 7 or soma_dados == 11:
                fichas=fichas+aposta_plb
                print("A soma dos dados foi {0}.".format(soma_dados))
                print("Parabéns {0}, você ganhou o Pass Line Bet! Continue jogando.".format(nome))
            elif soma_dados== 2 or soma_dados== 3 or soma_dados==12:
                fichas=fichas-aposta_plb
                print("A soma dos dados foi {0}.".format(soma_dados))
                print("Que pena {0}, você perdeu o Pass Line Bet! Tente novamente".format(nome))
            else:
                #Fase Point
                print("Você passou para a fase Point! Novos dados serão sorteados.")
                point=primeiro_dado + segundo_dado
                terceiro_dado=randint(1,6)
                quarto_dado=randint(1,6)
                nova_soma=terceiro_dado+quarto_dado
                print("O point é {0}.".format(point))
                if point==nova_soma:
                    fichas=fichas+aposta_plb
                    print("A soma dos dados novos foi igual ao point.")
                    print("Parabéns {0}, você ganhou o Pass Line Bet na fase Point! Continue jogando.".format(nome))
                elif nova_soma==7:
                    fichas=fichas-aposta_plb
                    print("A soma dos dados novos foi {0}.".format(nova_soma))
                    print("Que pena {0}, você perdeu o Pass Line Bet na fase Point! Tente novamente".format(nome))
                else:
                    quinto_dado=randint(1,6)
                    sexto_dado=randint(1,6)
                    outra_soma=quinto_dado+sexto_dado
                    a=0
                    while a!=1:
                        quinto_dado=randint(1,6)
                        sexto_dado=randint(1,6)
                        outra_soma=quinto_dado+sexto_dado
                        a=0
                        if outra_soma==point:
                            fichas=fichas+aposta_plb
                            print("A soma dos dados novos foi igual ao point.")
                            print("Parabéns {0}, você ganhou o Pass Line Bet na fase Point! Continue jogando.".format(nome))
                            a=1
                        elif nova_soma==7:
                            fichas=fichas-aposta_plb
                            print("A soma dos dados novos foi {0}.".format(outra_soma))
                            print("Que pena {0}, você perdeu o Pass Line Bet na fase Point! Tente novamente".format(nome))
                            a=1
                        else:
                            a!=1
        #Field:
        if aposta_f>0:
            if soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8:
                fichas=fichas-aposta_f
                print("A soma dos dados foi {0}.".format(soma_dados))
                print("Que pena {0}, você perdeu o Field! Tente novamente".format(nome))
            elif soma_dados==3 or soma_dados==4 or soma_dados==9 or soma_dados==10 or soma_dados==11:
                fichas=fichas+aposta_f
                print("A soma dos dados foi {0}.".format(soma_dados))
                print("Parabéns {0}, você ganhou o Field! Continue jogando.".format(nome))
            elif soma_dados==2:
                fichas=fichas+aposta_f*2
                print("A soma dos dados foi {0}.".format(soma_dados))
                print("Parabéns {0}, você ganhou o Field! Continue jogando.".format(nome))
            elif soma_dados==12:
                fichas=fichas+aposta_f*3
                print("A soma dos dados foi {0}.".format(soma_dados))
                print("Parabéns {0}, você ganhou o Field! Continue jogando.".format(nome))
        #Any Craps:
        if aposta_ac>0:
            if soma_dados==2 or soma_dados==3 or soma_dados==12:
                fichas=fichas+aposta_ac*7
                print("A soma dos dados foi {0}}.".format(soma_dados))
                print("Parabéns {0}, você ganhou o Any Craps! Continue jogando.".format(nome))
            else:
                fichas=fichas-aposta_ac
                print("A soma dos dados foi {0}.".format(soma_dados))
                print("Que pena {0}, você perdeu Any Craps! Tente novamente".format(nome))
        #Twelve:
        if aposta_t>0:
            if soma_dados==12:
                fichas=fichas+aposta_t*12
                fichas=fichas+aposta_t*30
                print("A soma dos dados foi {0}.".format(soma_dados))
                print("Parabéns {0}, você ganhou o Twelve! Continue jogando.".format(nome))
            else:
                fichas=fichas-aposta_t
                print("Que pena {0}, você perdeu o Twelve! Tente novamente".format(nome))



















#Código 2 Gustavo e Fillipo OFICIAL - Craps INSPER
nome = input("Digite seu nome caro padawan: ")
print ("{0}, seja bem-vindo ao Quarentena's Vegas Licit (not so much) House!".format(nome))
print ("Nesse jogo você ganha ou perde! É simples!")
from random import randint 
fichas = 1000
#Fase Come Out 
while (fichas>0):  
    #Fase Come Out
    primeiro_dado = randint(1,6)
    segundo_dado = randint(1,6)
    soma = primeiro_dado+segundo_dado
    print ("{0}, você está com {1} fichas!".format(nome,fichas))
    print ("Você está na fase Come Out! ")
    apostar_ou_sair = input("{0}, você deseja apostar ou sair?: ".format(nome))
    if apostar_ou_sair == "sair":
        break 
    else:
        while apostar_ou_sair == "apostar":
            tipo_aposta = input("Por favor, digite o nome de todas as apostas separadamente (plb,ac,tw,f) e depois digite o valor da aposta. Quando terminar digite jogar dados: ")
            print ("Atenção: Todos os tipos devem receber valores! Caso não queria apostar no tipo aposte 0 fichas")
            if tipo_aposta == "plb":
                passline = int(input("Quantas fichas você quer apostar no Pass Line Bet: ")) 
            if tipo_aposta == "ac":
                anycraps = int(input("Quantas fichas você quer apostar no AnyCraps: "))
            if tipo_aposta == "tw":
                twelve = int(input("Quantas fichas você quer apostar no Twelve: "))
            if tipo_aposta == "f":
                fields = int(input("Quantas fichas você quer apostar no Fields: "))
            elif tipo_aposta == "jogar dados":
                break
        #Pass line bet
        if passline > 0:                       
            if soma == 7 and passline>0 or soma == 11:
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou no Pass Line Bet! A soma foi igual a 7 ou 11!")
                print ("O jogo será reiniciado!")
                fichas = fichas + passline
            elif soma == 2 or soma == 3 or soma == 12: 
                fichas = fichas - passline 
                print ("A soma é {0} ".format(soma))
                print ("Você perdeu no Pass Line Bet! A soma foi igual a 2,3 ou 12!")
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
                        fichas = fichas + passline
                        print ("O point é {0} ".format(point))
                        print ("A nova soma é {0} ".format(nova_soma))
                        print ("Você ganhou no Pass Line Bet! A soma point foi igual ao dos novos dados!")
                        print ("O jogo será reiniciado!")
                        a=1
                    elif nova_soma == 7: 
                        fichas = fichas - passline 
                        print ("A nova soma é {0} ".format(nova_soma))
                        print ("Você perdeu no Pass Line Bet! A nova soma deu 7!")
                        print ("O jogo será reiniciado!")
                        a = 1
    #Field
        if fields > 0:
            if soma == 5 and fields >0 or soma == 6 and fields >0 or soma == 7 and fields >0 or soma == 8 and fields >0:
                fichas = fichas - fields
                print ("A soma é {0} ".format(soma))
                print ("Você perdeu no Fields! A soma foi igual a 5,6,7 ou 8!")
                print ("O jogo será reiniciado!")
            elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                fichas = fichas + fields
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou no Fields! A soma foi igual a 3,4,9,10 ou 11!")
                print ("O jogo será reiniciado!")
            elif soma == 2:
                fichas = fichas + 2*fields
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou no Fields! A soma foi igual a 2! Que sortudo!")
                print ("O jogo será reiniciado!")
            else:
                fichas = fichas + 3*fields
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou no Fields! A soma foi igual a 12! UAU!")
                print ("O jogo será reiniciado!")
    #Any Craps 
    if anycraps > 0:
            if soma == 2 or soma == 3 or soma == 12:
                fichas = fichas + anycraps*7
                print ("A soma é {0} ".format(soma))
                print ("Você ganhou no AnyCraps! A soma foi igual a 2,3 ou 12! Ta com sorte! Joga mais muahahah!")
                print ("O jogo será reiniciado!")
            else: 
                fichas = fichas - anycraps
                print ("A soma é {0} ".format(soma))
                print ("Você perdeu no AnyCraps! Quem mandou você jogar mais em! Quem avisa amigo é!")
                print ("O jogo será reiniciado!")
    #Twelve
    if twelve > 0:
        if soma == 12:
            print ("A soma é {0} ".format(soma))
            print ("Você ganhou Twelve! A soma foi igual a 12! Sorte de principiante {0}".format(nome))
            print ("O jogo será reiniciado!")
            fichas = fichas + twelve*30
        else:
            print ("A soma é {0} ".format(soma))
            print ("Mas que ganancioso {0}! Claro que perdeu no Twelve! A soma não deu 12!".format(nome))
            print ("O jogo será reiniciado!")
            fichas = fichas - twelve
if fichas == 0:
    print ("Que pena {0}! Você torrou suas fichas! O jogo acabou!".format(nome)) 