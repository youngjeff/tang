from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from rango import views
from registration.backends.simple.views import RegistrationView


class MyRegistionView(RegistrationView):
    def get_success_url(self, user):
        return url('register_profile')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^rango/', include('rango.urls')),
    url(r'^account/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', MyRegistionView.as_view(),
        name='registration_register'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),

]
