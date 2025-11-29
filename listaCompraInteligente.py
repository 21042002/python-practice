# Lista de compra inteligente 

lista_compra = []

def adicionar_item(item):
    lista_compra.append(item)
    
    return lista_compra


def remover_item(item):
    lista_compra.remove(item)

    return lista_compra

def enumerar_itens():
    for i, item in enumerate(lista_compra, start=1):
        print(f"{i} - {item}")
    

while True: 
    print("\n=== Lista de compra ===")
    print("\n > MENU <")
    print("1 - Adiconar item a lista: ")
    print("2 - Mostra itens da lista.")
    print("3 - Quantidade de item na lista.")
    print("4 - Remover item da lista.")
    print("5 - Sair.")


    opcao = input("Escolha: ")

    if opcao == "1":
        print('Separe os itens por "," para adicionar mais item.')
        item = input("Digite o item: ")

        if "." in item:
            palavras = item.split(',')

            for p in palavras: 
                lista_compra.append(p.strip())
        else:
            lista_compra = adicionar_item(item)
            
    elif opcao == "2":
        if lista_compra:
            print("\nSegue os itens da lista de compra: ")
            enumerar_itens()
        else:
            print("Lista vazia! Por favor adiconar 1 item.")
    
    elif opcao == "3":
        print(f"\nQuantidade de itens da lista: {len(lista_compra)}")
    
    elif opcao == "4":
        item = input("Digite o item ou frase que deseja remover: ")

        lista_compra = remover_item(item)    
    elif opcao == "5":
        print("Saindo ...")
        break

    else: 
        print('Você não digitou algo válido! Por favor faça novamente.') 

        