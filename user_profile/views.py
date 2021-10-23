from django.shortcuts import render


def user_profile(request):
    """ displaying users profile """

    template = 'user_profile/user_profile.html'
    context = {}

    return render(request, template, context)
