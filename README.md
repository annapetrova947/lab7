# Лабораторная работа №7. REST. FastAPI. Swagger

## Запуск проекта 

```bash
docker-compose up
```
![alt text](1.jpg)
![alt text](2.png)

## Демонстрация

### Swagger
![alt text](3.jpg)

### Получение списка всех терминов.

```
GET 'http://localhost:8000/terms/'
```

![alt text](4.jpg)

### Получение информации о конкретном термине по ключевому слову.


```
GET "http://127.0.0.1:8000/terms/search/?keyword=Redux"
```

![alt text](5.jpg)

### Получение термина по id

```
GET "http://127.0.0.1:8000/terms/1"
```

![alt text](6.jpg)


### Добавление нового термина с описанием.
```
POST "http://127.0.0.1:8000/terms/"
```
![alt text](7.jpg)


### Обновление существующего термина.

```
PUT "http://127.0.0.1:8000/terms/5"
```

![alt text](8.jpg)


### Удаление термина из глоссария.

``` 
DELETE "http://127.0.0.1:8000/terms/5"
```

![alt text](9.jpg)
