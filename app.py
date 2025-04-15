from flask import Flask, render_template, jsonify
import csv
import os

app = Flask(__name__)

app.config['YANDEX_API_KEY'] = os.environ.get('YANDEX_API_KEY', 'ВАШ_КЛЮЧ_ПО_УМОЛЧАНИЮ')

data_file = os.path.join(os.path.dirname(__file__), 'data', 'objects.csv')

# Чтение CSV и преобразование в список словарей
def read_csv():
    objects = []
    with open(data_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader):
            objects.append({
                'id': idx,
                'name': row['Название объекта'],
                'info': row['дополнительная информация'],
                'lat': float(row['широта']),
                'lon': float(row['долгота']),
                'type': row['тип объекта'],
                'status': row['статус объекта']
            })
    return objects

@app.route('/')
def index():
    return render_template('index.html', api_key=app.config['YANDEX_API_KEY'])

@app.route('/api/objects')
def get_objects():
    return jsonify(read_csv())

@app.route('/object/<int:obj_id>')
def object_detail(obj_id):
    objects = read_csv()
    obj = next((o for o in objects if o['id'] == obj_id), None)
    return render_template('detail.html', obj=obj)

if __name__ == '__main__':
    app.run(debug=True)