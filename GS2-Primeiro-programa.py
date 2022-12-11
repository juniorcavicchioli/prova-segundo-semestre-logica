# ADILSON ROBERTO CAVICCHIOLI JUNIOR...RM: 9XXXX TURMA: XXXXX
# ALBERT OLIVEIRA RIBEIRO..............RM: 9XXXX
# MATHEUS GOMES DA SILVA...............RM: 9XXXX
# VINICIUS PRADO MENDES................RM: 9XXXX

# Nossa solução se resume a um aluguel de veículos pequenos podendo ou não serem elétricos. Nesse programa a pessoa pode apenas
# reservar.

"""
1. Registro !
2. Login !
3. Editar perfil !
4. Ver perfil !
5. Ver veículos !
5.1 Bicicleta !
5.2 Patins !
5.3 Patinete !
6. Alugar veículo !
6.1 Bicicleta !
6.2 Patins !
6.3 Patinete !
"""
from random import randint

def validar_email(email):
    """
    Valida se o formato de e-mail inserido é válido
    :param email: e-mail a ser analisado. Uma string
    :return: boolean
    """
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.'
    simbolos = '-_'
    email_separado = email.split('@')
    # mais de um ponto não é permitido | só é permitido um @ para separar o e-mail | não pode começar ou terminar com '.
    if '..' in email_separado[0] \
            or len(email_separado) > 2 or len(email_separado) < 2 \
            or email_separado[0][0] == '.' or email_separado[0][-1] == '.':
        return False
    # valida se o e-mail tem somente os caracteres de alfabeto
    for i in email_separado[0]:
        if i not in alfabeto and i not in simbolos:
            return False
    # verificação segunda metade
    for i in email_separado[1]:
        if i not in alfabeto:
            return False
    dominio_separado = email_separado[1].split('.')
    if len(dominio_separado) > 3:
        return False
    return True


def verificar_string(array, string, key):
    """
    Verifica se a string já está no array
    :param array: lista
    :param string: texto a ser verificado
    :param key: chave do dicionario
    :return: boolean
    """
    for i in array:
        if i[key] == string:
            return True
            break
    return False


def encontrar_conta(array, string, id):
    for i in range(len(array)):
        if array[i][id] == string:
            return i
            break
    return -1


def editar_perfil(id, key, novo_valor):
    """
    Faz a troca ou registro do novo dado da conta
    :param id: posição no array da conta
    :param key: dado a ser trocado
    :param novo_valor:
    """
    if key == 'email':
        string = 'e-mail'
    elif key == 'idade' or key == 'cpf' or key == 'nome':
        string = key
    while True:
        flag = input(f"{string.title()} atual: {cadastrados[id][key]}\n"
                     f"Novo {string}: {novo_valor}\n"
                     f"Deseja trocar o seu {string}?\n1. Sim\n2. Não\n-> ")
        if flag == '1':
            cadastrados[id][key] = novo_valor
            print(f"{string.title()} trocado com sucesso.")
            break
        elif flag == '2':
            break
        else:
            print("Digite uma opção válida.")


def transformar_int(num):
    try:
        num = int(num)
        return num
    except ValueError:
        print("Por favor, insira um número inteiro.")


def verificar_int(texto):
    """
    Repete até que o usuário digite um número inteiro
    :param texto: str a ser escrita na tela para o usuário
    :return: int
    """
    while True:
        num = input(texto)
        if num != '.':
            num = transformar_int(num)
            if type(num) == int:
                break
        else:
            break
    return num


def cpf_validate(numbers):
    """
    Verifica se o CPF é válido
    AUTOR: https://www.vivaolinux.com.br/script/Validador-e-gerador-de-CPF-em-Python#:~:text=Duas%20funções%20em%20Python%2C%20uma,que%20gera%20um%20CPF%20válido.&text=from%20random%20import%20randint%20def,dígitos%20if%20len(cpf)%20!%3D
    :param numbers: int
    :return: boolean
    """
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def identificar_veiculo(keys):
    if len(keys) == 3:
        return 'patins'
    elif len(keys) == 4:
        return "patinete"
    elif len(keys) == 5:
        return "bicicleta"


