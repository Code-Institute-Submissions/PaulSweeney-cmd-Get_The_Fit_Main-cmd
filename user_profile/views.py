from django.shortcuts import render, get_object_or_404

from .models import Profile
from .forms import ProfileForm


def user_profile(request):
    """ displaying users profile """
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'user_profile/user_profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
