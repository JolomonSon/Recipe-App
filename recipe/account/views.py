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
            return redirect('login')
        else:
            messages.error(request, "Invalid form! Try Again.")
            form = CustomUserCreationForm()

    return render(request, 'register.html', {'form':form})

def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user':user})
