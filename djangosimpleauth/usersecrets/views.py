from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from usersecrets.models import UserSecret


def secret(request):
    if request.user.is_authenticated:
        try:
            secret = UserSecret.objects.get(user=request.user)
        except UserSecret.DoesNotExist:
            secret = None
        return render(request, 'usersecrets/secret.html', {'usersecret': secret})
    else:
        return redirect('accounts:login')
