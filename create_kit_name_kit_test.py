import data
import sender_stand_request

def get_kit_body(name):

    kit_body = {
        'name': "Mi conjunto"
    }

    return kit_body

def negative_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_kit_for_user(kit_body)

    assert response.status_code == 400

def test_parameter_not_in_solicitude_get_error_response():
        negative_assert("{}")

def test_number_in_name_get_error_response():
    negative_assert("123")

def test_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_name_is_0_get_error_response():
    negative_assert("")

def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_kit_for_new_client(kit_body)

    assert response.status_code == 201

def test_numbers_in_name_get_success_response():
    positive_assert("123")

def test_character_special_name_get_success_response():
    positive_assert("&/((%$···")

def test_511_letter_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_spaces_in_name_get_success_response():
    positive_assert("A aaa")

def test_1_letter_name_get_success_response():
    positive_assert("A")

