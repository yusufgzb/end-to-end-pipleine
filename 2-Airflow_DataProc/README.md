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

echo -e "AIRFLOW_UID=$(id -u)" > .env

docker-compose up airflow-init

sudo docker-compose up -d

![image](https://user-images.githubusercontent.com/44902732/228494711-e22ecce5-e5d9-40b5-9413-2d31619bded1.png)


![image](https://user-images.githubusercontent.com/44902732/228495129-8c6d44c5-d4bd-44a2-bef6-451db787d1fb.png)


