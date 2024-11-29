lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Cript():
    palavra = input("Digite uma Palavra Para Ser Criptografada: ") 
    chave = int(input("Digite a chave de Criptografia: "))
    for i in palavra:   
        letra = lista.index(i)
        letra += chave
        if(letra > 25):
            letra -= 26
        criptografia = lista[letra]
        print(criptografia, end="")
    print("\n")

def Decript():
    palavra = input("Digite uma Palavra Para Ser Descriptografa: ") 
    chave = int(input("Digite a chave de Descriptografia: "))
    for i in palavra:   
        letra = lista.index(i)
        letra -= chave
        if(letra > 25):
            letra += 26
        descriptografa = lista[letra]
        print(descriptografa, end="")
    print("\n")

def Menu():
    print("\n------------------------------------")
    print("\nSelecione uma Opção: ")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("3 - Sair")
    print("\nOpção: ", end="")

def main():

    while(True):
        Menu()
        op = int(input())
        if op == 1:
            Cript()
            op = 0
        elif op == 2:
            Decript()
            op = 0
        elif op == 3:
            print("Saindo...")
            return False
        else:
            Menu()
            op = (input())
main()