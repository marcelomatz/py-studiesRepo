import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

with open('relatorio.txt', 'w') as relatorio:
    for pergunta in html.select('.question-summary'):
        titulo = pergunta.select_one('.question-hyperlink')
        data = pergunta.select_one('.relativetime')
        votos = pergunta.select_one('.vote-count-post')

        relatorio.write(
            f'\tQUANDO? {data.text} | \tDÚVIDA: {titulo.text} | \tVOTOS: {votos.text}\n')
