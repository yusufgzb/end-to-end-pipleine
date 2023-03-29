upload docker-composue file

Install Docker

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install docker.io

sudo apt install docker-compose

sudo apt-get update

sudo docker -v

sudo docker-compose -v

---

sudo docker-compose up -d

----
nifi

![image](https://user-images.githubusercontent.com/44902732/228493799-b39ceab1-178c-4220-afa2-cfd7e2fe8183.png)


----
kafka



>docker exec -it kafka-docker bash

>kafka-topics.sh --create --topic ornek --bootstrap-server localhost:9092
    
    Created topic ornek.




#Console producer

>kafka-console-producer.sh --topic ornek --bootstrap-server localhost:9092

>first message
>realtime message



#console consumer realtime

>kafka-console-consumer.sh --topic ornek --bootstrap-server localhost:9092
    
    first message
    realtime message
