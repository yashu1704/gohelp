from django.shortcuts import render, redirect
from .models import Client, ServiceProvider, ServiceHistory
from .forms import ClientForm, ServiceProviderForm, ServiceHistoryForm

def client_list(request):
    clients = Client.objects.all()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Redirect to avoid resubmission
    else:
        form = ClientForm()
    return render(request, 'help/client_list.html', {'clients': clients, 'form': form})

def service_provider_list(request):
    service_providers = ServiceProvider.objects.all()
    if request.method == 'POST':
        form = ServiceProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_provider_list')  # Redirect to avoid resubmission
    else:
        form = ServiceProviderForm()
    return render(request, 'help/service_provider_list.html', {'service_providers': service_providers, 'form': form})

def service_history_list(request):
    service_history = ServiceHistory.objects.all()
    if request.method == 'POST':
        form = ServiceHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_history_list')  # Redirect to avoid resubmission
    else:
        form = ServiceHistoryForm()
    return render(request, 'help/service_history_list.html', {'service_history': service_history, 'form': form})