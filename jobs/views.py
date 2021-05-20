from django.shortcuts import render, redirect
from .models import JobPosting
from .choices import Category_choices, Required_education_choices, Employement_type_choice, Required_experience_choices
from .forms import JobPostingForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="login")
def job_list_view(request):
    jobs = JobPosting.objects.filter(user=request.user, active=True)
    template_name = 'jobs/job_list.html'
    context = {'jobs': jobs}
    return render(request, template_name, context)


@login_required(login_url="login")
def job_add_view(request):
    pk = None
    if request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title', None)
        department = request.POST.get('department', None)
        # description = request.POST['description']
        # requirements = request.POST['requirements']
        country = request.POST.get('country', None)
        state = request.POST.get('state', None)
        zip_code = request.POST.get('zip_code', None)
        is_remote = request.POST.get('remote', None)
        employment = request.POST.get('employment')
        category = request.POST.get('category', None)
        education = request.POST.get('education', None)
        experience = request.POST.get('experience', None)
        lower_hour = request.POST.get('lower_hour', None)
        upper_hour = request.POST.get('upper_hour', None)
        publish_date = request.POST.get('publish_date', None)
        close_date = request.POST.get('close_date', None)
        if pk:
            job = JobPosting.objects.get(pk=pk, user=request.user)
            job.update(job_title=title, job_department=department, job_country=country, job_state=state, job_zip_code=zip_code,
                       is_remote=is_remote, job_employment_type=int(employment), job_category=int(category),
                       job_required_education=int(education), job_required_experience=int(experience),
                       job_lower_hours_per_week=int(lower_hour), job_upper_hours_per_week=int(upper_hour),
                       job_publish_date=publish_date, job_close_date=close_date)
        else:
            job = JobPosting.objects.create(user=request.user, job_title=title, job_department=department,
                                            job_country=country, job_state=state, job_zip_code=zip_code,
                                            is_remote=bool(int(is_remote)), job_employment_type=int(employment),
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
            'form': JobPostingForm(),
            'category_choices': Category_choices,
            'education_choices': Required_education_choices,
            'employement_choice': Employement_type_choice,
            'experience_choices': Required_experience_choices
        }
        return render(request, template_name, context)


@login_required(login_url="login")
def delete_job_view(request, pk):
    delete_job = JobPosting.objects.get(pk=pk)
    delete_job.active = False
    delete_job.save()
    return render('/job-list')
