# CRM-система для медицинского диагностического центра

## 📋 Описание проекта

CRM-система для автоматизации работы медицинского диагностического центра. Система обеспечивает:

- Онлайн-запись пациентов на приём к врачам и на диагностические процедуры
- Ведение электронных медицинских карт (история болезней, диагнозы, назначения)
- Управление расписанием работы врачей
- Учёт оказанных медицинских услуг
- Формирование отчётов для руководства
- Полный контроль системы для администратора

## 🛠️ Технологии

- **Backend:** Python, FastAPI, SQLAlchemy
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose

## 🚀 Запуск проекта

### Предварительные требования

- Python 3.11+
- PostgreSQL 15+
- Docker (опционально)

### Локальный запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Wheysed/CRM-Medical-Center.git
cd CRM-Medical-Center/backend
Создайте и активируйте виртуальное окружение:

bash
python3 -m venv .venv
source .venv/bin/activate  # для Linux/Mac
# .venv\Scripts\activate  # для Windows
Установите зависимости:

bash
pip install -r requirements.txt
Создайте файл .env на основе .env.example и настройте подключение к БД:

bash
cp .env.example .env
# Отредактируйте .env, указав свои параметры
Создайте базу данных PostgreSQL:

sql
CREATE DATABASE medcrm_db;
CREATE USER medcrm_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE medcrm_db TO medcrm_user;
Запустите приложение:

bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
Откройте в браузере:

Сайт: http://localhost:8000/

Документация API: http://localhost:8000/docs

Запуск с Docker
bash
docker-compose up -d
📚 API Документация
После запуска сервера документация доступна по адресу:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

Основные эндпоинты
Раздел	Метод	Эндпоинт	Описание
Patients	POST	/api/patients/	Создать пациента
Patients	GET	/api/patients/	Получить всех пациентов
Doctors	POST	/api/doctors/	Добавить врача
Services	GET	/api/services/	Получить все услуги
Appointments	POST	/api/appointments/	Записаться на приём
MedicalRecords	GET	/api/medical-records/patient/{id}	Медзаписи пациента
🧪 Тестирование
Запуск тестов:

bash
cd backend
pytest tests/ -v
📁 Структура проекта
text
medcrm_system/
├── frontend/          # HTML, CSS, JS (ЛР №1)
├── backend/           # FastAPI приложение (ЛР №2-3)
│   ├── app/
│   │   ├── models/    # SQLAlchemy модели
│   │   ├── schemas/   # Pydantic схемы
│   │   └── routers/   # API эндпоинты
│   ├── .env.example   # Пример переменных окружения
│   ├── requirements.txt
│   └── seed.py        # Наполнение БД тестовыми данными
└── docker-compose.yml
👥 Участники
Участник	Роль
Путенихин А.А.	Team Lead, Backend, DevOps
Ардаширов Р.Р.	Frontend, Тестирование, Документация
Пищурин Р.И.	Backend, База данных
📄 Лицензия
MIT

📞 Контакты
По всем вопросам обращайтесь к администратору системы.
