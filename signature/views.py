from django.shortcuts import render, get_object_or_404, redirect
from .models import SignatureTool
from users.models import CustomUser
from django.contrib import messages
from .forms import UserDetailsForm
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    user = request.user
    sigtool = SignatureTool.objects.get(user__username=request.user.username)
    readonlyvar = ''

    if sigtool.full_name != '':
        readonlyvar = 'readonly'

    if request.method == 'POST':
        user_form = UserDetailsForm(request.POST, instance=request.user.signaturetool)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('mainapp:home')
    else:
        user_form = UserDetailsForm(instance=request.user.signaturetool)
    context = {
        'user_form':user_form,
        'sigtool':sigtool,
        'readonlyvar':readonlyvar
    }
    return render(request, 'signature/index.html', context)
