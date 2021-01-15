
from yoctopuce.yocto_lightsensor import *


def register_light_sensor(target='any'):
    try:
        errmsg = YRefParam()

        # Setup the API to use local USB devices
        if YAPI.RegisterHub("usb", errmsg) != YAPI.SUCCESS:
            sys.exit("init error" + errmsg.value)

        if target == 'any':
            # retrieve any Light sensor
            sensor = YLightSensor.FirstLightSensor()
            if sensor is None:
                sys.exit('check USB cable')
        else:
            sensor = YLightSensor.FindLightSensor(target + '.lightSensor')

        if not (sensor.isOnline()):
            print('light sensor device not connected')

    except Exception as e:
        print(e.__str__())
        YAPI.FreeAPI()

    return sensor


def get_lux(sensor):
    """
    Read light level (in Lux) from light sensor
    :param sensor:
    :return:
    """

    if sensor.isOnline():
        lux = round(sensor.get_currentValue(), 2)
        if lux < 1.0:
            lux = 0.0       # headlights of passing cars ?
        return lux
    else:
        return None

