from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        print("It meeeee")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabsapp:home')  # Redirect to a success page.
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# When receiving a POST request, why do we redirect() and then render()?
