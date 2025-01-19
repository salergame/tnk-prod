from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger(__name__)

class LogRedirectURIMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if '/accounts/google/login/callback/' in request.build_absolute_uri():
            logger.debug("Redirect URI: %s", request.build_absolute_uri())
