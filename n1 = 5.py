import os
import time

os.system('cls')


def Calculadora_Temperatura():

    os.system('cls') # Faz apagar o texto do Terminal

    while True: # Loop
        
        # Menu 
        os.system('cls')

        print(' Ｃｅｌｓｉｕｓ ｅ Ｆａｈｒｅｎｈｅｉｔ\n')

        print('1. Celsius'), print('2. Fahreint'), print('0. Sair\n')
     
            
        Celsius_ou_f = int(input('Quer calcular o que?:  '))
        print('\n') # Serve só pra adicionar uma linha a mais de espaço

        if Celsius_ou_f == 1: # Celsius
            graus = int(input('Quantos graus celsius?: '))   
            print(graus,'celsius =', graus * (9/5) + 32, 'fahrenheit\n')

            sair = input('Deseja refazer o calculo? y/n: ')
            if sair == 'y':
                pass
            else:
                break

        elif Celsius_ou_f == 2: # fahrenheit 
            graus = int(input('Quantos fahrenheit? '))
            print(graus,'Graus fahrenheit =', (graus - 32) * 5/9, 'Graus Celsius\n')

            sair = input('Deseja refazer o calculo? y/n: ')
            if sair == 'y':
                pass
            else:
                break

        elif Celsius_ou_f == 0: # Sair
            print('Saindo...')
            time.sleep(1)
            break

        else:
            print('ta querendo calcular o que home???\n')

def Escolher_Produto():

    os.system('cls')

    while True:

        # Menu
        print('Escolha um desses 4 items:\n')

        print('1. Wind Sword')
        print('2. Dragon Slayer')
        print('3. Manto de vento')
        print('4. Adaga de fogo')

        print('0. Sair\n')

        info = int(input("Insira um numero para ver as informações do item: "))
        
        if info == 1: # Wind Sword

            print("""
            ░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░  ░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
            ░██║░░██╗░░██║██║████╗░██║██╔══██╗  ██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
            ░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║  ╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
            ░░████╔═████║░██║██║╚████║██║░░██║  ░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
            ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝  ██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
            ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░\n""")
            
            print('A Espada de vento é capaz de atacar a uma distância muito maior do que o comprimento de sua "lâmina", essencialmente permitindo que seu usuário, caso sejam compatíveis com os Silfos na espada, lance correntes de ar de navalha e corte inimigos à distância. Nas mãos de um esgrimista habilidoso, ele pode atacar com precisão o suficiente para cortar uma vela sem apagar seu fogo.\n')
            
            print('quantidade: 1'), print('Valor: Gratis\n')

            
            Escolha = input('\nDeseja escolher esse item? y/n: ')
            
            os.system('cls')

            if Escolha == "y":
                print("Você fez sua decisão... até a proxima, Serpico!\n")
                time.sleep(1)
                break

        elif info == 2: # Dragon Slayer
            print(""" 
            ██████╗░██████╗░░█████╗░░██████╗░░█████╗░███╗░░██╗  ░██████╗██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░
            ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░██║  ██╔════╝██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
            ██║░░██║██████╔╝███████║██║░░██╗░██║░░██║██╔██╗██║  ╚█████╗░██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝
            ██║░░██║██╔══██╗██╔══██║██║░░╚██╗██║░░██║██║╚████║  ░╚═══██╗██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗
            ██████╔╝██║░░██║██║░░██║╚██████╔╝╚█████╔╝██║░╚███║  ██████╔╝███████╗██║░░██║░░░██║░░░███████╗██║░░██║
            ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")

            print("Dado o incrível tamanho e peso da espada, o Dragon Slayer funciona mais como uma lâmina maul do que uma espada real, embora Guts seja mais do que capaz de usá-la para cortar vários alvos. O ímpeto puro de Guts balançando-o pode rasgar qualquer um pego no impacto de ataque em pedaços com um balanço; Isso geralmente é aplicado a mais de um inimigo ao mesmo tempo, cortando vários inimigos em um único balanço. Mesmo os apóstolos em suas verdadeiras formas mal conseguem resistir à espada, e muitas vezes têm seus seus ossos e órgãos internos fortemente danificados por um ataque da arma. Esse tamanho e peso também concede ao Dragon Slayer alguma versatilidade, já que Guts usou o lado largo da arma para esmagar e achatar vários oponentes. A largura do Dragon Slayer também permite que Guts o use defensivamente, em vez de um escudo.\n")

            print('quantidade: 1'), print('Valor: Gratis\n')

            Escolha = input('Deseja escolher esse item? y/n: ' )

            os.system('cls')

            if Escolha == "y":
                print("Você fez sua decisão... até a proxima, Guts!\n")
                time.sleep(1)
                break

        elif info == 0: # Sair
            print('Saindo...')
            time.sleep(1)
            break
        
def Area_do_triangulo():
   while True: 
        Base = int(input('Insira a base (b) do △ : ' ))
        Altura = int(input('Insira a Altura (h) do △ : '))

        print('\nA Area do Triangulo é: ', (Base*Altura)/2, '\n')

        sair = input('Deseja sair? (y/n): ')
        
        if sair == 'y':
            print('Saindo...')
            time.sleep(1)
            break
        else:
            os.system('cls')

def Media_das_notas():

    os.system('cls')

    while True:
        print('Ｍｅｄｉａ ｄａｓ Ｎｏｔａｓ\n')

        primeiro_trimestre = float(input('Nota do primeiro Trimestre: '))
        segundo_trimestre = float(input('Nota do segundo Trimestre: '))
        terceiro_trimestre = float(input('Nota do terceiro Trimestre: '))

        media = (primeiro_trimestre*2 + segundo_trimestre*3 + terceiro_trimestre*5)/10
        print('\nSua média é ',media)

        if media < 6:
            print('bah\n')

        elif 6 <= media < 8:
            print('passou ta bom\n')

        elif 8 <= media <= 10:
            print('Caraio Jimmy Neutron\n')

        else:
            print('Deu pro professor foi????\n') 

        

        refazer = input('Deseja refazer o calculo? y/n: ')
        print('\n')

        if refazer == 'y':
            os.system('cls')
            pass
        else:
            break

 
def main():

    while True:
        os.system('cls')

        print("""
        ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
        ████╗░████║██╔════╝████╗░██║██║░░░██║
        ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
        ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
        ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
        ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░""",'\n')

        print('1. Calcular Celsius e Fahreint')
        print('2. Escolher um Produto')
        print('3. Area do Triangulo')
        print('4. Media das Notas')
        print('0. Sair\n')


        escolha = int(input('Digite sua escolha: '))


        if escolha == 1: # Calculadora C e F
            Calculadora_Temperatura()
        if escolha == 2: # Escolher Produtos
            Escolher_Produto()
        if escolha == 3: # Area do Triangulo
            Area_do_triangulo()
        if escolha == 4: # Media das notas
            Media_das_notas()
        if escolha == 0: # Sair
            break

        
if __name__ == '__main__':
    main()
