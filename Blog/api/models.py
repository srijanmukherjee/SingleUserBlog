import html

from django.contrib.auth.models import User
from django.db.models import Model, CharField, BooleanField, ForeignKey, CASCADE, TextField, DateTimeField

from admin.helper import convert_to_slug


class Post(Model):
    title = CharField(max_length=128)
    slug = CharField(max_length=200, unique=True)
    published = BooleanField(default=False)
    archived = BooleanField(default=False)
    private = BooleanField(default=False)
    published_on = DateTimeField(auto_now_add=True)
    last_update = DateTimeField(auto_now_add=True)
    published_by = ForeignKey(User, on_delete=CASCADE)
    keywords = CharField(max_length=200)
    content = TextField()

    def save(self, *args, **kwargs):
        self.title = html.escape(self.title.strip())
        self.keywords = html.escape(self.keywords.strip())
        self.slug = convert_to_slug(self.title)

        super(Post, self).save(*args, **kwargs)
