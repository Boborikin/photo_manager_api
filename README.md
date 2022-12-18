# Photo Manager API

## Запуск

---
**Скопировать данные из файла <i>.env.example</i> в файл <i>.env</i> и изменить данные на ваши**

**Для сборки и запуска**
```shell
docker-compose up -d 
```

**Проект доступен по ссылке ниже:**
```text
http://localhost:8000/
```

## Методы API

**Регистрация пользователя**
```shell
curl -X POST 'http://127.0.0.1:8000/auth/register/'\
   -H 'Content-Type: application/json' \
   -d '{"username":"<username>","password":"<password>",
   "email":"<email>","first_name":"<first_name>","last_name":"<last_name>"}'
```
**Вход пользователя**
```shell
curl -X POST 'http://127.0.0.1:8000/auth/login/'\
   -H 'Content-Type: application/json' \
   -d '{"username":"<username>","password":"<password>"}'
```

**Вернется значение <i>access</i>**.
**Данное access значение используется для получения/добавления данных.**

**Добавление фотографии**

```bash
curl -XPOST 'http://127.0.0.1:8000/api/v1/photos/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <access>' \
  -H 'Content-Type: multipart/form-data' \
  -F 'picture=@<picture_url>' \
  -F 'latitude=<value>' \
  -F 'longitude=<value>' \
  -F 'description=<value>' \
  -F 'people_list=<value>, <value>' \
  -F 'upload_date=<datetime>'
```

**Получение списка фотографий**

```shell
curl -XGET '127.0.0.1:8000/api/v1/photos/' -H 'Authorization: Bearer <access>'
```

**Получение информации о фото с метаданными по ID**

```shell
curl -XGET '127.0.0.1:8000/api/v1/photos/<id>/' -H 'Authorization: Bearer <access>'
```

**Получение списка фотографий с сортировкой / фильтрацией:**

```shell
curl -XGET '127.0.0.1:8000/api/v1/photos/?upload_date_gte=2022-12-18' -H 'Authorization: Bearer <access>'
```

#### Параметры:

Доступные варианты сортировки:<br>

`ordering=upload_date` - по возрастанию<br>
`ordering=-upload_date` - по убыванию<br>

Доступные варианты фильтрации даты:

`upload_date=2022-12-18`  - дата создания<br>
`upload_date_gte=` - дата создания больше или равно<br>
`upload_date_lte=` - дата создания меньше или равно<br>
`upload_date_gt=` - дата создания больше чем<br>
`upload_date_lt=` - дата создания меньше чем<br>

Доступные варианты фильтрации геолокации:

`geolocation=Египет` - название города/улицы/страны вводятся русскими буквами.
При этом необязательно вводить полное название города/улицы/страны, можно ввести, например `Егип`, и фильтрация будет
происходить по неполному названию. Не чувствительно к регистру.

Доступные варианты фильтрации имен людей на фото:

`people_list=John` - Вводите имя человека.  
При этом необязательно вводить полное имя,
можно ввести часть и фильтрация будет происходить по неполному имени. 
Не чувствительно к регистру.

### Для удобства тестирования и просмотра всего перечня функций

---

Мною была добавление документация с помощью <a href="https://github.com/axnsan12/drf-yasg">drf-yasg</a>.

Доступно как <a href="http://127.0.0.1:8000/swagger"><b>Swagger</b></a>, так и <a href="http://127.0.0.1:8000/redoc"><b>Redoc</b></a> документация.