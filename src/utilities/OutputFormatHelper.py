import json

def OutputJson(region, ):
    output_json = dict()
    otp = list()
    output_map = dict()
    output_map["region"] = "New York"
    output_map["total_cost"] = 100
    output_map["machines"] = [
        {
            "a": 1,
            "b": 2
        }
    ]
    otp.append(output_map)
    otp.append(output_map)
    output_json["Output"] = otp
    json_string = json.dumps(output_json, indent=4)
    print(json_string)
    return json_string