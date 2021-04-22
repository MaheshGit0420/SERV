from django.urls import path, include
from . import views

urlpatterns = [
    path('list_events/', views.list_events, name="list_events"),
    path('register/<int:eve_id>', views.register_view, name="register_view"),
    # path('leaders/', views.leaders_view, name="leaders_view"),
]
