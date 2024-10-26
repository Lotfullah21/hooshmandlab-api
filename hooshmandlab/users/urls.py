from django.urls import path
from .views import CourseList, Course

urlpatterns = [
    path("",CourseList.as_view()),
    path("<int:pk>/",Course.as_view())
]
