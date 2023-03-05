import requests

if __name__ == '__main__':

    url = 'http://httpbin.org/post'
    header = {'Conten-Type' : 'application/json' }
    
    response = requests.post(url, headers=header)
    
    if response.status_code == 200:
        rheaders = response.headers
        print(rheaders) 