"""
Descrição:
    Arquivo python para suporte ao main.py e best.py
"""
def regulate(iterable):
    """
    Filtrar variáveis para a função send da biblioteca yagmail
    Args:
        iterable ([str, list]): Um iterable de algum campo do email
    """
    if len(iterable) == 0:
        return None
    elif len(iterable) == 1 and iterable[0] == '':
        return None
    else:
        return iterable


def adapt_text(text: str):
    """
    Args:
        text (str): texto da mensagem em string

    Returns:
        str: texto adaptado para função envelop
    """
    new_text = text[:].split('\n')
    if new_text[0] == '':
        del new_text[0]
    if new_text[-1] == '':
        del new_text[-1]
    return " ".join(new_text)

def envelop(text: str):
    """
    Melhora visualmente a mensagem enviada 
    Args:
        text (str): texto da mensagem em lina única
    Returns:
        str: texto formatado com html e css
    """
    size_line = 500 # in px
    new_text = f'<p style="margin:0;padding-bottom:0px;margin-bottom:0px; color:rgb(12, 12, 12); text-align: justify; width: {size_line}px; font-family: Arial, Helvetica, sans-serif;">'+ adapt_text(text) + '</p>'
    return new_text
