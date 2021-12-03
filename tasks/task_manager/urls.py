from django.urls import path
from . import views
urlpatterns =[
    path('addtask/',views.CreateTask,name="add_task"),
    path('view_task/',views.ViewTask,name="view_task"),
    path('view_task/<slug:slug>',views.DetailedTasksView,name="product_view"),
]