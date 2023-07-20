from django.http import JsonResponse


class ExceptionHandlingMiddleware:
    """Handle uncaught exceptions instead of raising a 500.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    @staticmethod
    def process_exception(request, exception):
        if isinstance(exception, CustomMiddlewareException):
            # Show warning in admin using Django messages framework
            messages.warning(request, str(exception))
            # Or you could return json for your frontend app
            return JsonResponse({'error': str(exception)})

        return None  # Middlewares should return None when not applied
