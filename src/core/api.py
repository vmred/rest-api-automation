import json
from xml.dom import minidom

import requests
from src.helpers.logger import Logger


class API(Logger):

    def __init__(self):
        super().__init__()
        self._hostname = ''
        self._cookies = {}
        self._headers = {}
        self._request_params = {}

    def _set_request_params(self, params):
        self._request_params.update(params)

    def get_request_params(self):
        return self._request_params

    def _set_header(self, headers):
        self._headers.update(headers)

    def get_headers(self):
        return self._headers

    def get_header(self, key):
        return self._headers[key]

    def _set_hostname(self, value):
        self._hostname = value

    def get_hostname(self):
        return self._hostname

    def set_cookies(self, key, value):
        self._cookies[key] = value

    def get_cookies(self):
        return self._cookies

    def get_cookie_by_name(self, value):
        return self.get_cookies().get(value)

    @staticmethod
    def format_response_data(response):
        if response.headers and 'content-type' in response.headers.keys():
            content_type = response.headers['content-type']

            if 'text/plain' in content_type:
                return response.content.decode('utf-8')

            if 'application/json' in content_type:
                return json.loads(response.content)

            if 'application/xml' in content_type:
                return minidom.parse(response.content)

        # unknown response data format, returning as is
        return response.content

    def post(self, api, data):
        api_call = self.get_hostname() + api
        response = requests.post(api_call, data, params=self.get_request_params())
        self.log('sending POST, url: {}, data: {}'.format(api_call, data))
        self.log('status code: {}'.format(response.status_code))
        response_data = self.format_response_data(response)
        self.log('response data: {}'.format(response_data))
        return response, response_data

    def put(self, api, data):
        api_call = self.get_hostname() + api
        response = requests.put(api_call, data)
        self.log('sending PUT, url: {}, data: {}'.format(api_call, data))
        self.log('status code: {}'.format(response.status_code))
        response_data = self.format_response_data(response)
        self.log('response data: {}'.format(response_data))
        return response, response_data

    def get(self, api):
        api_call = self.get_hostname() + api
        response = requests.get(api_call, headers=self.get_headers(), params=self.get_request_params())
        self.log('sending GET, url: {}'.format(api_call))
        self.log('status code: {}'.format(response.status_code))
        response_data = self.format_response_data(response)
        self.log('response data: {}'.format(response_data))
        return response, response_data

    def delete(self, api):
        api_call = self.get_hostname() + api
        response = requests.get(api_call)
        self.log('sending DELETE, url: {}'.format(api_call))
        self.log('status code: {}'.format(response.status_code))
        response_data = self.format_response_data(response)
        self.log('response data: {}'.format(response_data))
        return response, response_data
