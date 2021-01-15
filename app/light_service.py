# microservice
import os
import time
import sys

from flask import Flask, jsonify, request

import light_sensor
import light_service_funcs
import definitions

app = Flask(__name__)


# fixme : this does not give info about the actual exception
@app.errorhandler(500)
def error_handling(error):
    answer = {}
    answer['error'] = str(error)
    print('light_service() : error : ' + error.__str__())
    response = jsonify(answer, 500)

    return response


# an endpoint that can be polled with little overhead
@app.route('/status')
def status():
    answer = {}
    app_name = request.args.get('app_name')

    answer['status'] = 'OK'
    answer['version'] = light_service_funcs.get_version()

    print('status() : app_name=' + app_name.__str__() + ', version=' + answer['version'])
    response = jsonify(answer)

    return response


@app.route('/get_lux')
def get_lux_api():
    """

    :param app_name: e.g. name of the calling app so it can be identified in logs
    :return:
    """
    try:
        answer = {}
        app_name = request.args.get('app_name')

        lux = light_sensor.get_lux(Sensor)

        print('get_lux_api() : app_name=' + app_name.__str__() + ', lux=' + lux.__str__())

        # Create response
        answer['status'] = 'OK'
        answer['lux'] = lux

        response = jsonify(answer)

        return response

    except Exception as e:
        answer['function'] = 'get_lux_api()'
        answer['error'] = str(e)
        print('get_lux_api() : app_name=' + app_name.__str__() + ', error : ' + e.__str__())
        response = jsonify(answer, 500)

        return response


if __name__ == '__main__':
    os.environ['PYTHONUNBUFFERED'] = "1"            # does this help with log buffering ?
    version = light_service_funcs.get_version()     # container version

    print('flight_service started, version=' + version)
    Sensor, msg = light_sensor.register_light_sensor()  # set up hardware
    print(msg)

    if Sensor is None:
        time.sleep(3)
        sys.exit()

    app.run(host='0.0.0.0', port=definitions.listen_port.__str__())
