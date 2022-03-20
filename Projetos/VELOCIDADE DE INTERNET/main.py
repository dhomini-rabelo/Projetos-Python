"""
Projeto de iniciante - Velocidade de Internet

Objetivo: retorna velocidade de download e upload do usuário apartir da biblioteca speedtest

Variáveis globais:
 - speed_data: instância da classe Speedtest
 - download_speed: valor de download
 - upload_speed: valor de upload
"""

# Importações necessárias
from support import format_web_speed
from speedtest import Speedtest

#* Obtendo valores em float
speed_data = Speedtest()
download_speed = speed_data.download()
upload_speed = speed_data.upload()

# Formatando os valores para string
download_speed = format_web_speed(download_speed)
upload_speed = format_web_speed(upload_speed)

#* retornando resultado para usuário
print(f'Velocidade de download: {download_speed} Mbps')
print(f'Velocidade de upload: {upload_speed} Mbps')
