from django.shortcuts import render, redirect
from .models import JobPosting
from .choices import Category_choices, Required_education_choices, Employement_type_choice, Required_experience_choices
from .forms import JobPostingForm

# Create your views here.


def job_list_view(request):
    jobs = JobPosting.objects.filter(user=request.user, active=True)
    template_name = 'jobs/job_list.html'
    context = {'jobs':jobs}
    return render(request, template_name, context)

def job_add_view(request, pk=None):
    if request.method == 'POST':
        title = request.POST['title']
        department = request.POST['department']
        # description = request.POST['description']
        # requirements = request.POST['requirements']
        country = request.POST['country']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        is_remote = request.POST['is_remote']
        employement = request.POST['employement']
        category = request.POST['category']
        education = request.POST['education']
        experience = request.POST['experience']
        lower_hour = request.POST['lower_hour']
        upper_hour = request.POST['upper_hour']
        publish_date = request.POST['publish_date']
        close_date = request.POST['close_date']
        if pk:
            job = JobPosting.objects.get(pk=pk, user=request.user)
            job.update(job_title=title, job_department=department, job_country=country, job_state=state, job_zip_code=zip_code,
                       is_remote=is_remote, job_employment_type=int(employement), job_category=int(category),
                       job_required_education=int(education), job_required_experience=int(experience),
                       job_lower_hours_per_week=int(lower_hour), job_upper_hours_per_week=int(upper_hour),
                       job_publish_date=publish_date, job_close_date=close_date)
        else:
            job = JobPosting.objects.create(user=request.user, job_title=title, job_department=department,
                                            job_country=country, job_state=state, job_zip_code=zip_code,
                                            is_remote=is_remote, job_employment_type=int(employement), 
                                            job_category=int(category), job_required_education=int(education), 
                                            job_required_experience=int(experience), job_lower_hours_per_week=int(lower_hour),
                                            job_upper_hours_per_week=int(upper_hour), job_publish_date=publish_date, 
                                            job_close_date=close_date)
        job.save()
        form = JobPostingForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
        return redirect('/job-list')
    else:
        template_name = 'jobs/job_add.html'
        context = {
            'form':JobPostingForm(),
            'category_choices': Category_choices,
            'education_choices': Required_education_choices,
            'employement_choice': Employement_type_choice,
            'experience_choices': Required_experience_choices
        }
        return render(request, template_name, context)


def delete_job_view(request,pk):
    delete_job = JobPosting.objects.get(pk=pk)
    delete_job.active = False
    delete_job.save()
    return render('/job-list')


    
