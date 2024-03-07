import json
import datetime

def get_api_key():
    #open file and read data
    with open("utils/api_usage.json", "r") as jsonFile:
        data = json.load(jsonFile)
    keys = data['keys']
    for key in keys:
        # print('hehe')
        if keys[key]["remain"] > 0:
            keys[key]["remain"] -= 1
            data['keys'] = keys
            update_usage(data)
            # print(keys[key]["key"])
            return keys[key]["key"]
    print("all api key unavailable")
    return None
    
def update_usage(data):
    # current_month = datetime.datetime.now().strftime("%m")
    # current_year = datetime.datetime.now().strftime("%Y")
    # if data['month'] != int(current_month) or data['year'] != int(current_year):
    #     for key in data['keys']:
    #         data['keys'][key]["remain"] = 500
    #         data['month'] = int(current_month)
    #         data['year'] = int(current_year)
    
    # manual_update()
    
    # Writing to sample.json
    with open("utils/api_usage.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def manual_update():
    with open("utils/api_usage.json", "r") as jsonFile:
        data = json.load(jsonFile)
    current_month = datetime.datetime.now().strftime("%m")
    current_year = datetime.datetime.now().strftime("%Y")
    if data['month'] != int(current_month) or data['year'] != int(current_year):
        print("update new month")
        for key in data['keys']:
            data['keys'][key]["remain"] = 500
            data['month'] = int(current_month)
            data['year'] = int(current_year)
    else:
        print("month no change")
    print("update success")
    return True        
# manual_update()
        