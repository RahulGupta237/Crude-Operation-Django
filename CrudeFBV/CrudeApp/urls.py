
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_student,name='Add'),
     path('delet/<int:id>/',views.delete_data,name='Del'),
        path('<int:id>/',views.update_data,name='Update'),
]
