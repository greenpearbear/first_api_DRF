import json


def fixtures_create(json_file_path):
    json_array = []

    with open(json_file_path, 'r', encoding='utf-8') as jsonf:
        json_array = json.load(jsonf)

    json_array_new = []

    for json_data in json_array:
        json_array_new.append({
            "id": json_data['Id'],
            "name": json_data['name'],
            "author": json_data['author'],
            "price": json_data['price'],
            "description": json_data['description'],
            "address": json_data['address'],
            "is_published": json_data['is_published']
        })

    json_fixture = []
    i = 1

    for json_data in json_array_new:
        json_fixture.append({
            "model": "ads.announcement",
            "pk": i,
            "fields": json_data
        })

    with open('announcement_fixture.json', 'w', encoding='utf-8') as jsonf:
        json.dump(json_fixture, jsonf, indent=4)


fixtures_create(r'Announcement.json')
