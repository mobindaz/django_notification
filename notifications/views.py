from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Notification
from .forms import NotificationForm, LoginForm
from django.urls import reverse

def index(request):
    notifications = Notification.objects.order_by('-created_at')
    return render(request, 'notifications/index.html', {'notifications': notifications})

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'notifications/admin_login.html', {'form': form})

@login_required
def admin_dashboard(request):
    notifications = Notification.objects.all()
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save()
            return redirect(reverse('admin_dashboard'))
    else:
        form = NotificationForm()
    
    context = {
        'form': form,
        'form_title': 'Add New Notification',
        'button_text': 'Add Notification',
        'notifications': notifications,
    }
    return render(request, 'notifications/admin_dashboard.html', context)
@login_required
def add_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = NotificationForm()
    return render(request, 'notifications/add_notification.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def edit_notification(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_dashboard'))
    else:
        form = NotificationForm(instance=notification)
    
    context = {
        'form': form,
        'form_title': 'Edit Notification',
        'button_text': 'Save Changes',
    }
    return render(request, 'notifications/admin_dashboard.html', context)

def delete_notification(request, pk):
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        notification.delete()
        return redirect(reverse('admin_dashboard'))
    
    context = {
        'notification': notification,
    }
    return render(request, 'notifications/confirm_delete.html', context)
