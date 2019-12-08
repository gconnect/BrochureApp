from django.conf.urls.static import static
from django.urls import path
from .import views
from django.conf import settings

app_name = 'blog'
urlpatterns =[
    path('', views.index, name='home'),
    path('course/', views.CourseList.as_view(), name='course_list'),
    path('event/', views.EventList.as_view(), name='event_list'),
    path('blog/', views.BlogList.as_view(), name='blog_list'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/event/', views.EventDetailView.as_view(), name='event_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)