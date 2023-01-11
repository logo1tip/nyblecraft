from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', WorkerList.as_view(), name='home'),
    path('worker/<int:pk>/', DetailWorker.as_view(), name='worker'),
    path('worker/add-worker', CreateWorker.as_view(), name='add_worker'),
]