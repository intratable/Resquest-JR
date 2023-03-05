# Resquest-JR



[![33.jpg](https://i.postimg.cc/Bvn9SggS/33.jpg)](https://postimg.cc/WdCfS0CC)



suplantar los 0.0.0 por la mascara de subred del gateway a escanear 

    #!/bin/bash
   
    for i in $(seq 1 254); do
            timeout 1 bash -c "ping -c 1 0.0.0.$i" &> /dev/null && echo "[+]Host  0.0.0.$i - ACTIVE"&
    done; wait
    
el $i hace referencia al ultimo argumento de la IP especificada que se le aplica un secuenciador de 1 a 254; como se define en el for 

     for i in $(seq 1 254)                   
                
                ej      192.168.0.$i = 192.168.0.1 
                                        192.168.0.2
                                         192.168.0.3 
                                         
para aplicarse en un grupo mas reducido de posibilidades, modificar el segundo argumento del secuenciador ya que hace referencia al limite del mismo
        
        ej
         for in$(seq 1 10)
            for in$(seq 1 7)
            for in$(seq 1 24)
 

## Build and install from source

`git clone https://github.com/intratable/Detect-IP-ON.git`

`cd ip_on`

`chmod +x build.sh`

`./build.sh`


## Usage

    ./IP_ON.sh

