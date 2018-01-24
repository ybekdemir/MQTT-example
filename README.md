# WATTX CHALLENGE

Application for loopstock.io challenge with Docker, Django-rest and PostgreSQL via https://github.com/loopstock-io/challenges/tree/master/backend-devs

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

**Note: ** I didn't implement bonus point, I think it can be solved with new queue between two integer generator. Hovewer,
with this solution one of the generator must wait for producing integer from other one.
