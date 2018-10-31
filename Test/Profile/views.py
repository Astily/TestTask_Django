from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse

from .forms import CustomUserForm
from .models import CustomUser, IpUsers


def index(request):
    return HttpResponse("You're at the polls index. Section in development")


def profile(request, profile_id):
    try:
        profile = CustomUser.objects.get(pk=profile_id)
    except CustomUser.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'profile/profile.html', {'profile': profile, 'edit': reverse('edit')})


@login_required
def edit_profile(request):
    profile_obj = request.user
    if request.method == "POST":
        form = CustomUserForm(request.POST, instance=profile_obj)
        if form.is_valid():
            post = form.save(commit=False)
            ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
            userIp = IpUsers(user=post, ip=ip)
            userIp.save()

            post.save()
            return redirect('profile', profile_id=profile_obj.pk)
    else:
        form = CustomUserForm(instance=profile_obj)
    return render(request, 'profile/edit.html', {'form': form})


def home(request):
    user = request.user
    if user.is_authenticated:
        return redirect('profile', profile_id=user.pk)
    else:
        return redirect('login')

