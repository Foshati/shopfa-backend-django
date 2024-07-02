"""
path('blog/', include('blog.urls'))
"""

from tkinter.font import names
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls", namespace="home")),
]
