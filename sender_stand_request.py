import configuration
import data
import requests

def post_new_user(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)


response = post_new_user(data.user_body)

print(response.status_code)
print(response.json())

def post_kit_for_new_client(body):

    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH, json=body, headers=data.headers_kits)

response = post_kit_for_new_client(data.kit_body)

print(response.status_code)
print(response.json())