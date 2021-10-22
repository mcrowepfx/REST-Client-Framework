import requests

class ServiceResponseError(RuntimeError):
    def __init__(self, request, msg):
        from rest_client_framework.request import FrozenRequest
        self.request = FrozenRequest(request)
        if isinstance(msg, requests.Response):
            self.response = msg
            msg = 'The request failed with HTTP status {}.'.format(
                self.response.status_code
            )
        super().__init__(msg)

class MaximumAttemptsExceeded(RuntimeError):
    def __init__(self, request, responses, attempts):
        from rest_client_framework.request import FrozenRequest
        self.request = FrozenRequest(request)
        self.responses = responses
        self.attempts = attempts
        super().__init__('Failed to complete {} request to {} after {} attempts.'.format(
            request.method, request.get_printable_url(), attempts
        ))

class WebServiceDefinitionError(RuntimeError):
    pass