from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', list, name='home'),
    path('books/', list, name='books'),
    path('librarians/', list, name='librarians'),
    path('libraries/', list, name='libraries'),

]