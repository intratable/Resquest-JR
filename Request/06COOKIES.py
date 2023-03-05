import requests

if __name__ == '__main__':

    url = 'https://www.datacels.com/detectar-empresa-telefono'

    """ 
        extraer cookies
    """
    
    response = requests.get(url)

    if response.status_code == 200:
        cookies = response.cookies
        print(response.cookies)
        print(response.content)

    """

    enviar cookies

    """

    cookies = {'' : '', '' : ''}
    
    response = requests.get(url, cookies = cookies)

    if response.status_code == 200:
        print(response.content)

        content= response.content
