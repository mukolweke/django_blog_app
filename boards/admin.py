from django.contrib import admin
from .models import Board, Topic, Post

# Registering models
admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)

