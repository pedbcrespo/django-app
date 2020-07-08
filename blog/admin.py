from django.contrib import admin
from .models import Categoria
from .models import Transacao
from .models import Post

admin.site.register(Categoria)
admin.site.register(Transacao)
admin.site.register(Post)
# Register your models here.
