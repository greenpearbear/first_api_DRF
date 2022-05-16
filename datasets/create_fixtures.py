import json


def fixtures_create(json_file_path):
    json_array = []

    with open(json_file_path, 'r', encoding='utf-8') as jsonf:
        json_array = json.load(jsonf)

    json_array_new = []

    for json_data in json_array:
        json_array_new.append({
            "id": json_data["id"],
            "name": json_data["name"],
            "lat": json_data["lat"],
            "lng": json_data["lng"],
        })

    json_fixture = []
    i = 1

    for json_data in json_array_new:
        json_fixture.append({
            "model": "user.location",
            "pk": i,
            "fields": json_data
        })

    with open('location_fixture.json', 'w', encoding='utf-8') as jsonf:
        json.dump(json_fixture, jsonf, indent=4)


fixtures_create(r'LOCATION.json')
