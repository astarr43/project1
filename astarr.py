import requests
import hashlib
import os
hash_value = input('Enter your file path : ')

api_key = input("Enter your api key: ")
if os.path.exists(hash_value):
        d = os.listdir(hash_value)
        # print(d)
        for we in d:
                if we.endswith('.exe' or '.bat'):
                        print(we)

        ro = input('choose your file : ')
            
        file_hash = hashlib.sha256(ro.encode()).hexdigest()
        print(file_hash)
        url = f'https://www.virustotal.com/api/v3/files/{file_hash}'

        headers = {'x-apikey' : api_key }
        response = requests.get(url,headers=headers)

        if response.status_code == 200:
                        data = response.json()

                        stats = data['data']['attributes']['last_analysis_stats']

                        print('malicious : ',stats['malicious'])
                        print('suspicious : ',stats['suspicious'])
                        print('undetected : ',stats['undetected'])

                        if stats['undetected'] < 60:
                          print('file safe') 
                        else:
                               print('file ok')
        else:
         print(response.status_code)

else:
        print('enter valid path.')