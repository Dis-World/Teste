import os

def menu():
    print('Escolha um desses 4 items:\n')

    print('1. Wind Sword')
    print('2. Dragon Slayer')
    print('3. Manto de vento')
    print('4. Adaga de fogo\n')

def Escolher_opção():
    info = int(input("Insira um numero para ver as informações do item: "))

    if info == 1: # Wind Sword

        print("""
        ░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░  ░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
        ░██║░░██╗░░██║██║████╗░██║██╔══██╗  ██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
        ░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║  ╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
        ░░████╔═████║░██║██║╚████║██║░░██║  ░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
        ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝  ██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
        ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░\n""")
        
        print('The Sylph Sword is able to strike at a far greater distance than the length of its "blade", essentially allowing its user, should they be compatible with the Sylphs in the sword, to launch razor air currents and cut apart enemies from a distance. In the hands of a skilled fencer it can strike precisely enough to cut a candle without blowing off its fire.\n')

        Escolha = input('\nDeseja escolher esse item? y/n: ')
       
        os.system('cls')

        if Escolha == "y":
            print("Você fez sua decisão... até a proxima, Serpico!")
           

    elif info == 2: # Dragon Slayer
        print(""" 
        ██████╗░██████╗░░█████╗░░██████╗░░█████╗░███╗░░██╗  ░██████╗██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░
        ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░██║  ██╔════╝██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
        ██║░░██║██████╔╝███████║██║░░██╗░██║░░██║██╔██╗██║  ╚█████╗░██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝
        ██║░░██║██╔══██╗██╔══██║██║░░╚██╗██║░░██║██║╚████║  ░╚═══██╗██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗
        ██████╔╝██║░░██║██║░░██║╚██████╔╝╚█████╔╝██║░╚███║  ██████╔╝███████╗██║░░██║░░░██║░░░███████╗██║░░██║
        ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚══╝  ╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")

        print("Given the sword's incredible size and weight, the Dragon Slayer functions more like a bladed maul than an actual sword, though Guts is more than capable of using it to cut through various targets. The sheer momentum of Guts swinging it can tear anyone caught in the attack impact into pieces with one swing; this often is applied to more than one enemy at once, cleaving through multiple foes in a single swing. Even apostles in their true forms can barely stand up to the sword, and often have their bones and internal organs heavily damaged by an attack from the weapon. This size and weight also grants the Dragon Slayer some versatility, as Guts has used the broad side of the weapon to squash and flatten several opponents. The Dragon Slayer's width also allows Guts to use it defensively, in lieu of a shield.\n")

        Escolha = input('Deseja escolher esse item? y/n: ' )

        os.system('cls')

        if Escolha == "y":
            print("Você fez sua decisão... até a proxima, Guts!")
 
        
    elif info == 3: # Manto de Vento
        pass

    elif info == 4:
        pass

    

def main():
    menu()
    Escolher_opção()

if __name__ == '__main__':
    main()       