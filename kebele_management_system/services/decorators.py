from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You must be logged in to access this page.")
            
            # Check if the user has the required role or is a superuser
            if request.user.role == role or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            
            return HttpResponseForbidden("You don't have permission to access this page.")
        return _wrapped_view
    return decorator
