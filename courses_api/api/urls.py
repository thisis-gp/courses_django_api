from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.CourseListCreate.as_view(), name='course-list-create'),
    path("courses/<int:pk>/", views.CourseDetailView.as_view(),name="course-detail"),
    path("instances/<int:year>/<int:semester>/",views.CourseInstanceListCreate.as_view(), name="instance-list-create"),
    path('instances/<int:year>/<int:semester>/<int:course_id>/', views.CourseInstanceDetail.as_view(), name="instance-detail"),
]