"""
Gerador de senhas simples
"""
from string import ascii_letters, punctuation, digits
from random import randint


def generate_password(password_length=8):
    """
    Gera uma senha aleatória apartir do padrão ascii
    Args:
        password_length (int, optional): Tamanho da senha. Defaults to 8.
    Returns:
        [str]: senha aleatória
    """
    characters = ascii_letters + punctuation + digits
    options = [char for char in characters]
    sweepstakes = [randint(0, len(options)-1) for c in range(0, password_length)]
    password_as_list = [options[number] for number in sweepstakes]
    official_password = ''.join(password_as_list)
    return official_password

password_length = 8
password = generate_password(password_length)
print(password)
