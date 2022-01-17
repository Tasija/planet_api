import pytest
from assertpy import assert_that


@pytest.mark.parametrize('planet', ['1', '2'])
def test_planet_status_success_code(https_object, planet):
    result = https_object.get(resource=f'planets/{planet}/')
    assert_that(result['status_code']).is_equal_to(200)


@pytest.mark.parametrize('planet', ['1', '2'])
def test_planet_success_code(https_object, planet, planet_config):
    request_result = https_object.get(resource=f'planets/{planet}/')['data']
    assert_that(request_result).is_equal_to(planet_config[planet])