def exibir_veiculos(array):
    for i in range(len(array)):
        # identificar qual veículo é o array
        keys = array[i].keys()
        tipo = identificar_veiculo(keys)

        print(f"=-=----={tipo.upper()} {array[i]['id']}=----=-=\n"
              f"Cor: {array[i]['cor']}\n"
              f"Tamanho: {array[i]['tamanho']}")
        if 'marcha' in keys:
            if array[i]['marcha']:
                marcha = "sim"
            else:
                marcha = "não"
            print(f"Marcha: {marcha}")
        if 'eletrica' in keys:
            if array[i]['eletrica']:
                eletrica = 'sim'
            else:
                eletrica = 'não'
            print(f"Eletrica: {eletrica}")


def gerar_patins():
    patins = {}
    cores = ["branco", "preto", "amarelo", "rosa", "verde", "roxo"]
    tamanhos = ["infantil", "adulto"]
    i = randint(0, 5)
    patins["cor"] = cores[i]
    i = randint(0, 1)
    patins["tamanho"] = tamanhos[i]
    return patins


def gerar_patinete():
    patinete = gerar_patins()
    boolean = [False, True]
    i = randint(0, 1)
    patinete["eletrica"] = boolean[i]
    return patinete


def gerar_bicicleta():
    """
    Método criado para gerar pseudo-aleatoriamente alguns dados de bicicletas
    Não é uma funcionalidade do programa
    :return: dict
    """
    bicicleta = gerar_patinete()
    boolean = [False, True]
    i = randint(0,1)
    bicicleta["marcha"] = boolean[i]
    return bicicleta


def alugar_veiculo(dict, email, string):
    while True:
        alugar = input(f"Deseja alugar alguma {string}?\n1. Sim\n2. Não\n-> ")
        if alugar == '1':
            id_conta = encontrar_conta(cadastrados, email, "email")  # IMPORTANTE!
            num = verificar_int(f"Digite o número do {string} que deseja reservar: ")
            id = encontrar_conta(cadastrados, email, "email")  # IMPORTANTE!
            keys = dict[id].keys()
            tipo = identificar_veiculo(keys)
            if tipo == 'bicicleta':
                cadastrados[id_conta]["bic_alugadas"].append(num)
            elif tipo == 'patins':
                cadastrados[id_conta]["patins_alugadas"].append(num)
            elif tipo == 'patinete':
                cadastrados[id_conta]["patinete_alugadas"].append(num)
            print(f"{tipo.title()} {num} reservada.")
            break
        elif alugar == '2':
            break
        else:
            print("Digite uma opção válida")


# Cadastro de usuário
cadastrados = []
usuario = {"email": '',
           "senha": '',
           "nome": '',
           "cpf": '',
           "idade": '',
           "bic_alugadas": [],
           "patins_alugadas": [],
           "patinetes_alugadas": []}

# Veículos que nossa empresa "possui"
# Bicicletas
bicicleta = {"cor": '',
             "tamanho": '',
             "marcha": False,
             "eletrica": False,
             "id": ''}
lista_bicicleta = []
for i in range(10):
    bike = gerar_bicicleta()
    bike['id']= i
    lista_bicicleta.append(bike.copy())

# Patins
patins = {"cor": '',
          "tamanho": '',
          "id": ''}
lista_patins = []
for i in range(10):
    temp_patins = gerar_patins()
    temp_patins['id']= i
    lista_patins.append(temp_patins.copy())

# Patinete
patinete = {"cor": '',
            "tamanho": '',
            "eletrica": False,
            "id": ''}
lista_patinete = []
for i in range(10):
    temp_patinete = gerar_patinete()
    temp_patinete['id'] = i
    lista_patinete.append(temp_patinete.copy())


