users = {'ID_1234': 12,
         'ID_25343': 13,
         'ID_4564': 34,
         'ID_6644': 23,
         'ID_3453': 45,
         'ID_45645': 23,
         'ID_5656': 70,
         'ID_43456': 34,
         'ID_57567': 45,
         'ID_6745': 57,
         'ID_6756': 36,
         'ID_45654': 34}


def slovar():
    new_slov = {}

    spisok = list(users.values())
    spisok.sort()

    key1 = list(users.keys())
    index1 = list(users.values()).index(spisok[0])
    key2 = list(users.keys())
    index2 = list(users.values()).index(spisok[-1])


    new_slov['rare'] = key1[index1]
    new_slov['frequently'] = key2[index2]

    return new_slov






def find_key(data, special_key):
    if isinstance(data, dict):
        if special_key in data:
            return data[special_key]
        for value in data.values():
            result = find_key(value, special_key)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_key(item, special_key)
            if result is not None:
                return result
    return None


j =  {
  "id": "root",
  "data": {
    "type": "container",
    "items": [
      {
        "id": "item1",
        "value": 10
      },
      {
        "id": "nested_group",
        "metadata": {
          "level": 2,
          "target_key": "Найдено!"
        },
        "list": [5, 6]
      }
    ]
  }
}

print(find_key(j, "target_key"))