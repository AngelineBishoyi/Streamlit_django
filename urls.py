# from django.urls import path
# from .views import MyModelCreateView

# urlpatterns = [
#     path('insert/', MyModelCreateView.as_view(), name='student-list-create'),
#     path('get/', MyModelCreateView.as_view(), name='student-retrieve'),
#     path('update/<int:pk>/', MyModelCreateView.as_view(), name='student-update'),
#     path('delete/<int:pk>/', MyModelCreateView.as_view(), name='student-destroy'),
# ]


# students/urls.py

from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-retrieve-update-destroy'),
]
