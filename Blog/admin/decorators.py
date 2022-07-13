import json

from django.http import JsonResponse

from api.models import Post


def handle_json_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except json.JSONDecodeError:
            return JsonResponse({"error": "invalid request"}, status=400)
        except KeyError:
            return JsonResponse({"error": "missing parameters in the request"}, status=500)

    return wrapper


def with_post(func):
    @handle_json_error
    def wrapper(request):
        post = None
        try:
            body = json.loads(request.body)

            if 'pk' in body and body['pk'] is not None:
                primary_key = body['pk']
                post = Post.objects.get(pk=primary_key)

            return func(request, post)
        except Post.DoesNotExist:
            return JsonResponse({"error": "post does not exist"}, status=404)

    return wrapper
