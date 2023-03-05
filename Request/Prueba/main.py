import requests

indicativo = 11 #sys.argv[1]
bloque = 66414342 #sys.argv[2]
_token = 'eZ0xdBL428ZqSzxp9sTDrZkyZuApCfYvoAZfBiRb'
buscador = 'Buscar'
Remote Address = '151.106.111.203:443'
REQUEST-XSRF-TOKEN	= ''
REQUEST-laravel_session = ''
RESPONSE-XSRF-TOKEN = ''

#'indicativo={indicativo}&bloque={bloque}&_token=eZ0xdBL428ZqSzxp9sTDrZkyZuApCfYvoAZfBiRb&buscador=Buscar'

if __name__ == '__main__':

    url = 'https://www.datacels.com/detectar-empresa-telefono'
    payload = {'indicativo' : indicativo, 'bloque': bloque, '_token' : _token, 'buscador' : buscador}
    headers = {

        'authority': "www.datacels.com",
        'method': "POST",
        'path': "/detectar-empresa-telefono",
        'scheme': "https",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "es-ES,es;q=0.6",
        'cache-control': "max-age=0",
        'content-length': "93",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "XSRF-TOKEN=eyJpdiI6IkpVTVMzdmFPdFM2Y0tVTUNHVlRkV2c9PSIsInZhbHVlIjoid1JqWStaSlg3TW1qazZlSkttUEVnNzFkdWRhYWFrQm9JVElJUHliZ3ZocVk2V0drZUd5bkNEK3hYZnF5WXRUdGFIbzFmTjFJSlF1OVdoWVlRNlRxdUUvOWZSODZCNm1UUGgwOC9sNVNBY0V6a2pML2hwbWJWUTMwNU9TbVJLKzIiLCJtYWMiOiJlMWZjMTY3NTY0MDYxN2M2ZWYwY2MxMjdjOTUyMWM1NGRhNDdlZTM5NzA2MTJmMTRmNmE3YWVmMDQ5OWIzYTcyIn0%3D; laravel_session=eyJpdiI6IkwrcUUwTjJaOGd2cUlBR1ViaUFPTnc9PSIsInZhbHVlIjoiaVlLNjIyZktGa0kwYVVSZXgvUlZyNUpId1lmVGR3RmlRQnVYTFhRTkt4WWk4VnliRkEvL254N3ZaSXhGR1FvMTNGWDREeGlubEw5d0JLUGx0ZFc2UnN3TXU2TEVIdTFvSGp0TFFHcytuNERkcWI5UE82dlMwYWtKR3hsdEx1aWUiLCJtYWMiOiIyYmJjZTQ0Y2UzMGQ3OGQwYmVkMGQ0YWQwMzI1ODhjZWNjNjJlNTkwMjFiNmI0ZjgwY2VhZGY3YjdhZTg4ZGRkIn0%3D",
        'origin': "https://www.datacels.com",
        'referer': "https://www.datacels.com/detectar-empresa-telefono",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': "document",
        'sec-fetch-mode': "navigate",
        'sec-fetch-site': "same-origin",
        'sec-fetch-user': "?1",
        'sec-gpc': "1",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print('fa')