# Gerar de senha aleátoria

import random # Gerar númmeros
import string # Gerador de símbulo, letras e caracteres

# Listas de caracteres possíveis
caracteres = string.ascii_letters + string.punctuation + string.digits


def gerar_Senha(tamanho):

    senha = []
    for i in range(tamanho):
        senha.append(random.choice(caracteres)) # adiciona um caractere aleatório
    return ''.join(senha) # Transforma a lista em string


# Entrada do usuário 
print("\n ==== Gerador de senha aleátorio ====")
usuario_caracteres = int(input("Qauntos caracteres você quer na senha?  "))

if usuario_caracteres > 0:
    senha_gerada = gerar_Senha(usuario_caracteres)
    print("Sua senha aleatória é: ", senha_gerada)
else:
    print("Digite um número maior que 0.")