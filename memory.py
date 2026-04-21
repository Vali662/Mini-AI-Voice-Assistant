import json

def save_memory(key, value):
    data = {}
    try:
        with open("memory.json", "r") as f:
            data = json.load(f)
    except:
        pass

    data[key] = value

    with open("memory.json", "w") as f:
        json.dump(data, f)

def get_memory(key):
    try:
        with open("memory.json", "r") as f:
            data = json.load(f)
            return data.get(key, "I don't know")
    except:
        return "No memory found"