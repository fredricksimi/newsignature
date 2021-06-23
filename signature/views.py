from django.shortcuts import render, redirect
from .models import SignatureTool
# from users.models import CustomUser
from django.contrib import messages
# from .forms import UserDetailsForm, UserImageForm
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    user_id = request.user.id
    sigtool = SignatureTool.objects.get(user_id=request.user.id)
    readonlyvar = ''

    if sigtool.full_name != '':
        readonlyvar = 'readonly'

    if request.method == 'POST':
        full_name = request.POST['full_name']
        company = request.POST['company']
        designation = request.POST['designation']
        department = request.POST['department']
        phone = request.POST['phone']
        email = request.POST['email']
        website = request.POST['website']

        # socials
        facebook = request.POST['Facebook']
        linkedin = request.POST['LinkedIn']
        twitter = request.POST['Twitter']
        github = request.POST['GitHub']
        instagram = request.POST['Instagram']
        whatsapp = request.POST['WhatsApp']
        youtube = request.POST['YouTube']
        personalimage = request.POST['PersonalImage']

        sigtool.full_name = full_name
        sigtool.company = company
        sigtool.designation = designation
        sigtool.department = department
        sigtool.phone = phone
        sigtool.email = email
        sigtool.website = website
        sigtool.personalimage = personalimage
        sigtool.facebook = facebook
        sigtool.linkedin = linkedin
        sigtool.twitter = twitter
        sigtool.github = github
        sigtool.instagram = instagram
        sigtool.whatsapp = whatsapp
        sigtool.youtube = youtube
        sigtool.save()
        messages.success(request, 'Your profile was updated successfully!')
        return redirect('signature:home')
    context = {
        'sigtool':sigtool,
        'readonlyvar':readonlyvar
    }
    return render(request, 'signature/index.html', context)

# @login_required
# def simple_upload(request):
#     sigtool = SignatureTool.objects.get(user_id=request.user.id)
#     if request.method == 'POST' and 'userimage' in request.FILES:
#         image = request.FILES['userimage']
#         sigtool.image = image
#         sigtool.save()
#         return redirect('signature:home')
#     return render(request, 'signature/index.html')