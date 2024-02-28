from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.hello_world,name="hello_world"),
    path('livre',views.ADD_LIVRE,name="add_get_all_livres"),
    path('livre/<int:id>/',views.LIVRE_CRUD,name="delete_get"),
    path('livre/<int:id_livre>/<int:id_user>/',views.EMPREINT,name="empreinter")
]