# Começando o projeto 

















































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
        tipo_aposta = input("Escolha o tipo da aposta, lembre-se que você pode apostar em mais de um tipo por vez . Digite apenas as siglas dos tipos e se for mais de um colocar na ordem apresentada e no formato (x_y_z_w). Tipos: Pass Line Bet (plb), Field (f), Any Craps (ac), Twelve(t): ")
        aposta = int(input("Quantas fichas você quer apostar: ")  
        if tipo_aposta=="plb":                       #Jogador escolhe plb.
            if soma = 7 or soma = 11:
                print ("Você ganhou!")
                fichas = fichas + aposta
            elif soma = 2 or soma = 3 or soma = 12: 
                fichas = fichas - aposta 
            else: 
                #Fase Point 
                print ("Você passou para a fase Point!") 
                point = primeiro_dado+segundo_dado
                nova_soma = novo_dado+novo_dado_2
                while  (point!=nova_soma and nova_soma != 7): 
                    novo_dado = randint(1,6)
                    novo_dado_2 = randint(1,6)
                    if point == nova_soma:
                        fichas = fichas + aposta
                        break
                    if nova_soma = 7: 
                        fichas = fichas - aposta 
                        break

            #field
            if tipo_aposta=="f": 
                if soma = 5 or soma = 6 or soma = 7 or soma = 8:
                    fichas = fichas - aposta
                elif soma = 3 or soma = 4 or soma = 9 or soma = 10 or soma = 11:
                    fichas = fichas + aposta
                elif soma = 2:
                    fichas = fichas + 2*aposta
                else:
                    fichas = fichas + 3*aposta
            #Any Craps 
            if tipo_aposta=="ac":
                if soma = 2 or soma = 3 or soma = 12:
                    fichas = fichas + aposta*7
                else: 
                    fichas = fichas - aposta 
            #Twelve
            if tipo_aposta=="t":
                if soma = 12:
                    fichas = fichas + fichas*30
                else:
                    fichas = fichas - aposta 








if tipo_aposta=="plb":




if tipo_aposta=="plb":
                    
                
                





if (fichas == 0):
    print ("Você perdeu todas suas fichas!")
    break 