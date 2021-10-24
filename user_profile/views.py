from django.shortcuts import render, get_object_or_404

from .models import Profile


def user_profile(request):
    """ displaying users profile """
    profile = get_object_or_404(Profile, user=request.user)
    template = 'user_profile/user_profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
