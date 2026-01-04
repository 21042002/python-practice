# Lista de Compras Inteligente

Este é um projeto simples em Python para gerenciar uma lista de compras via linha de comando, permitindo adicionar, remover, listar e contar itens de forma interativa.

## Descrição

O script `listaCompraInteligente.py` oferece um menu para o usuário interagir com a lista de compras. Funcionalidades incluem:
- Adicionar itens (suporta múltiplos itens separados por vírgula).
- Listar todos os itens enumerados.
- Mostrar a quantidade de itens.
- Remover itens específicos.
- Sair do programa.

## Requisitos

- Python 3.x instalado no sistema

## Como executar

1. Certifique-se de que o Python está instalado.
2. Execute o script no terminal:

   ```bash
   python listaCompraInteligente.py
   ```

3. Use o menu para escolher as opções desejadas.

## Exemplo de uso

```
=== Lista de compra ===

 > MENU <
1 - Adiconar item a lista:
2 - Mostra itens da lista.
3 - Quantidade de item na lista.
4 - Remover item da lista.
5 - Sair.
Escolha: 1
Separe os itens por "," para adicionar mais item.
Digite o item: maçã, banana, leite

Escolha: 2

Segue os itens da lista de compra:
1 - maçã
2 - banana
3 - leite
```

## Observações

- Os itens são armazenados em memória durante a execução; não há persistência em arquivo.
- Este é um projeto básico para prática de loops e listas em Python.

## Licença

Este projeto é de uso pessoal e educacional.