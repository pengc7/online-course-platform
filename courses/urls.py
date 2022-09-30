from django.urls import path,include

from . import views #import views file from the same folder

from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses',views.CourseView)

urlpatterns = [
    path('api', include(router.urls)),
    path('', views.index,name="index"),
    path('<int:course_id>', views.detail,name="detail"),
]
