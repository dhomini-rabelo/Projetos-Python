"""
Projeto de Iniciante beep sound

Objetivo: retornar som de 'beep' utilizando a biblioteca winsound
Variáveis globais:
 - time: com essa variável o usuário altera o tempo em que o beep sound ocorre.
 - frequency: com essa variável o usuário altera o tempo em que o beep sound ocorre. 
"""
import winsound

frequency = 1700
time = 400

winsound.Beep(frequency, time)
