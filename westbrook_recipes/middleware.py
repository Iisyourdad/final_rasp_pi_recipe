# westbrook_recipes/middleware.py
from django.shortcuts import render

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # When a response has a 404 status, force it to use our template
        if response.status_code == 404:
            return render(request, '404.html', status=404)
        return response
