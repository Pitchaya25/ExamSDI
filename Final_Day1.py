from flask import *
import psutil as ps

app = Flask(__name__)

@app.route('/api/v1/vms/usages/<string:val>', methods=['GET'])
def vmsUsage(val):
    usage = {}
    if val == "cpu":
        usage['CPU'] = getCPU()
    elif val == "mem":
        usage['MEM'] = getMem()
    elif val == "disk":
        usage['DISK'] = getDisk()
    else:
        usage['CPU'] = getCPU()
        usage['MEM'] = getMem()
        usage['DISK'] = getDisk()
    usage['STATUS'] = 200
    return jsonify(usage), 200

def getCPU():
    return ps.cpu_percent(1)

def getMem():
    return ps.virtual_memory().used/(1024.0**3)

def getDisk():
    return ps.disk_usage("/").percent

app.run(host="0.0.0.0")