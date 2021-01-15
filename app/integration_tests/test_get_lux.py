import integration_definitions
import call_rest_api


def test_get_lux():
    """
    Test /status
    :return:
    """
    query = {}
    query['app_name'] = 'integration_tests'

    status_code, response_dict = call_rest_api.call_rest_api(integration_definitions.endpoint_base + '/get_lux', query)

    assert status_code == 200
    assert response_dict['lux'] >= 0.0

