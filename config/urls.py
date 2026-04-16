from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='/portal/', permanent=False)),
    path('portal/', include('portal.urls')),
    path('authentication/', include('authentication.urls')),
    # path('kanban', include('kanban.urls')),
]