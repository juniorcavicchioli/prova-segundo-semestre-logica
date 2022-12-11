# ADILSON ROBERTO CAVICCHIOLI JUNIOR...RM: 9XXXX TURMA: XXXXX
# ALBERT OLIVEIRA RIBEIRO..............RM: 9XXXX
# MATHEUS GOMES DA SILVA...............RM: 9XXXX
# VINICIUS PRADO MENDES................RM: 9XXXX

from datetime import date, datetime # para validção da data

def busca_sequencial(lista, v):
    """
    Método simples de busca sem sentinela. Passa por cada elemento.
    Cada comparação elimina apenas um elemento do vetor.
    :param lista: lista a ser pesquisada
    :param v: valor a ser encontrado
    :return: índice na lista onde o valor está ou -1 caso não seja encontrado
    """
    flag = False
    i = 0
    while i < len(lista) and not flag:
        if lista[i]["mes_ano_referencia"] == v:
            flag = True
        else:
            i += 1
    if flag:
        return i
    else:
        return -1


def transformar_int(num):
    try:
        num = int(num)
        return num
    except ValueError:
        print("Por favor, insira um número inteiro.")


def validar_data(data):
    """
    Valida se a data está no formato pedido e se ela não é no futuro
    :param data: uma string
    :return: True ou False
    """
    try:
        data = datetime.strptime(data, '%m-%Y').date()
    except ValueError:
        print("Data inválida. Utilize o formato mês-ano. Ex.: 02-2022")
        return False
    data_atual = date.today()
    if data > data_atual:
        print("Insira uma data antes da atual.")
        return False
    return True


def estatistica(total_obitos, total_habitantes):
    """
    Calcula o número de óbitos a cada 100 mil habitantes
    :param total_obitos: int
    :param total_habitantes: int
    :return: float
    """
    return round(total_obitos/total_habitantes * 100000, 2)


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


def pesquisa_lista(array, item):
    """
    Procura e salva todos os items registrados do ano indicado
    :param array: list
    :param item: str | ano a ser pesquisado
    :return: uma lista cheia ou vazia seguida por um boolean
    """
    resultado = []
    status = False
    for i in range(len(array)):
        item_temp = array[i]['mes_ano_referencia']
        item_temp = item_temp.split('-')
        if item_temp[1] == item:
            resultado.append(i)
            status = True
    return resultado, status


def soma_valores(indices, array, key):
    """
    Soma os valores de acordo com os indices de onde estão os registros
    :param indices: uma lista com os indices dos elementos da outra lista
    :param array: array com os valores a serem somados
    :param key: chave do dicionario para acessar o valor a ser somado
    :return: int com a soma dos valores
    """
    soma = 0
    for i in range(len(indices)):
        soma += array[indices[i]][key]
    return soma


def regra_de_tres(valor1, valor2):
    return round(100*valor2/valor1 - 100, 1)


# dicionários e listas
registro = {"mes_ano_referencia": '',
            "total_habitantes": '',
            "total_obitos": ''}
tabela_registro = []

# programa principal
while True:
    menu_principal = input("==============-MENU PRINCIPAL-==============\n"
                           "1. Cadastrar mês referência\n"
                           "2. Exibir dados do mês de referência\n"
                           "3. Relatório comparativo | Referência 2019\n"
                           "4. Listar todos os meses cadastrados\n"
                           "0. Sair\n"
                           "-> ")
    if menu_principal == '1':
        print("==============-CADASTRO-==============\n"
              "Para cancelar, digite [.]")
        while True:
            data = input("Mês-ano....: ")
            if data == '.':
                break
            if validar_data(data):
                break
        if data != '.':
            total_habitantes = verificar_int("Total de habitantes.....: ")
            if total_habitantes != '.':
                total_obitos = verificar_int("Total de óbitos.........: ")
                if total_obitos != '.':
                    registro["mes_ano_referencia"] = data
                    registro["total_habitantes"] = total_habitantes
                    registro["total_obitos"] = total_obitos
                    tabela_registro.append(registro.copy())
                    print("***** Gravado com sucesso *****")
                else:
                    print("Cancelado")
            else:
                print("Cancelado")
        else:
            print("Cancelado")
    elif menu_principal == '2':
        print("==============-CONSULTA-==============")
        pesquisa = input("Digite o mês-ano desejado: ")
        i = busca_sequencial(tabela_registro, pesquisa)
        if i != -1:
            print(f"Mês-ano................: {tabela_registro[i]['mes_ano_referencia']}\n"
                  f"Total de habitantes....: {tabela_registro[i]['total_habitantes']}\n"
                  f"Total de óbitos........: {tabela_registro[i]['total_obitos']}")
        else:
            print("***** Mês-ano ainda não cadastrado! *****")
    elif menu_principal == '3':
        print("==============-COMPARAÇÃO-==============")
        pesquisa = input("Digite o ano a ser comparado: ")
        resultado = pesquisa_lista(tabela_registro, pesquisa)
        if resultado[1]:
            soma_habitantes = soma_valores(resultado[0], tabela_registro, 'total_habitantes')
            soma_obitos = soma_valores(resultado[0], tabela_registro, 'total_obitos')
            taxa_100_habitante = estatistica(soma_obitos, soma_habitantes)
            print(f"Total de habitantes: {soma_habitantes}\n"
                  f"Total de óbitos: {soma_obitos}\n"
                  f"Taxa por 100k habitantes - {pesquisa}: {taxa_100_habitante}\n"
                  f"Taxa por 100k habitantes - 2019: 15.00\n"
                  f"Comparativo percentual entre {pesquisa} e 2019: {regra_de_tres(15, taxa_100_habitante)}")
        else:
            print("***** Ano não cadastrado! *****")
    elif menu_principal == '4':
        for i in range(len(tabela_registro)):
            print(f"Mês-ano................: {tabela_registro[i]['mes_ano_referencia']}")
            print(f"Total de habitantes....: {tabela_registro[i]['total_habitantes']}")
            print(f"Total de óbitos........: {tabela_registro[i]['total_obitos']}")
            print('-'*35)
    elif menu_principal == '0':
        print("O macado está acenando! Tchau :)")
        break
    else:
        print("Digite uma opção válida.")
