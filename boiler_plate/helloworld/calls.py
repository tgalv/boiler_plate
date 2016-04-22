"""
Requests made to other Microservices.
"""

from urllib.parse import urljoin

from process_digital_mortgage import app


app.config.from_object(os.environ.get('SETTINGS'))


class _APIBase:
    """
    The Base Class for a collaborating service call.
    """
    
    base = ''

    def _get_json(self, url, schema = None, params = None):
        """
        A `get` request with logging and schema validation.

        :type url: str
        :type schema: str
        :type params: dict

        :returns: The response from the service.
        :rtype: str
        """
        url = urljoin(self.base, url)
        app.logger.debug("get: '%s' : '%s'...", url, params)
        response = requests.get(url, params=params)
        response.raise_for_status()
        ret_val = json.loads(response.text)
        app.logger.debug(response.text)
        if schema is not None:
            jsonschema.validate(ret_val, schema)
        return ret_val

    def _post_json(self, url, data=None, schema=None):
        """
        A `post` request with logging, schema validation
        and exception checking.
        
        :type url: str
        :type data: dict
        :type schema: str

        :returns: The response from the service.
        :rtype: str
        """
        url = urljoin(self.base, url)
        if schema is not None:
            jsonschema.validate(data, schema)
        if data is None:
            data = {}
        app.logger.debug("post: '%s' : '%s'...", url, data)
        response = requests.post(url, data=json.dumps(data))
        response.raise_for_status()
        app.logger.debug(response.text)
        return response.text


class _DemoAPI(_APIBase):
    """
    TODO: Replace this with calls to Microservices.
    """

    base = app.config.get('DEMO_API')

    def greet_boiler_plate(self):
        """
        Hit the index of another boiler_plate.
        """
        return self._get_json('/')

DEMO_API = _DemoAPI()

        
