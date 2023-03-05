import requests

user = ''
password = ''

acc_url = ''
# acces_token = ''

if __name__ == '__main__':

    url = 'https://www.aa.com/'
    paayload = {'user' : user, 'pass': password, 'code' : acc_url}
    headers = {'Accept' : 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()

        access_token = response_json ['access_token']
        print(acces_token)