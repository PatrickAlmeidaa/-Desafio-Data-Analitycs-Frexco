import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error

#lendo os dados e definindo e espaço de tempo para previsão
tabela = pd.read_excel('Dados.xlsx', 'Query result')
vendas = tabela['Vendas']
window_size = 5

#calculo da previsão de demanda
def previsao_demanda(vendas, window_size):
    media = calc_media_movel(vendas, window_size)
    previsao = np.zeros(len(vendas) - window_size + 1)
    previsao[0] = media[0]
    for i in range(1, len(previsao)):
        previsao[i] = previsao[i - 1] * window_size + media[i]
        previsao[i] /= window_size + 1
    return previsao

#calculo da média movel
def calc_media_movel(vendas, window_size):
    media2 = np.zeros(len(vendas) - window_size + 1)
    for i in range(len(media2)):
        media2[i] = np.mean(vendas[i:i + window_size])
    return media2

#previsão com todos os dados fornecidos
prev_total = previsao_demanda(vendas, window_size)

#previsão sem os ultimos 5 dias dos dados fornecidos
prev_total_erro = previsao_demanda(vendas[0:40], window_size)

#formatação para não mostrar casas decimais no previsão de vendas
prev_total_final = [round(x, 0) for x in prev_total]

print("Previsão de vendas para os proximos 5 (cinco) dias: ", prev_total_final[-5:])
print("Erro na previsão: ", round(mean_absolute_percentage_error(prev_total[-5:], prev_total_erro[-5:]), 3))