import requests

if __name__ == '__main__':

    url = 'https://www.datacels.com/detectar-empresa-telefono'
    
    response = requests.get(url)

    if response.status_code == 200:
        cook = response.cookies
                
        xsrftoken = cook['XSRF-TOKEN']
        laraveltoken = cook['laravel_session']

        cookiesf = { 'XSRF-TOKEN' : xsrftoken , 'laravel_session' : laraveltoken}

        print (cookiesf)
        #response = requests.get(url, cookies = cookiesf)

        #if response.status_code == 200:
          #  print(response.cookies)
    
        
        
    