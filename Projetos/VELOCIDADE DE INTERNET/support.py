"""
Descrição:
Arquivo .py com funções de auxilio para o programa principal 
"""
def format_web_speed(web_speed:float):
    """
    Essa função visa adaptar valor da biblioteca speedtest de bytes para megabytes

    Args:
        web_speed(float): velociade de internet em bytes

    Returns:
        web_speed(str): formatado para megabytes com escrita no padrão brasileiro
    """
    web_speed = round(web_speed/10**6, 2)
    web_speed = str(web_speed).replace('.', ',')
    return web_speed
