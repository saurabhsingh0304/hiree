from django.urls import path
from . import views as v

urlpatterns = [
    path('job-list/', v.job_list_view, name='job_list'),
    path('job-add/', v.job_add_view, name='job_add'),
    path('job-delete/<int:pk>', v.delete_job_view, name='job_delete')
]
