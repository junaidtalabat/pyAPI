from behave import *
import requests
import json
from payload import *
from utilities.configurations import *
from utilities.resources import *


@given('I have login auth credentials')
def step_impl(context):
    context.url = getConfig()['LoginAPI']['endpoint'] + ApiResources.logintoken
    context.headers = {"Accept-Encoding": "gzip", "Accept-Language": "en-US", 'BrandType': "1",
                       "User-Agent": "Talabat/6.0.4 (iPhone; iOS 11.1; Scale/3.00)",
                       "Content-Type": "application/x-www-form-urlencoded",
                       "X-Device-Source": "4", "X-Device-Version": "6.0.4"}
    context.payload = loginpayload()


@when(u'I hit login POST request')
def step_impl(context):
    context.response = requests.post(context.url, data=context.payload, headers=context.headers, )


@then(u'token type should be bearer')
def step_impl(context):
    response_json = context.response.json()
    assert response_json['token_type'] == 'bearer'
    bearer = response_json['token_type']
    print(bearer)
    print("")


@then(u'I must fetch the access token')
def step_impl(context):
    response_json = context.response.json()
    accessoken = response_json['access_token']
    print(accessoken)
    print("")


@then(u'status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    assert context.response.status_code == statusCode
    print(context.response.status_code)
    print("")


@then(u'validate schema type access_token')
def step_impl(context):
    response_json = context.response.json()
    accesstoken = response_json['access_token']
    assert  type(accesstoken) == str
    print(type(accesstoken))
    print("")


@then(u'validate schema type of token_type')
def step_impl(context):
    response_json = context.response.json()
    token_type = response_json['token_type']
    assert type(token_type) == str
    print(type(token_type))
    print("")


@then(u'validate schema type of expires_in')
def step_impl(context):
    response_json = context.response.json()
    expires_in = response_json['expires_in']
    assert type(expires_in) == int
    print(type(expires_in))
    print("")


@then(u'validate header Content-Type')
def step_impl(context):
    assert context.response.headers['Content-Type'] == 'application/json;charset=UTF-8'


@then(u'validate header Transfer-Encoding')
def step_impl(context):
    assert context.response.headers['Transfer-Encoding'] == 'chunked'


@then(u'validate header Content-Encoding')
def step_impl(context):
    assert context.response.headers['Content-Encoding'] == 'gzip'
