from django.shortcuts import render, get_object_or_404, redirect
from .models import SignatureTool
from users.models import CustomUser
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

        sigtool.full_name = full_name
        sigtool.company = company
        sigtool.designation = designation
        sigtool.department = department
        sigtool.phone = phone
        sigtool.email = email
        sigtool.website = website
        sigtool.facebook = facebook
        sigtool.linkedin = linkedin
        sigtool.twitter = twitter
        sigtool.github = github
        sigtool.instagram = instagram
        sigtool.whatsapp = whatsapp
        sigtool.youtube = youtube
        # user_info = SignatureTool(
        #     user_id = user_id,
        #     full_name = full_name,
        #     company = company,
        #     designation = designation,
        #     department = department,
        #     phone = phone,
        #     email = email,
        #     website = website,
        #     facebook = facebook,
        #     linkedin = linkedin,
        #     twitter = twitter,
        #     github = github,
        #     instagram = instagram,
        #     whatsapp = whatsapp,
        #     youtube = youtube
        # )
        # user_form = UserDetailsForm(request.POST, instance=request.user.signaturetool)
        # if user_form.is_valid():

            # user_form.save()
        # user_info.save(commit=False)
        # user_info.user.id = user.id
        sigtool.save()
        messages.success(request, 'Your profile was updated successfully!')
        return redirect('signature:home')
    # else:
        # user_form = UserDetailsForm()
    context = {
        # 'user_form':user_form,
        'sigtool':sigtool,
        'readonlyvar':readonlyvar
    }
    return render(request, 'signature/index.html', context)

@login_required
def imageview(request):
    user = request.user
    sigtool = SignatureTool.objects.get(user__username=request.user.username)
    readonlyvar = ''

    if sigtool.full_name != '':
        readonlyvar = 'readonly'
    
    if request.method == 'POST':
        imageform = UserImageForm(request.POST, instance=request.user.signaturetool)
        if imageform.is_valid():
            imageform.save()
            messages.success(request, 'Your profile was updated successfully')
            return redirect('signature:home')
        else:
            imageform = UserImageForm()
    context = {
        'imageform':imageform,
        'readonlyvar':readonlyvar
    }
    return render(request, 'signature/index.html', context)
    