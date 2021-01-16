# fixme : add time so that 'sunset/sunrise' can be added
# fixme - full moon is not reliable
def map_lux_to_sky_condition(lux):
    """

    :param lux:
    :return:
    >>> map_lux_to_sky_condition(0.1)
    'dark'
    >>> map_lux_to_sky_condition(8.0)
    'twilight'
    >>> map_lux_to_sky_condition(100.0)
    'overcast'
    >>> map_lux_to_sky_condition(10000.0)
    'daylight'
    >>> map_lux_to_sky_condition(50000.0)
    'bright sky'
    """
    if lux <= 0.1:
        condition = 'dark'
    # elif lux <= 0.2:
    #     condition = 'full moon'
    elif lux <= 10:
        condition = 'twilight'
    elif lux <= 1000:
        condition = 'overcast'
    elif lux <= 30000:
        condition = 'daylight'
    elif lux <= 100000:
        condition = 'bright sky'

    return condition


def calc_watts(lux):
    """
    Convert lux to watt/mm squared
    :param lux:
    :return:
    """
    watts = round((lux * 0.0079), 2)

    return watts
