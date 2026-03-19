import requests
api_key = "0af097982ab18dd43e82486df7d2ed7ad483757fcecbb9ac05318a09b6449b4e"
hash_value = '8c27f3fb746a321a3bc7b371672aafb1d61c6d2f46fa8f36a1e8185058254b48'
url = f'https://www.virustotal.com/api/v3/files/{hash_value}'

headers = {'x-apikey' : api_key  }

response = requests.get(url,headers = headers)
print(response.json())

if response.status_code == 200:
     data = response.json()
    
     stats = data['data']['attributes']['last_analysis_stats']

     print("malicious:",stats['malicious'])
     print('suspicious',stats['suspicious'])
     print('undetected',stats['undetected'])

else:
     print(response.status_code)