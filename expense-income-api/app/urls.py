from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    # api
   
    url(r'^api/profiles/$', views.ProfileList.as_view()), # list of profiles
    url(r'^api/profiles/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()), # single profile
    url(r'^api/users/$', views.UserList.as_view()), # list of users
    url(r'^api/users/create/$', views.UserCreate.as_view()), # create user
    url(r'^api/auth/login/$', views.loginUser.as_view()), # login user
    url(r'^api/auth/logout/$', views.logoutUser.as_view()), # logout user
    url(r'^api/products/$', views.ProductList.as_view(), name="products"),
    url(r'^api/products/<int:pk>/', views.ProductDetail.as_view(), name="products_detail")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
