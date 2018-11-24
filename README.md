
Simple application which handle architecture below with Docker, Django-rest, PostgreSQL and Mosquitto.

![Image of services](https://raw.githubusercontent.com/loopstock-io/challenges/master/backend-devs/backend-challenge.png)

## 1. Installation
Clone this repository.
```
https://github.com/ybekdemir/loopstock-challenge.git
cd loopstock-challenge

```
Build API, postgres and MQTT services with docker-compose
```
cd api
docker-compose build
docker-compose up

```

Build Integer generator instances
```
cd ..
cd integer_generator
docker-compose build
docker-compose up scale integergenerator=2

```

Build Average calculator instance
```
cd ..
cd average_calculator
docler-compose build
docker-compose up
```

You can access API on http://localhost:8000/api/values/

```
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:8000/api/values/

```
