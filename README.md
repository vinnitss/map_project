# Система отображения объектов строительства на карте (Flask + Yandex Maps)

## 📌 Описание

Веб-приложение для визуализации объектов строительства на карте Яндекс. Поддерживаются фильтры по типу и статусу, всплывающие карточки с информацией и переход на отдельную страницу объекта.

## 🚀 Технологии

- Flask (Python)
- JavaScript (Yandex Maps API)
- Tailwind CSS
- CSV-файл как источник данных
- NGINX-ready (можно развернуть на сервере)

## 📁 Структура

map_project/ 
├── app.py 
├── requirements.txt 
├── README.md 
├── data/ 
│   └── objects.csv 
└── templates/ 
    ├── index.html 
    └── detail.html


## 📦 Установка

```bash
git clone https://github.com/vinnitss/map_project.git
cd map_project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
