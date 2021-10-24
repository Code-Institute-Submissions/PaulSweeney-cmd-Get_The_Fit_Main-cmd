from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

@login_required
def user_profile(request):
    """ displaying users profile """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        # generating users information, checking validation
        # and returning a success message if everything checks out.
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')

    form = ProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'user_profile/user_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)
