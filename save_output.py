import json

def save_tags(username, data):
    result = {
        "username": username,
        "interests": data["tags"],
        "audience_size": data["audience_size"]
    }

    with open("output.json", "w") as f:
        json.dump(result, f, indent=4)
    