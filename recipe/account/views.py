from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "{} created successfully".format(username))
            return redirect('home')
        else:
            messages.error(request, "Invalid form!\nTry Again.")
            form = CustomUserCreationForm()

    return render(request, 'register.html', {'form':form})