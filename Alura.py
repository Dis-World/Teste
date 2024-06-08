import os

def Exercicios_aula_1():
    print('Python na Escola de Programação da Alura\n')

    Nome, Idade = input('Insira seu nome: ') , input('Idade: \n')

    print(f'Meu nome é {Nome} e tenho {Idade} anos\n')

    print('A')
    print('l')
    print('u')
    print('r')
    print('a\n')
    resposta_certa = print('A','L','U','R','A',sep='\n')

    pi = 3.14159

    print(f'O valor aproximado de PI é {pi}')

def Exercicios_aula_2():

    Lista_Usuarios = ['DisWorld','tiomight']
    Lista_Senhas = ['tiomight','tferrah']

    Par_ou_impar = int(input('Digite um número: '))

    if (Par_ou_impar%2) == 0:
        print('Este número é Par!\n')

    elif (Par_ou_impar%2) == 1:
        print('Este número é Impar!\n')


    Classificar_idade = int(input('Digite sua idade: '))

    if Classificar_idade < 0:
        print('Espermatozoide\n')
    elif Classificar_idade <= 12:
        print('Criança\n')   
    elif 13 <= Classificar_idade <= 19:
        print('Adolescente pae\n')      
    elif Classificar_idade >= 20:
        print('Adulto / idoso\n')
    
    while True:
        Login = input('Digite seu nome de usuario: ')
        
        if Login in Lista_Usuarios:
            pass

        else:
            print('Usuario não localizado\n')

        Senha = input('Digite sua senha')

def Exercicios_aula_3():

    # 1. Crie uma lista para cada informação a seguir:
    Numeros = [1,2,3,4,5,6,7,8,9,10]
    Nomes = ['Luiz','Henrique','Ligia',"Isabel"]
    Anos = [2006,2024]

    # 2. Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
    for i in Numeros:
        print(i)
    
    # 3. Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
    
    soma_impares = 0
    soma_pares = 0

    for i in (Numeros):
        if i%2 == 1:
            soma_impares += i
        else:
            soma_pares += i

    print('\nSoma dos numeros impares: ',soma_impares)
    print('Soma dos numeros pares: ',soma_pares,'\n')

    #4. Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

    x = len(Numeros)
    for i in Numeros:
        print(x)
        x -= 1

    # 5.Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

    while True:
        try:
            Seleção_usuario = float(input('\nEscolha um numero de 1 a 10: '))
            for i in Numeros:
                print(Seleção_usuario,' x ', i ,' = ',Seleção_usuario*i)
            break
        except:
            print('\nO numero que você digitou é invalido, se deseja adicionar virgulas use . em vez de ,')

def Testes():

    Nomes = [{'Nome': 'Luiz','Idade': '18','Sexo': 'Masculino','Sanidade Mental': '70%'},
             {'Nome': 'Henrique','Idade': '18','Sexo': 'Masculino','Sanidade Mental': '60%'},
             {'Nome': 'Ligia','Idade': '18','Sexo': '???','Sanidade Mental': '40%'},
             {'Nome': 'Isabel','Idade': '18','Sexo': 'Masculino','Sanidade Mental': '???'}]
    
    
    print('Nome | Idade | Sexo | Sanidade\n')
    
    for nome in Nomes:

        Nome_do_pessoal = nome['Nome']
        Idade_do_pessoal = nome['Idade']
        Sexo_do_pessoal = nome['Sexo']
        Sanidade_do_pessoal = nome['Sanidade Mental']
        
        
        print(Nome_do_pessoal,Idade_do_pessoal,Sexo_do_pessoal,Sanidade_do_pessoal,'\n')
        #print(nome['Nome'],nome['Idade'],nome['Sanidade Mental'])
        
def Python_orientado_a_Objeto_1():

    class Musica:
        
        nome = ''
        artista = ''
        duração = ''

    musica1 = Musica()

    musica1.nome = 'Dramaturgy'
    musica1.artista = 'Eve'
    musica1.duração = '4:30'

    print(f'Música: {musica1.nome} \n Artista: {musica1.artista} \n Duração: {musica1.duração} ' )


def main():
    os.system('cls')
    Python_orientado_a_Objeto_1()

if __name__ == '__main__':
    main()