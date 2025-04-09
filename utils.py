# utils.py
import threading

_thread_locals = threading.local()

def set_request(request):
    _thread_locals.request = request

def get_request():
    return getattr(_thread_locals, 'request', None)
