import requests



url ='https://www.rexcarga.net/checkout'
payload = {
        'telefono':"11111111111111111",
        'monto':"1111",
        'nombre_apellido':"@Krisipo Pai",
        'documento':"11111111",
        'credit_card':"1111 1111 1111 1111",
        'exp_date':"11/" ,
        'sec_code':"1111",
        }
headers = {

        'authority':"www.rexcarga.net",
        'method':"POST",
        'path':"/checkout",
        'scheme':"https",
        'accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding':"gzip, deflate, br",
        'accept-language':"es-ES,es;q=0.8",
        'cache-control':"max-age=0",
        'content-length':"149",
        'content-type':"application/x-www-form-urlencoded",
        'origin':"https'://www.rexcarga.net",
        'referer':"https://www.rexcarga.net/movistar",
        'sec-ch-ua-mobile':"?0",
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest':"document",
        'sec-fetch-mode':"navigate",
        'sec-fetch-site':"same-origin",
        'sec-fetch-user':"?1",
        'sec-gpc':"1",
        'upgrade-insecure-requests':"1",
        'user-agent':"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
                

    }

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print(response)