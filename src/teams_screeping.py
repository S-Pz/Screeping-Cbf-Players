import pandas as pd
import requests
import json
from bs4 import BeautifulSoup

home_page_= "https://www.cbf.com.br/futebol-brasileiro/times/campeonato-brasileiro/serie-a/2024"

headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'
}

response = requests.get(home_page_, headers=headers)



try:
  json_data = response.json()
  print(json_data)
  soup = BeautifulSoup(response.content, 'html.parser')
  find_href = soup.find(class_='styles__ClubsGrid-sc-15tpbpf-2 eQyJzu')

  href = find_href.find_all('a')
  
  #print(href)
  url_list:list = []

  for url in href:
    print(url)
    # url_list.append(url['href'])
    # print(url.find('h2').get_text())
    #url_dict["name"]=url

except:
  raise Exception(f"Error {response.status_code}") 

# for url in url_list:

#   completed_url = "https://www.cbf.com.br" + url

#   response = requests.get(completed_url, headers=headers)

#   if response.status_code == 200:
#       soup = BeautifulSoup(response.text, 'html.parser')
#       table = soup.find(class_='table m-t-30')

#       if table is not None:
#         for tbody in table.find_all('tbody'):
#           for tr_element in tbody.find_all('tr'):

#             th_element = tr_element.find('th')
#             td_elements = tr_element.find_all('td')

#             if len(td_elements) > 1:
#               titles = td_elements[1].find('img')
#             else:
#               titles = None

#             if th_element is not None:
#               nome = th_element.get_text()
#               linkg = th_element.a['href'] if th_element.a is not None else None
#               nome_jogador = nome.strip() if nome is not None else None
#             else:
#               nome = None
#               linkg = None
#               nome_jogador = None

#             apelido = td_elements[0].get_text()
#             apelido_jogador = apelido.strip() if apelido is not None else None

#             time = titles.get('title') if titles else "Time nao encontrado"
#             time_jogador = time.strip()

#             jogadores.append({
#               "Src" : linkg,
#               "Nome" : nome_jogador,
#               "Apelido" : apelido_jogador,
#               "Time" : time_jogador
#             })
#       else:
#         print("No table found")
#   else:
#     print(f"Request failed with status code {response.status_code}")

# df = pd.DataFrame(jogadores, columns=['Src','Nome', 'Apelido','Time']).drop_duplicates()
# df.to_csv("jogadores.csv", index=False, encoding='utf-8')