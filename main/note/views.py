from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def new_note(request):
    notes = Note.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')
        new_note = Note(title=title, content=content, image=image)
        new_note.created_by = request.user
        new_note.save()
        return redirect('note_list')
    return render(request, 'new.html', {'notes': notes})

@login_required
def note_list(request):
    notes = Note.objects.filter(created_by=request.user)
    
    return render(request, 'index.html', {'notes': notes})

def delete_note(request, pk):
    notes = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        notes.delete()
        return redirect('note_list')
    return render(request, 'delete.html', {'note': notes})

def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        new_title = request.POST.get('title', '')
        new_content = request.POST.get('content', '')
        new_image = request.FILES.get('image')
        
        # Validate form data
        if not new_title:
            return render(request, 'update.html', {"note": note, "error": "Title is required."})

        if not new_content:
            return render(request, 'update.html', {"note": note, "error": "Content is required."})

        if not new_image:
            return render(request, 'update.html', {"note": note, "error": "Image is required."})

        note.title = new_title
        note.content = new_content
        note.image = new_image
        note.save()

        return redirect('note_list')

    return render(request, 'update.html', {"note": note})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            return redirect('note_list')
        return render(request, 'login.html', {'success': 'Account created successfully'})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('note_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')