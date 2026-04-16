from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', include('kanban.urls')),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', include('portal.urls')),
    path('portal', include('portal.urls'))
    # path('authentication', include('authentication.urls'))
    # path('kanban', include('kanban.urls'))
]