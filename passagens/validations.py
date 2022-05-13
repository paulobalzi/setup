from django.template import Origin


def origem_destino_iguais(origem, destino, lista_de_erros):
    """verifica se os campos origem e destino são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica a existẽncia de um dígito na string"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números nesse campo'

def data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros):
    """verifica se data de ida maior que data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta']

def data_ida_menor_data_de_hoje(data_ida, data_pesquisa, lista_de_erros):
    """verifica se a data de ida é menor que a data da pesquisa"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que a data de hoje'