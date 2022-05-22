import json


def fixtures_create(json_file_path):

    with open(json_file_path, 'r', encoding='utf-8') as jsonf:
        json_array = json.load(jsonf)

    json_array_new = []

    for json_data in json_array:
        json_array_new.append({
            "first_name": json_data["first_name"],
            "last_name": json_data["last_name"],
            "username": json_data["username"],
            "password": json_data["password"],
            "role": json_data["role"],
            "age": json_data["age"],
            "locations": [int(json_data["location_id"])],
        })

    json_fixture = []
    i = 1

    for json_data_fix in json_array_new:
        json_fixture.append({
            "model": "user.author",
            "pk": i,
            "fields": json_data_fix
        })
        i += 1

    with open('../user_fixture.json', 'w', encoding='utf-8') as jsonf:
        json.dump(json_fixture, jsonf, indent=4)


fixtures_create(r'USER.json')
