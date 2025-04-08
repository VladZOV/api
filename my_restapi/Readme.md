# FSTR API: Система учёта перевалов

## 📌 О проекте
REST API для мобильного приложения, позволяющего туристам фиксировать данные о перевалах (координаты, фото, уровень сложности). Реализовано на Django REST Framework.

## 🔧 Функционал
- ✅ Добавление данных о перевале (POST)
- ✅ Редактирование данных (PATCH, только для статуса "new")
- ✅ Получение данных по email пользователя (GET)
- 📊 Документация Swagger/OpenAPI


Установить зависимости:

pip install -r requirements.txt


🌐 Документация API
Доступна через Swagger UI:
🔗 https://api-fstr.onrender.com/swagger/

Или Redoc:
🔗 https://api-fstr.onrender.com/redoc/

📝 Примеры запросов
1. Добавление перевала (POST)
URL: https://api-fstr.onrender.com/submitData/

Запрос:

bash
Copy
curl -X POST "https://api-fstr.onrender.com/submitData/" \
-H "Content-Type: application/json" \
-d '{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "",
  "user": {
    "email": "user@example.com",
    "fam": "Иванов",
    "name": "Петр",
    "otc": "Сергеевич",
    "phone": "+79991234567"
  },
  "coords": {
    "latitude": "45.3842",
    "longitude": "7.1525",
    "height": "1200"
  },
  "level": {
    "winter": "",
    "summer": "1А",
    "autumn": "1А",
    "spring": ""
  }
}'
Ответ:

json
Copy
{
  "status": 200,
  "message": "Отправлено успешно",
  "id": 42
}
2. Редактирование перевала (PATCH)
URL: https://api-fstr.onrender.com/submitData/42/

Запрос:

bash
Copy
curl -X PATCH "https://api-fstr.onrender.com/submitData/42/" \
-H "Content-Type: application/json" \
-d '{
  "title": "Новое название",
  "level": {
    "summer": "2А"
  }
}'
Ответ (успех):

json
Copy
{
  "state": 1,
  "message": null
}
Ответ (ошибка):

json
Copy
{
  "state": 0,
  "message": "Редактирование запрещено: запись не в статусе 'new'"
}
3. Получение данных по email (GET)
URL: https://api-fstr.onrender.com/submitData/?user__email=user@mail.ru

Ответ:

json
Copy
[
  {
    "id": 42,
    "title": "Пхия",
    "user": {
      "email": "user@example.com",
      "name": "Петр"
    },
    "coords": {
      "latitude": "45.3842",
      "longitude": "7.1525"
    }
  }
]
🛠 Технологии:

Python 3.10
Django 4.2
Django REST Framework
PostgreSQL

Swagger/OpenAPI

