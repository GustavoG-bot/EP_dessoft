#Exercício Programa – Design de Software 2020.1 - “Craps Insper”

#Filippo

from random import randint 
fichas = 1000
#Fase Come Out
while fichas>0:
    print ("Você está na fase Come Out")
    primeiro_dado=randint(1,6)
    segundo_dado=randint(1,6)
    soma_dados=primeiro_dado + segundo_dado 
    print("Você está com {0} fichas.".format(fichas))
    apostar_ou_sair=input("Você deseja apostar ou sair (apostar/sair)?")
    if apostar_ou_sair=="sair":
        break
    else:
        tipo_aposta=input("Escolha seu tipo de aposta. Lembre-se que você pode apostar em mais de um tipo por vez. Digite apenas as siglas dos tipos e se escolher mais de um, colocar na ordem apresentada e no formato(x_y_z). Tipos: Pass Line Bet(plb), Field(f), Any Craps(ac) e Twelve(t)")
        aposta=int(input("Quantas fichas você deseja apostar?"))
        if tipo_aposta=="plb":
            if soma_dados== 7 or soma_dados == 11:
                fichas=fichas+aposta 
                print("Você ganhou!")
            elif soma_dados== 2 or soma_dados== 3 or soma_dados==12:
                fichas=fichas-aposta
            else:
                #Fase Point
                print("Você passou para a fase Point!")
                point=primeiro_dado + segundo_dado
                terceiro_dado=randint(1,6)
                quarto_dado=randint(1,6)
                nova_soma=terceiro_dado+quarto_dado
                if point==nova_soma:
                    fichas=fichas+aposta
                    print("Você ganhou!")
                elif nova_soma==7:
                    fichas=fichas-aposta
                    print("Você perdeu!")
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
                            fichas=fichas+aposta
                            print("Você ganhou!")
                            a=1
                        elif nova_soma==7:
                            fichas=fichas-aposta
                            print("Voê perdeu!")
                            a=1
                        else:
                            a!=1






















































#Gustavo
from random import randint 
fichas = 1000
#Fase Come Out 
while (fichas>0):  
    #Fase Come Out
    primeiro_dado = randint(1,6)
    segundo_dado = randint(1,6)
    soma = primeiro_dado+segundo_dado
    print ("Você está com {0}".format(fichas))
    print ("Você está na fase Come Out! ")
    apostar_ou_sair = input("Você quer deseja apostar ou sair (apostar/sair)?: ")
    if apostar_ou_sair == "sair":
        break 
    else: 
        tipo_aposta = input("Escolha o tipo da aposta, lembre-se que você pode apostar em mais de um tipo por vez . Tipos: Pass Line Bet (plb), Field (f), Any Craps (ac), Twelve(t): ")
        aposta = int(input("Quantas fichas você quer apostar: "))
        #Pass line bet
        if tipo_aposta=="plb":                        
            if soma == 7 or soma == 11:
                print ("Você ganhou!")
                fichas = fichas + aposta
            elif soma == 2 or soma == 3 or soma == 12: 
                fichas = fichas - aposta 
                print ("Você perdeu!")
            else: 
                #Fase Point 
                print ("Você passou para a fase Point!") 
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
                        print ("Você ganhou!")
                        a=1
                    elif nova_soma == 7: 
                        fichas = fichas - aposta 
                        print ("Você perdeu!")
                        a = 1
        #field
        if tipo_aposta=="f": 
            if soma == 5 or soma == 6 or soma == 7 or soma == 8:
                fichas = fichas - aposta
                print ("Você perdeu!")
            elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
                fichas = fichas + aposta
                print ("Você ganhou!")
            elif soma == 2:
                fichas = fichas + 2*aposta
                print ("Você ganhou!")
            else:
                fichas = fichas + 3*aposta
                print ("Você ganhou!")
        #Any Craps 
        if tipo_aposta=="ac":
            if soma == 2 or soma == 3 or soma == 12:
                fichas = fichas + aposta*7
                print ("Você ganhou!")
            else: 
                fichas = fichas - aposta 
                print ("Você perdeu!")
        #Twelve
        if tipo_aposta=="t":
            if soma == 12:
                fichas = fichas + fichas*30
            else:
                fichas = fichas - aposta
