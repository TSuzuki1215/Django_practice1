from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import PostForm

from .models import *

from django.core.paginator import Paginator


# Create your views here.

def index(request, now_page=1):
    memos = Memo.objects.all()
    page = Paginator(memos, 10)
    params = {
        'page': page.get_page(now_page),
        'form': PostForm()
    }
    return render(request, 'index.html', params)

def post(request):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid():
        form.save()
    else:
        print(form.errors)

    return redirect(to='/')