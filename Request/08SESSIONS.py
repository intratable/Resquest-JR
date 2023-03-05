import requests

if __name__ == '__main__':

    url = 'https://www.datacels.com/detectar-empresa-telefono'
    
    session = requests.session(url)
    session.auth = ('','')
    response = session.get(url)
    if response.status_code == 200:
        print(response.content)
        response = session.get ('https://www.a.com')
        if response.status_code == 200:
            print(response.cookies)
        else :
            print(response.content)
    else :
        print(response.content)
    