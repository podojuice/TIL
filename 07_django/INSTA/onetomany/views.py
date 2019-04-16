from django.shortcuts import render, redirect
from .models import Book, Writer, Chapter
from .forms import *


def create(request):
    if request.method == 'POST':
        form = WriterModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WriterModelForm()
    return render(request, '', {
        'form': form,
    })


def update(request, id):
    writer = Writer.objects.get(id=id)
    if request.method == 'POST':
        form = WriterModelForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect()
    else:
        form = WriterModelForm(instance=writer)
    return render(request, '', {
        'form': form,
    })
