from django.urls import path
from . import views
#from django.conf.urls import include

urlpatterns = [
	path('', views.index, name='index'),
	path('blogs/', views.BlogListView.as_view(), name='blogs'),
	path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
	path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
	path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
#	path('blog/<int:pk>/comment/', views.BlogDetailView.as_view(), name='blog-detail'),
]
