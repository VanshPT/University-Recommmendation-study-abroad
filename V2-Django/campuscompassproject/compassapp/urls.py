from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path('video_detail/<int:video_id>/', views.video_detail, name='video_detail'),

    path("upload_files/",   views.upload_files,     name="upload_files"),
    path('upload_success/', views.upload_success,   name='upload_success'),

    # path('get_video/<int:video_id>/',      views.download_video,   name='download_video'),
    # path('get_subtitle/<int:video_id>/',   views.download_subtitle, name='download_subtitle'),


    # path("business", views.business, name="Business"),
    # path("about/", views.about, name="AboutUs"),
    # path("contact/", views.contact, name="ContactUs"),
    # # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),

]