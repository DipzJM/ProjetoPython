from urllib.parse import urlparse
from django.conf import settings

class ForceCorrectHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        site_url = getattr(settings, 'SITE_URL', None)
        if site_url:
            parsed = urlparse(site_url)
            request.META['HTTP_HOST'] = parsed.netloc
            request.META['wsgi.url_scheme'] = parsed.scheme
            if 'HTTP_X_FORWARDED_PROTO' not in request.META:
                request.META['HTTP_X_FORWARDED_PROTO'] = parsed.scheme
        return self.get_response(request)