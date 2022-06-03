import json

import requests

# URL = "http://127.0.0.1:8000/student/"
#
# data = {
#     'name': 'Ahmer Iqbal',
#     'profession': 'Flutter Developer',
#     'mobile_no': +923142525258,
#     'roll_number': 12,
#     'degree': 'Software Engineering',
#     'city': 'Burewala',
# }
#
# json_data = json.dumps(data)
#
# response = requests.post(url=URL, data=json_data)
# data = response.json()
# print(data)


# response = requests.get(url=URL)
# data = response.json()
# print(data)

URL = "http://127.0.0.1:8000/studentapi/"


# TODO GET DATA
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    response = requests.get(url=URL, data=json_data)
    data = response.json()
    print(data)


# get_data()

# TODO POST DATA
def post_data():
    data = {
        'name': 'kaka Khan',
        'profession': 'Badminton Player',
        'mobile_no': +923036101010,
        'roll_number': 22,
        'degree': 'MBA',
        'city': 'Multan',
    }

    json_data = json.dumps(data)

    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


# post_data()


# TODO UPDATE DATA
def update_data():
    data = {
        'id': 3,
        'name': 'Nehhhhhhhha Khan',
        'profession': 'Armfdsay Man',
        'degree': 'Donasdft know',
        'city': 'Tibasdfba Sultan Pur'
    }

    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data)
    data = response.json()
    print(data)


# update_data()


# TODO DELETE DATA
def delete_data():
    data = {'id': 2}
    json_data = json.dumps(data)
    response = requests.delete(url=URL, data=json_data)
    data = response.json()
    print(data)

delete_data()
