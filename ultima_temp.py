import urllib.request, json

url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/6731/current?token=f1c5f496ee82002b669422247f945ef0"

req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})

with urllib.request.urlopen(req) as curitiba:
    dados = json.loads(curitiba.read().decode())

cidade = dados["name"]
estado = dados["state"]
temper = dados["data"]["temperature"]
condic = dados["data"]["condition"]
humida = dados["data"]["humidity"]
sensas = dados["data"]["sensation"]

chaves = ["Cidade","Estado","Temperatura","Condicao climatica","Humidade do ar","Sensasao termica"]
valore = [cidade,estado,temper,condic,humida,sensas]

tudo = dict(zip(chaves,valore))


url = "https://www.sensacaotermica.com.br/curitiba-pr/"

from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as bs4

req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
page = urlopen(req).read()
soup = bs4(page,'html.parser')

cidade = soup.find(class_="h2_interno")

table = soup.find(class_="dados")
tr = table.find_all("tr")

td = []
for t in tr:	
    td.append(t)

semana = td[1].contents[0].contents[0]
dia = td[1].contents[1].contents[0]
clima = td[1].contents[2].contents[0]
maxima = td[1].contents[3].contents[0]
minima = td[1].contents[4].contents[0]
nascer_sol = td[1].contents[5].contents[0]
por_sol = td[1].contents[6].contents[0]
vel_vento = td[1].contents[7].contents[0]

chaves = ["Semana","Dia","Clima","Maxima","Minima","Nascer do Sol","Por do Sol","Velocidade vento"]
valore = [semana,dia,clima,maxima,minima,nascer_sol,por_sol,vel_vento]

tudo2 = dict(zip(chaves,valore))

#10 cidades mais frias
frias = soup.find_all(class_="cor_fria")
#10 cidades mais quentes
quentes = soup.find_all(class_="cor_quente")

c_f = []
for f in frias:
	c_f.append(f.contents[0])

c_q = []
for q in quentes:
	c_q.append(q.contents[0])

lua = soup.find_all("strong")

from tabulate import tabulate

geral = []
climate = []

for dados in td[2:]:
	geral.append([dados.contents[0].contents[0],dados.contents[1].contents[0],dados.contents[2].contents[0],dados.contents[3].contents[0],dados.contents[4].contents[0],dados.contents[5].contents[0],dados.contents[6].contents[0],dados.contents[7].contents[0]])
	climate.append(f"({dados.contents[0].contents[0]}){dados.contents[2].contents[0]}")

tres_cidades = [["3 Cidades mais quentes","3 Cidades mais frias"],
				[f"{c_q[0]}",f"{c_f[0]}"],
				[f"{c_q[1]}",f"{c_f[1]}"],
				[f"{c_q[2]}",f"{c_f[2]}"]]
as_tres = tabulate(tres_cidades,tablefmt='fancy_grid',headers="firstrow")

tabelao = [[f"Semana: {tudo2['Semana']}",f"Dia: {tudo2['Dia']}"],
			[f"Cidade: {tudo['Cidade']}",f"Estado: {tudo['Estado']}"],
			[f"Temperatura: {tudo['Temperatura']} °C"],
			[f"Maxima: {tudo2['Maxima']}",f"Minima: {tudo2['Minima']}"],
			[f"Sensasao termica: {tudo['Sensasao termica']}",f"Humidade do ar: {tudo['Humidade do ar']}"],
			[f"Velocidade vento: {tudo2['Velocidade vento']}",f"Lua: {lua[0].contents[0]}"],
			[f"Nascer do Sol: {tudo2['Nascer do Sol']}",f"Por do Sol: {tudo2['Por do Sol']}"]]


vaiqvai = tabulate(tabelao,tablefmt="fancy_grid")

from rich.console import Console
from rich.table import Table
from rich import box

tablea = Table(title="Proximos dias",show_lines=True)
tablea.add_column("Sem")
tablea.add_column("Dia")
tablea.add_column("Max")
tablea.add_column("Min")
tablea.add_column("Nascer Sol")
tablea.add_column("Por Sol")
tablea.add_column("Vel vento")
tablea.add_column("Clima", no_wrap=False)

for d in geral:
	tablea.add_row(d[0],d[1],d[3],d[4],d[5],d[6],d[7],d[2])

console = Console()

tobe = Table(show_header=False,box=box.ROUNDED)
tobe.add_row(f"Condicao climatica: {tudo['Condicao climatica']}",f"Clima: {tudo2['Clima']}")

print(vaiqvai)
console.print(tobe)
print(as_tres)
console.print(tablea)