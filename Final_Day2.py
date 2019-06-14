from flask import *
import subprocess

app = Flask(__name__)

@app.route('/api/v1/ping', methods=['POST'])
def getData():
    data = request.get_json()
    destination = data['destination']

    result = {}
    val_result = {}
    for h in destination:
        pingHost(h, val_result)

    result["result"] = val_result
    # print(result)
    # print(type(result))

    return jsonify(result)

def pingHost(host, dic_val):
    try:
        ping_byte = subprocess.check_output("ping " + host)
        ping_str = ping_byte.decode("utf-8")
        ping_split = ping_str.split()
        dic_val[host] = ping_split[len(ping_split)-1]
    except:
        print("Error!!")

app.run(host="0.0.0.0")