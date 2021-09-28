import json

def get_value(key):
    with open("./data/config.json", encoding='utf*8') as config:
        data = json.load(config)
        value = data[key]
        return value

async def set_value(key, value):
    with open("./data/config.json", encoding='utf*8') as config:
        data = json.load(config)
    data[key] = value
    with open("./data/config.json", 'w') as config:
        json.dump(data, config)