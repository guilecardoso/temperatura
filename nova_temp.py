url = "https://www.sensacaotermica.com.br/curitiba-pr/"

#parou de funcionar o requests
#import requests

#utilizado essa a partir de 13/9/20
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as bs4

# parou junto com o requests
#page = requests.get(url)
#soup = bs4(page.text,'html.parser')

req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
page = urlopen(req).read()
soup = bs4(page,'html.parser')

cidade = soup.find(class_="h2_interno")
cidade
#<h2 class="h2_interno">Curitiba - PR</h2>
cidade.contents
#['Curitiba - PR']
cidade.contents[0]
#'Curitiba - PR'

table = soup.find(class_="dados")
table.contents
# ['\n', <tbody><tr>
# <th colspan="3">DATA</th>
# <th>MÁX</th>
# <th>MIN</th>
# <th>NASCER SOL</th>
# <th>POR SOL</th>
# <th>VELOC. VENTO</th>
# </tr>
# <tr><td>TER</td><td>05/03/2019</td><td>Tempestades se formando à tarde.</td><td class="max">27 ºC</td><td class="min">18 ºC</td><td>06:13:25</td><td>06:43:43</td><td>11 km/h</td></tr><tr><td>QUA</td><td>06/03/2019</td><td>Tempestades.</td><td class="max">25 ºC</td><td class="min">18 ºC</td><td>06:13:52</td><td>06:42:39</td><td>11 km/h</td></tr><tr><td>QUI</td><td>07/03/2019</td><td>Tempestades.</td><td class="max">27 ºC</td><td class="min">18 ºC</td><td>06:14:23</td><td>06:41:40</td><td>13 km/h</td></tr><tr><td>SEX</td><td>08/03/2019</td><td>Tempestades se formando à tarde.</td><td class="max">29 ºC</td><td class="min">18 ºC</td><td>06:14:54</td><td>06:40:41</td><td>16 km/h</td></tr><tr><td>SÁB</td><td>09/03/2019</td><td>Tempestades se formando à tarde.</td><td class="max">27 ºC</td><td class="min">18 ºC</td><td>06:15:25</td><td>06:39:41</td><td>11 km/h</td></tr> </tbody>]

table.tr
# <tr>
# <th colspan="3">DATA</th>
# <th>MÁX</th>
# <th>MIN</th>
# <th>NASCER SOL</th>
# <th>POR SOL</th>
# <th>VELOC. VENTO</th>
# </tr>

table.td
#<td>TER</td>
table.tr()
# [<th colspan="3">DATA</th>, <th>MÁX</th>, <th>MIN</th>, <th>NASCER SOL</th>, <th>POR SOL</th>, <th>VELOC. VENTO</th>]

tr = table.find_all("tr")

tr
# [<tr>
# <th colspan="3">DATA</th>
# <th>MÁX</th>
# <th>MIN</th>
# <th>NASCER SOL</th>
# <th>POR SOL</th>
# <th>VELOC. VENTO</th>
# </tr>, <tr><td>TER</td><td>05/03/2019</td><td>Tempestades se formando à tarde.</td><td class="max">27 ºC</td><td class="min">18 ºC</td><td>06:13:25</td><td>06:43:43</td><td>11 km/h</td></tr>, <tr><td>QUA</td><td>06/03/2019</td><td>Tempestades.</td><td class="max">25 ºC</td><td class="min">18 ºC</td><td>06:13:52</td><td>06:42:39</td><td>11 km/h</td></tr>, <tr><td>QUI</td><td>07/03/2019</td><td>Tempestades.</td><td class="max">27 ºC</td><td class="min">18 ºC</td><td>06:14:23</td><td>06:41:40</td><td>13 km/h</td></tr>, <tr><td>SEX</td><td>08/03/2019</td><td>Tempestades se formando à tarde.</td><td class="max">29 ºC</td><td class="min">18 ºC</td><td>06:14:54</td><td>06:40:41</td><td>16 km/h</td></tr>, <tr><td>SÁB</td><td>09/03/2019</td><td>Tempestades se formando à tarde.</td><td class="max">27 ºC</td><td class="min">18 ºC</td><td>06:15:25</td><td>06:39:41</td><td>11 km/h</td></tr>]


td = []
# linha 1 dia atual, vai até a linha 5
for t in tr[1]:
    td.append(t)

td
# [<td>TER</td>, <td>05/03/2019</td>, <td>Tempestades se formando à tarde.</td>, <td class="max">27 ºC</td>, <td class="min">18 ºC</td>, <td>06:13:25</td>, <td>06:43:43</td>, <td>11 km/h</td>]
td[3]
#<td class="max">27 ºC</td>
td[3].contents
#['27 ºC']
td[3].contents[0]
#'27 ºC'
semana = td[0].contents[0]
dia = td[1].contents[0]
clima = td[2].contents[0]
maxima = td[3].contents[0]
minima = td[4].contents[0]
nascer_sol = td[5].contents[0]
por_sol = td[6].contents[0]
vel_vento = td[7].contents[0]

chaves = ["Semana","Dia","Clima","Maxima","Minima","Nascer do Sol","Por do Sol","Velocidade vento"]
valore = [semana,dia,clima,maxima,minima,nascer_sol,por_sol,vel_vento]

tudo = dict(zip(chaves,valore))

# print(tudo)
for x in tudo:
  print(f"{x}: {tudo[x]}")

#10 cidades mais frias
frias = soup.find_all(class_="cor_fria")
#10 cidades mais quentes
quentes = soup.find_all(class_="cor_quente")

#primeira cidade mais fria
frias[0].contents[0]
#10a cidade mais quente
quentes[len(quentes)-1].contents[0]

#fase da lua
lua = soup.find_all("strong")
lua[0].contents[0]
