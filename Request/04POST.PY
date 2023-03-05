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