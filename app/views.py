from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import TodoItem


def index(request):
    todoitems = TodoItem.objects.all().order_by("create_at")
    context = {"todoitems":todoitems}
    return render(request, 'index.html',context)


@csrf_exempt
def todo_action(request):
    content = request.POST['content']
    TodoItem.objects.create(text=content)
    return HttpResponseRedirect('/')

@csrf_exempt
def delete(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
