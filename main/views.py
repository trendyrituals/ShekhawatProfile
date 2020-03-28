from django.shortcuts import render
from .models import Profile
# Create your views here.
def home(request):
	info = Profile.objects.get(name='Bhawani Singh Shekhawat')
	context = {
		'img': info.img,
		'bio': info.bio,
		'name': info.name
	}
	return render(request,'home.html',context)
