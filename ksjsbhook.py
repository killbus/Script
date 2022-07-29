import codecs
from flask import Flask, request
import frida

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getsig():
    str = request.args.get('str', '')
    session = frida.get_device_manager().get_remote_device().attach('快手极速版')
    with codecs.open('./hookzr.js', 'r', 'utf-8') as f:
        source = f.read()
    #return source
    script = session.create_script(source)
    script.load()
    sign = script.exports.getsig(str)
    return sign
app.run(port=5000)