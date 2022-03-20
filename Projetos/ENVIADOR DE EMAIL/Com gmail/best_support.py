"""
suporte ao arquivo best.py
"""
from datetime import datetime

def salutation():
    """
    Retorna saudação adequada ao período do dia
    Returns:
        str: saudação
    """
    current_hour = datetime.now().hour  
    if current_hour < 12:
        return 'Bom dia'
    elif current_hour < 18:
        return 'Boa tarde'
    else:
        return 'Boa noite'    


def adapt_gender(gender: str):
    """
    Args:
        gender (str): sexo da pessoa

    Returns:
        str: tratamento ao sexo
    """
    if gender == 'm':
        return 'o aluno'
    elif gender == 'f':
        return 'a aluna'
    else:
        return ''
    
    
def adapt_situation(situation: str):
    """
    Args:
        situation (str): abreviação da situação

    Returns:
        str: tratamento da situação
    """
    if situation == 'a':
        return 'aprovado'
    elif situation == 'r':
        return 'reprovado'
    else:
        return ''    
    
def adapt_result(result: str):
    """
    Args:
        result (str): nota do aluno

    Returns:
        str: mensagem para aluno
    """
    if float(result) >= 9:
        return 'Parabéns, ele é um aluno excepcional !!!'
    elif float(result) >= 7:
        return 'Parabéns pela aprovação'
    else:
        return 'Estude mais'
    

def check_dinamic_email_objects(quantity_of_shipments: int, *email_objects):
    """
    Valida objetos dinâmicos no envio dos emails
    Args:
        quantity_of_shipments (int): quantidade de informações na tabela

    Raises:
        ValueError: Se não for tupla nem lista
        IndexError: se tamanho não for o ideal
    """
    for email_object in email_objects:
        if not isinstance(email_object, (list, tuple)):
            raise ValueError(f'"{email_object}" não é lista nem tupla')
        if len(email_object) != quantity_of_shipments:
            raise IndexError(f'"{email_object}" tem tamanho inválido, o  tamanho correto é {quantity_of_shipments}')


