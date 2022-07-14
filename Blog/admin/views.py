import json

from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView

from api.models import Post
from .decorators import with_post


class Home(TemplateView):
    template_name = "admin/home.html"


class CreatePostView(TemplateView):
    template_name = "admin/create.html"


class PostListView(ListView):
    template_name = "admin/posts.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 10
    ordering = ['-published_on']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(archived=False)


@csrf_exempt
@with_post
def save_post(request, post: Post):
    body = json.loads(request.body)
    title = body['title']
    content = body['content']
    keywords = body['keywords'] if 'keywords' in body else ''

    if not post:
        post = Post(title=title, content=content, keywords=keywords, published_by=request.user)
    else:
        post.title = title
        post.content = content
        post.keywords = keywords

    try:
        post.save()
    except IntegrityError:
        return JsonResponse({"error": {"title": "Title is not unique!"}}, status=400)

    return JsonResponse({
        "pk": post.pk,
        "created_on": post.published_on,
        "last_update": post.last_update
    })


def preview_post(request, slug: str):
    try:
        post = Post.objects.get(slug=slug)
        return render(request, "admin/preview.html", context={"post": post})
    except Post.DoesNotExist:
        return HttpResponse("Post doesn't exist")
