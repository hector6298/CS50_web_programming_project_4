from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from .models import SkinImages
from .forms import ImageUpload
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from .forms import UserRegistration
from .models import *
from django.views import generic
from django.contrib.auth.decorators import login_required
import os
import requests
import cv2
import numpy as np

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class SignUp(generic.CreateView):
    form_class = UserRegistration
    success_url = reverse_lazy('login')
    template_name = 'register.html'


@login_required(login_url='accounts/login')
def upload_view(request):
    if request.method == 'POST':
        user = request.user
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            image_record = SkinImages()
            image_record.patient_key = user
            image_record.image = form.cleaned_data['image']
            image_record.title = form.cleaned_data['title']
            image_record.save()
            print(os.path.join(BASE_DIR, 'media\\'+request.FILES['image'].name))
            test_image =  cv2.imread(os.path.join(BASE_DIR, 'media/skin_imgs/'+request.FILES['image'].name))
            if test_image is not None:

                test_image = cv2.resize(test_image, (100, 100))
                test_image = test_image.astype('float32')
                test_image /= 255
                print(test_image.shape)

                payload = {
                    'image': test_image.tolist()
                }

                r = requests.post('http://localhost:5000/predict', json=payload)
                if r.status_code != 200:
                    return JsonResponse({'success': False})

                data = r.json()

                print(data['diagnostic'])
                json_data = {
                    'success' : True,
                    'diagnostic' : data['diagnostic'],
                    'image': image_record.image.url
                }
                return JsonResponse(json_data)
                
            else:
                print('image didnt load')
                return JsonResponse({'success': False})
            
            #return HttpResponseRedirect(reverse("home"))

        else:
            print('Failed uploading image')
            return JsonResponse({'success': False})

    context = {
        'form': ImageUpload()
    }
    return render(request, 'post.html', context)


@login_required(login_url='accounts/login')
def home_view(request):
    context = {
        'images' : SkinImages.objects.filter(patient_key=request.user)
    }
    return render(request, 'home.html', context=context)


