import requests

# URL for the JSON data
url = "https://www.cbf.com.br/_next/data/IBxkbsVR0-vMEBqtSHfnY/futebol-brasileiro/times/campeonato-brasileiro/serie-a/2024/62194.json?slug=campeonato-brasileiro&slug=serie-a&slug=2024&slug=62194"

# Define headers
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    'Referer': 'https://www.cbf.com.br/futebol-brasileiro/times/campeonato-brasileiro/serie-a/2024',
    'Cookie': 'cookies_accepted_categories=technically_required; _hjSessionUser_976019=eyJpZCI6ImRmN2U5YmRmLTIyYzUtNTdiZC05MWEwLTliNTBhMjkxOTdhYiIsImNyZWF0ZWQiOjE3Mjk2MTYyMDQxNTYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_976019=eyJpZCI6ImUwMDgwZTYxLWE4NWItNGE0YS04NjkxLTI2NWUxYmE0YzU3ZiIsImMiOjE3Mjk2MTYyMDQxNTcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _ga_VN8QK704R4=GS1.1.1729616204.1.1.1729616513.0.0.0; _ga=GA1.1.1239552774.1729616204',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.90',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'x-nextjs-data': '1'
}

# Perform the GET request
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    json_data = response.json()  # Automatically parse JSON
    print(json_data)
else:
    print(f"Error: {response.status_code}")


#pesquisar esse request de api do site da cbf, que não era para ser exposto mas por um motivo está exposto