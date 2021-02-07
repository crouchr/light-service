import uuid
import integration_definitions
import call_rest_api


def test_get_lux():
    """
    Test /status
    :return:
    """
    query = {}
    this_uuid = uuid.uuid4().__str__()

    query['app_name'] = 'integration_tests'
    query['uuid'] = this_uuid.__str__()

    status_code, response_dict = call_rest_api.call_rest_api(integration_definitions.endpoint_base + '/get_lux', query)

    assert status_code == 200
    assert response_dict['status'] == 'OK'

    assert response_dict['lux'] >= 0.0
    assert response_dict['watts'] >= 0.0

    assert response_dict['uuid'] == this_uuid
