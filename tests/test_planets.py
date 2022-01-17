from assertpy import assert_that


def test_planets_status_success_code(https_object):
    result = https_object.get(resource='planets')
    assert_that(result['status_code']).is_equal_to(200)


def test_planets_page_not_found(https_object):
    result = https_object.get(resource='planets/?page=7')
    assert_that(result['status_code']).is_equal_to(404)
