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
        
        
    