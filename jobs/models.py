from django.db import models
from process.models import ModelBase
from . import choices as c

# Create your models here.


class JobPosting(ModelBase):
    job_title = models.CharField(max_length=50, null=True, blank=True)
    job_department = models.CharField(max_length=50, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    job_requirements = models.TextField(null=True, blank=True)
    job_country = models.CharField(max_length=50,null=True, blank=True)
    job_state = models.CharField(max_length=50, null=True, blank=True)
    job_zip_code = models.CharField(max_length=10,null=True, blank=True) 
    is_remote = models.BooleanField(default=False)
    job_employment_type = models.IntegerField(choices=c.Employement_type_choice, default=1)
    job_category = models.IntegerField(choices=c.Category_choices, default=1)
    job_required_education = models.IntegerField(choices=c.Required_education_choices, default=1)
    job_required_experience = models.IntegerField(choices=c.Required_experience_choices, default=1)
    job_lower_hours_per_week = models.IntegerField(default=0)
    job_upper_hours_per_week = models.IntegerField(default=0)
    job_publish_date = models.DateField(null=True, blank=True)
    job_close_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.job_title


    
