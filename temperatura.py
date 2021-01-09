import urllib.request, json

url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/6731/current?token=f1c5f496ee82002b669422247f945ef0"

req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})

#codigo 6731 é curitiba
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

# print(tudo)

for x in tudo:
	print(f"{x}: {tudo[x]}")
