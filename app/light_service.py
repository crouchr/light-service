# microservice
import os
import time
import sys

from flask import Flask, jsonify, request

# artifacts
import solar_funcs

import light_sensor
import definitions
import get_env

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
    uuid = request.args.get('uuid')

    answer['status'] = 'OK'
    answer['uuid'] = uuid.__str__()
    answer['service_name'] = 'light-service'
    answer['version'] = get_env.get_version()

    print('status() : uuid=' + uuid + ', app_name=' + app_name.__str__() + ', version=' + answer['version'])
    response = jsonify(answer)

    return response


@app.route('/stats')
def stats():
    answer = {}
    app_name = request.args.get('app_name')
    uuid = request.args.get('uuid')

    answer['status'] = 'OK'
    answer['uuid'] = uuid.__str__()
    # answer['api_calls'] = -1    # not yet implemented

    print('status() : uuid=' + uuid + ', app_name=' + app_name.__str__() + ', api_calls=' + answer['api_calls'])
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
        uuid = request.args.get('uuid')

        # very crude averaging - take two readings with 1 second between
        lux1 = light_sensor.get_lux(Sensor)
        time.sleep(0.5)
        lux2 = light_sensor.get_lux(Sensor)
        time.sleep(0.5)
        lux3 = light_sensor.get_lux(Sensor)
        lux = (lux1 + lux2 + lux3) / 3.0
        lux_avg = round(lux, 2)

        sky_condition = solar_funcs.map_lux_to_sky_condition(lux_avg)
        watts = solar_funcs.convert_lux_to_watts(lux)

        print('get_lux_api() : uuid=' + uuid.__str__() + ', app_name=' + app_name.__str__() + ', lux=' + lux_avg.__str__() + ', solar=' + watts.__str__() + ', sky_condition=' + sky_condition)

        # Create response
        answer['status'] = 'OK'
        answer['uuid'] = uuid.__str__()
        answer['lux'] = lux_avg
        answer['watts'] = watts
        answer['sky_condition'] = sky_condition

        response = jsonify(answer)

        return response

    except Exception as e:
        answer['function'] = 'get_lux_api()'
        answer['uuid'] = uuid
        answer['error'] = str(e)
        print('get_lux_api() : uuid=' + uuid + ', app_name=' + app_name.__str__() + ', error : ' + e.__str__())
        response = jsonify(answer, 500)

        return response


if __name__ == '__main__':
    os.environ['PYTHONUNBUFFERED'] = "1"            # does this help with log buffering ?
    version = get_env.get_version()             # container version

    print('light-service started, version=' + version)
    Sensor, msg = light_sensor.register_light_sensor()  # set up hardware
    print(msg)

    if Sensor is None:
        time.sleep(1)
        print('light-service unable to access Yoctopuce light sensor, exiting...')
        sys.exit()

    app.run(host='0.0.0.0', port=definitions.listen_port.__str__())
