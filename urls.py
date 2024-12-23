from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.manage_department), 
    path('department/<int:id>/', views.manage_department),

    path('shifts/', views.manage_shift), 
    path('shifts/<int:id>/', views.manage_shift), 

    path('roles/', views.manage_role), 
    path('role/<int:id>/', views.manage_role), 

    path('attendance/', views.manage_attendance), 
    path('attendance/<int>/', views.manage_attendance), 

    path('staff/', views.manage_staff), 
    path('staff/<int:id>', views.manage_staff), 
]
