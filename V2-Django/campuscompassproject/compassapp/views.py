#  i have created this file - GTA
# from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# from .models import Product, Contact
# import random

from django.contrib.auth import authenticate, login, logout, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# from .models import Videos


# media_full_path = settings.MEDIA_ROOT + "\playapp_data"
media_full_path = settings.STATIC_MEDIA_ROOT + "\\static\\compassapp\\uploaded_files"


def index(request):
    # return HttpResponse('Playtube    |      Index Page')

    # Retrieve all Videos objects, ordered by upload_date in descending order
    # videos = Videos.objects.all().order_by('-upload_date')
    # recent_video = Videos.objects.all().order_by('-upload_date').first()

    # Print the titles of videos to the terminal
    # for video in videos:
    #     print(video.title)

    # playVideoDetails = {
    #     'v_id' : recent_video.v_id,
    #     'title' : recent_video.title,
    #     'v_path' : "\\playapp\\uploaded_files\\"      + str(recent_video.v_path),
    #     'sub_path' : "\\playapp\\uploaded_files\\"    + str(recent_video.sub_path),
    #     'upload_date' : recent_video.upload_date,

    # }

    # Render the list of videos in a template (optional)
    # return render(request, 'compassapp/index.html', {'playvideo': "playVideoDetails", 'allvideos': "videos"})
    return render(request, 'compassapp/index.html')  # Create an HTML file for your upload form

# def video_detail(request, video_id):
#     # Retrieve video from the database using the video_id
#     video = get_object_or_404(Videos, v_id=video_id)
#     allvideos = Videos.objects.all().order_by('-upload_date')


#     # Print video details to the terminal
#     # print(f"Video Title: {video.title}")
#     # print(f"Video Path: {video.v_path}")
#     # print(f"Subtitle Path: {video.sub_path}")
#     # print(f"Upload Date: {video.upload_date}")

#     playVideoDetails = {
#         'v_id' : video.v_id,
#         'title' : video.title,
#         'v_path' : "\\playapp\\uploaded_files\\"      + str(video.v_path),
#         'sub_path' : "\\playapp\\uploaded_files\\"    + str(video.sub_path),
#         'upload_date' : video.upload_date,

#     }
    

#     # Render the video details in a template
#     return render(request, 'playapp/index.html', 
#                   {'playvideo': playVideoDetails, 'media_full_path': media_full_path,  'allvideos' : allvideos})



# def download_video(request, video_id):
#     video = get_object_or_404(Videos, v_id=video_id)
#     file_path = media_full_path + "\\" + video.v_path
#     print("api download - video file_path: ", file_path)
    
#     with open(file_path, 'rb') as file:
#         response = HttpResponse(file.read(), content_type='video/mp4')
#         response['Content-Disposition'] = 'attachment; filename="video.mp4"'
#         return response

# def download_subtitle(request, video_id):
#     video = get_object_or_404(Videos, v_id=video_id)

#     file_path = media_full_path + "\\" + video.sub_path
#     print("api download - subtitle file_path: ", file_path)

#     with open(file_path, 'rb') as file:
#         response = HttpResponse(file.read(), content_type='text/plain')
#         response['Content-Disposition'] = 'attachment; filename="video_subtitle.vtt"'
#         return response



def upload_success(request):
    return render(request, 'compassapp/index.html')  # Create an HTML file for your upload form
    # return HttpResponse('Playtube    |      upload_success Page')

def upload_files(request):
    if request.method == 'POST':

        print("form post working : ")

        # Handle video file upload
        video_file = request.FILES['video_file']
        # print("settings.MEDIA_ROOT : ",media_full_path)
        fs = FileSystemStorage(location=media_full_path)
        print("fs : ", fs)
        video_path = fs.save(video_file.name, video_file)
        print("video_path : ", media_full_path + "\\" + video_path)

        # Handle subtitle file upload
        subtitle_file = request.FILES['subtitle_file']
        subtitle_path = fs.save(subtitle_file.name, subtitle_file)
        print("subtitle_path : ", media_full_path + "\\" + subtitle_path)

        # Save information to the database
        # video = Videos(title=request.POST['title'], v_path=video_path, sub_path=subtitle_path)
        # video.save()

        # return redirect('upload_success')  # You can redirect to a success page or any other page
        return redirect('index')  # You can redirect to a success page or any other page

    return render(request, 'compassapp/upload_video.html')  # Create an HTML file for your upload form



# ------------------------------------------------------------------------------
# Login / Register / Logout

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            # Create a new user
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)
            return redirect('user_login')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None

    return render(request, 'agroapp/register.html',
                  {'error_message': error_message})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('viewNodes')  # Redirect to your dashboard view
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None

    return render(request, 'agroapp/login.html',
                  {'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to your login view






'''
def index(request):
    products = Product.objects.all()

    all_prods = []
    catProds = Product.objects.values('category', 'Product_id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(products)
        all_prods.append([prod, n]) 

    params = {
        'catproducts' : all_prods,
        'allproducts' : products,
              }

    return render(request,'tze/index.html', params)


def business(request):
    # return HttpResponse('Teamzeffort    |      business Page')
    return render(request,'tze/business.html')

def about(request):
    return render(request,'tze/about.html')

def contact(request):
    coreMem = Contact.objects.filter(mem_tag="core")
    teamMem = Contact.objects.filter(mem_tag="team")
    # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

    return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

def productView(request, myslug):
    # Fetch the product using the id
    product = Product.objects.filter(slug=myslug)
    prodCat = product[0].category
    # print(prodCat)
    recproduct = Product.objects.filter(category=prodCat)
    # print(recproduct)

    # randomObjects = random.sample(recproduct, 2)
    randomObjects = random.sample(list(recproduct), 2)


    return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })


# def index(request):
#     return HttpResponse('Teamzeffort    |      index Page')
'''
