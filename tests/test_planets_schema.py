from assertpy import assert_that


def test_planets_schema_status_success_code(https_object):
    result = https_object.get(resource='planets/schema/')
    assert_that(result['status_code']).is_equal_to(200)
