
from yoctopuce.yocto_lightsensor import *


def register_light_sensor(target='any'):
    try:
        print('entered register_light_sensor()')

        errmsg = YRefParam()

        # Setup the API to use local USB devices
        if YAPI.RegisterHub("usb", errmsg) != YAPI.SUCCESS:
            msg = "light sensor init error" + errmsg.value
            return None, msg

        if target == 'any':
            # retrieve any Light sensor
            sensor = YLightSensor.FirstLightSensor()
            if sensor is None:
                msg = 'check light sensor USB cable'
                return None, msg
        else:
            sensor = YLightSensor.FindLightSensor(target + '.lightSensor')

        if not (sensor.isOnline()):
            msg = 'light sensor device not connected'
            return None, msg

        return sensor, 'light sensor registered OK'

    except Exception as e:
        print(e.__str__())
        YAPI.FreeAPI()
        return None




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
