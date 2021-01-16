import light_service_funcs


def test_calc_watts():
    """
    :return:
    """
    lux = 1000      # is 7.9 W/mm-squared
    watts = light_service_funcs.calc_watts(lux)

    assert watts == 7.9