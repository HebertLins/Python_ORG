from decimal import ConversionSyntax
import requests


import requests

real = float(input("Digite o valor em real: R$"))

conversao = int(input("""Deseja converter para
1- Dólar
2- Euro
3- Bitcoin
"""))

if (conversao == 1):
    link = str('USDBRL')
elif (conversao == 2):
    link = str('EURBRL')
elif (conversao == 3):
    link = str('BTCBRL')
else:
    print("O valor digitado é inválido")

print(f"A opção escolhida foi {link}!")

url = f"https://economia.awesomeapi.com.br/json/last/{link}"
response = requests.get(url)

if response.status_code == 200:                                       # status_code ser igual a 200 significa que deu certo, erro daria outro valor
    dados = response.json()
    moedaEst = float((dados[link]['ask']))                      #Aq a gente tá percorrendo um JSON que é organizado através de chave e parenteses
    print(moedaEst)                                             #Todos os dados foram trazidos para "DADOS" dai pra frente, agr é so ir acessando as pastas
                                                                # ou seja entrar em 'USDBRL' para depois acessar o restante, como a "ask"#

 
    
valor_final = real / moedaEst
print(f"O resultado é {valor_final}")                                                                  
                                                                     
                                  