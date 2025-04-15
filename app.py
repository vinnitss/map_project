from flask import Flask, render_template, jsonify
import csv
import os

app = Flask(__name__)

# Чтение данных из CSV файла
def read_objects_from_csv():
    objects = []
    try:
        file_path = os.path.join('data', 'objects.csv')  # Путь к файлу в папке data
        if os.path.exists(file_path):
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    objects.append(row)
        else:
            raise FileNotFoundError("CSV файл не найден.")
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
    return objects

# Главная страница
@app.route('/')
def index():
    # Находим центр карты (среднее значение координат)
    objects = read_objects_from_csv()
    if not objects:
        map_center = {'lat': 55.7558, 'lon': 37.6176}  # Москва по умолчанию
    else:
        latitudes = [float(obj['lat']) for obj in objects]
        longitudes = [float(obj['lon']) for obj in objects]
        map_center = {'lat': sum(latitudes) / len(latitudes), 'lon': sum(longitudes) / len(longitudes)}

    return render_template('index.html', api_key='YOUR_YANDEX_API_KEY', map_center=map_center)

# API для получения объектов
@app.route("/api/objects")
def api_objects():
    csv_path = os.path.join("data", "objects.csv")
    objects = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                obj = {
                    "id": row["id"],
                    "name": row["name"],
                    "info": row["info"],
                    "lat": float(row["lat"]),
                    "lon": float(row["lon"]),
                    "type": row["type"],
                    "status": row["status"]
                }
                objects.append(obj)
            except Exception as e:
                print(f"Ошибка при обработке строки: {row}\n{e}")
    return jsonify(objects)

# Страница с подробной информацией об объекте
@app.route('/object/<int:object_id>')
def object_detail(object_id):
    objects = read_objects_from_csv()
    obj = next((item for item in objects if int(item['id']) == object_id), None)
    if obj:
        return render_template('object_detail.html', object=obj)
    return "Объект не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
