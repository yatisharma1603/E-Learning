from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import CourseListView
from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static

from . import views

#from ..courses.views import AssignmentModuleUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    # path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('course/', include('courses.urls')),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('', HomePageView.as_view(), name='home'),
    path('students/', include('students.urls')),
    path('accounts/', include("allauth.urls")),
    path('accounts/', include("allauth.urls")),


    #path('courses/', AssignmentModuleUpdateView.as_view(), name='class_assignment'),

    #path('assignment_list/',views.assignment_list,name="assignment_list"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)