# API para cadastro de tarefas

## Steps para a criação de um CRUD simples usando o Django Rest Framework
 Após criar o ambiente de desenvolvimento e instalar o django e djangorestframework
 
 - Criar o projeto em Django
 

```
$ django-admin startproject django_todo
$ cd django_todo

```

- Dentro da página do projeto, crie um aplicativo

```
$ python3 manage.py startapp todo
```

- Declare o aplicativo criado e o rest_framework no settings.py do Django

```
INSTALLED_APPS = [
    ...
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
    'rest_framework',
]
```

- Criação do Model (Model em Python, são classes que representam um objet no banco de dados)

```
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 100)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str___(self):
        return self.title
        
```

- Crie as migrations e na sequência rode as migrates

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

- Criar o serializer para o model <br>
<i>O serializer tem a função de converter o nosso model para o formato JSON, para que possamos criar o endpoit que será consumido através de serviços externos</i>

```
from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__" # Passamos todos os campos, mas podemos declarar apenas os campos necessários quando for o caso
```

- Criando a View com os métodos para o CRUD <br>
```
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from todo.serializers import TodoSerializer
from todo.models import Todo

# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
```

- Criando os caminhos (urls)

```
from django.urls import path
from todo import views

urlpatterns = [
    path("",views.ListTodoAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo")
]
```

- Configurando a url.py do repositório base

```
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/todo/',include("todo.urls"))
]
```

# Testando a API
