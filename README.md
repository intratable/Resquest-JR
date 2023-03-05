# Resquest-JR


GET 

    import requests

    if __name__ == '__main__':

    url = 'https://www.datacels.com/detectar-empresa-telefono'
    
    response = requests.get(url)

    if response.status_code == 200:
        print(response.content)

        content= response.content

        file = open('web.html', 'wb')
        file.write(content)
        file.close()
    
GET-COOKIES

     import requests

    if __name__ == '__main__':

    url = 'https://www.datacels.com/detectar-empresa-telefono'
    
    response = requests.get(url)

    if response.status_code == 200:
        cooikes= response.cookies
        
        print(cooikes)
                                         
GET-JSON
        
        import requests

        if __name__ == '__main__':

        url = 'https://www.datacels.com/detectar-empresa-telefono'

        response = requests.get(url)

        if response.status_code == 200:
            rjson= response.json
            print(rjson)
            argsjson = response.json['content'] #parte especifica del json 
          # print(argsjson)

            rjsontext = json.loads(response.text) # json.loads Deserializando el json  
            textjson = rjsontext['content'] 
          # print(textjson)
        
        
POST 

        import requests

        if __name__ == '__main__':

            codarea = sys.argv[1]
            linea = sys.argv[2]

            url = 'https://www.datacels.com/detectar-empresa-telefono'
            payload = {
                indicativo : codarea,
                bloque : linea,
                _token : 'eZ0xdBL428ZqSzxp9sTDrZkyZuApCfYvoAZfBiRb',
                buscador : 'Buscar'
                }

            response = requests.post(url, json=payload)

            """ 

           internamente el metodo post va a SERIALIZAR tomando el diccionario y convirtiendolo en json
           siempre y cuando el diccionario sea inviado por json = 
            """

             response = request.post (url, data=json.dumps(payload))

            """
           tambien se puede enviar el diccionario por data = pero en ese caso habria que SERIALIZAR el diccionario
           usando json.dumps


           """ 

            if response.status_code == 200:
                print(response.content)
                
HEADERS
    
    import requests

    if __name__ == '__main__':

    url = 'http://httpbin.org/post'
    header = {'Conten-Type' : 'application/json' }
    
    response = requests.post(url, headers=header)
    
    if response.status_code == 200:
        rheaders = response.headers
        print(rheaders)
        
COOKIS

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
      
oAuth

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
     
SESSIONS

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
    
