import requests

if __name__ == '__main__':

    url = 'https://www.datacels.com/detectar-empresa-telefono'
    
    response = requests.get(url)

    if response.status_code == 200:
        cooikes= response.cookies
        
        print(cooikes)
        
    