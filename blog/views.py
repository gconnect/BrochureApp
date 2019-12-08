from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.utils import timezone
from .models import Blog, Course, Event


def index(request):
    latest_blog_list = Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:4:]
    course_list = Course.objects.all()[:4]
    event_list = Event.objects.all()[:4]
    context = {'latest_blog_list': latest_blog_list, 'course_list': course_list, 'event_list': event_list}
    return render(request, 'brochure/home.html', context)


class BlogList(generic.ListView):
    template_name = 'brochure/all_blog.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        return Blog.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'brochure/detail.html'
    slug_field = 'title'
    slug_url_kwarg = 'title'


class CourseList(generic.ListView):
    template_name = 'brochure/course.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.all()[:4:]


class EventList(generic.ListView):
    template_name = 'brochure/event_list.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.all()[:4:]

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'brochure/event_detail.html'