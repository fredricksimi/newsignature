from django.shortcuts import render
from .models import SignatureTool
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'signature/index.html')