# Programa principal
while True:
    menu_principal = input("==============-MENU-==============\n"
                           "1. Registrar\n"
                           "2. Login\n"
                           "0. Sair\n"
                           "-> ")
    if menu_principal == '1':
        email = input("Digite um e-mail: ")
        if verificar_string(cadastrados, email, "email"):
            print("E-mail já cadastrado.")
        elif not validar_email(email):
            print("Por favor, digite um e-mail válido")
        else:
            senha = input("Insira uma senha: ").strip()
            usuario['email'] = email
            usuario['senha'] = senha
            cadastrados.append(usuario.copy())
            print("Conta criada!\n"
                  f"E-mail: {email}\n"
                  f"Senha: {senha}")
    elif menu_principal == '2':
        email = input("Digite seu e-mail: ")
        if verificar_string(cadastrados, email, "email"):
            senha = input("Digite sua senha: ")
            if verificar_string(cadastrados, senha, "senha"):
                print("Login efetuado!")
                while True:
                    menu_logado = input("==============-MENU PRINCIPAL-==============\n"
                                        "1. Ver perfil\n"
                                        "2. Editar perfil\n"
                                        "3. Ver bicicletas\n"
                                        "4. Ver patins\n"
                                        "5. Ver patinete\n"
                                        "0. Voltar\n"
                                        "-> ")
                    if menu_logado == '1':
                        id = encontrar_conta(cadastrados, email, "email") # IMPORTANTE!
                        if id != -1:
                            print(f"E-mail: {cadastrados[id]['email']}")
                            if cadastrados[id]['nome'] != '':
                                print(f"Nome: {cadastrados[id]['nome']}")
                            else: print("Nome ainda não preenchido.")
                            if cadastrados[id]['cpf'] != '':
                                print(f"CPF: {cadastrados[id]['cpf']}")
                            else: print("CPF ainda não preenchido.")
                            if cadastrados[id]['idade'] != '':
                                print(f"Idade: {cadastrados[id]['idade']}")
                            else: print("Idade ainda não preenchida.")
                    elif menu_logado == '2':
                        id = encontrar_conta(cadastrados, email, "email") # IMPORTANTE!
                        while True:
                            menu_editar_perfil = input("==============-EDITAR PERFIL-==============\n"
                                                       "1. E-mail\n"
                                                       "2. Nome\n"
                                                       "3. Idade\n"
                                                       "4. CPF\n"
                                                       "0. Voltar\n"
                                                       "-> ")
                            if menu_editar_perfil == '1':
                                email = input("Digite o novo e-mail: ")
                                if not validar_email(email):
                                    print("Digite um e-mail válido.")
                                else:
                                    editar_perfil(id, 'email', email)
                            elif menu_editar_perfil == '2':
                                nome = input("Digite o novo nome: ")
                                editar_perfil(id, 'nome', nome)
                            elif menu_editar_perfil == '3':
                                idade = verificar_int("Digite a nova idade: ")
                                editar_perfil(id, 'idade', idade)
                            elif menu_editar_perfil == '4':
                                cpf = input("Digite o novo CPF: ")
                                if cpf_validate(cpf):
                                    editar_perfil(id, 'cpf', cpf)
                                else: print("CPF inválido.")
                            elif menu_editar_perfil == '0': break
                            else: print("digite uma opção válida.")
                    elif menu_logado == '3':
                        exibir_veiculos(lista_bicicleta)
                        print("-"*30)
                        alugar_veiculo(lista_bicicleta, email, "bicicleta")
                    elif menu_logado == '4':
                        exibir_veiculos(lista_patins)
                        print("-" * 30)
                        alugar_veiculo(lista_patins, email, 'patins')
                    elif menu_logado == '5':
                        exibir_veiculos(lista_patinete)
                        print("-" * 30)
                        alugar_veiculo(lista_patinete, email, 'patinete')
                    elif menu_logado == '0': break
                    else: print("digite uma opção válida")
            else: print("Senha incorreta")
        else:
            print("E-mail não cadastrado.")
    elif menu_principal == '0':
        print("O macado está acenando! Tchau :)")
        break
    else:
        print("Escolha uma opção válida.")
