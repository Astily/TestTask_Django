import datetime
from django.utils.deprecation import MiddlewareMixin
from .models import LogStore


class RequestLoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        request.start_time = datetime.datetime.now()

    def process_response(self, request, response):
        delta = datetime.datetime.now() - request.start_time
        url = request.path
        log_obj = LogStore(executionTime=str(delta), url=url)
        log_obj.save()
        return response
