from django.urls import path,include
from . import views

app_name = 'blog'
urlpatterns = [
# post views
path('', views.post_list, name='post_list'),
path('<int:year>/<int:month>/<int:day>/<slug:post>/',
     views.post_detail,
     name='post_detail'),
path('blog/',include('blog.urls', namespace='blog'))
]
