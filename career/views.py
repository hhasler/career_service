from django.shortcuts import render
from career.models import JobOffer, UserProfile, User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from career.forms import UserProfileFormStudent, JobOfferForm, ApplicationForm, UserTypeForm, UserProfileFormCompany
from django.core.mail import send_mail


def index(request):
    context_dict = {}
    response = render(request, 'career/index.html', context_dict)
    return response


def about(request):
    response = render(request, 'career/about.html', {})
    return response


def imprint(request):
    response = render(request, 'career/imprint.html', {})
    return response


def disclaimer(request):
    response = render(request, 'career/disclaimer.html', {})
    return response


def privacypolicy(request):
    response = render(request, 'career/privacypolicy.html', {})
    #logged_user = UserProfile.objects.get(user_id=request.user.id)
    #send_mail('Test Email from Django', 'Here is the message.', 'career.service.info.li@gmail.com',
    #[logged_user.email], fail_silently=False)
    logged_user = UserProfile.objects.get(user_id=request.user.id)
    print logged_user.student_name

    return response

def not_a_company(request):
    response = render(request, 'career/not_a_company.html',{})
    return response


def joboffers(request):
    context_dict = {}

    joboffers_list = JobOffer.objects.all()
    context_dict["joboffers"]=joboffers_list

    response = render(request, 'career/joboffers.html', context_dict)
    return response


def joboffer_detail(request, joboffer_id):
    context_dict = {}
    print request.user
    if str(request.user) <> "AnonymousUser":
        logged_user = UserProfile.objects.get(user_id=request.user.id)
        logged_user.last_visited_jo = joboffer_id
        logged_user.save()

    joboffer = JobOffer.objects.get(id=joboffer_id)
    context_dict["joboffer"]=joboffer

    response = render(request, 'career/joboffer_detail.html', context_dict)
    return response


def companies(request):
    context_dict = {}
    company_dict = {}

    companies_list = UserProfile.objects.all().filter(user_type='c').exclude(user_id=0)
    #context_dict["companies"]=companies_list

    for company in companies_list:
        joboffers_list = JobOffer.objects.all().filter(company=company)
        print company.company_name
        print company.link_to_website
        if len(joboffers_list) <> 0:
            company.number = len(joboffers_list)
    context_dict["companies"] = companies_list

    response = render(request, 'career/companies.html', context_dict)
    return response


def students(request):
    context_dict = {}

    student_list = UserProfile.objects.all().filter(user_type='s')
    study_dict = {
        'B': 'Business Administration',
        'A': 'Architecture',
        'E': 'Entrepreneurship',
        'F': 'Finance',
        'I': 'Information Systems',
    }
    degree_dict = {
        'B': 'BSc',
        'M': 'MSc',
    }
    for student in student_list:
        student.student_studyProgram = study_dict[student.student_studyProgram]
        student.student_degree = degree_dict[student.student_degree]
    context_dict["students"] = student_list

    response = render(request, 'career/students.html', context_dict)
    return response


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/career/')

@login_required
def change_user_info(request):
    context_dict = {}
    logged_user = UserProfile.objects.get(user_id=request.user.id)
    print logged_user.user_type
    # is user a student?
    if logged_user.user_type == 's':
        if request.method == 'POST':
            form = UserProfileFormStudent(request.POST, instance=logged_user)

            if form.is_valid():
                # Save the new category to the database.
                change = form.save(commit=True)
                change.save()
                return index(request)
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
        else:
            # If the request was not a POST, display the form to enter details.
            form = UserProfileFormStudent()

    # is user a company?
    if logged_user.user_type == 'c':
        if request.method == 'POST':
            form = UserProfileFormCompany(request.POST, instance=logged_user)

            if form.is_valid():
                # Save the new category to the database.
                change = form.save(commit=True)
                change.save()
                return index(request)
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
        else:
            # If the request was not a POST, display the form to enter details.
            form = UserProfileFormCompany()

    context_dict['form'] = form
    return render(request, 'registration/change_user_info.html', context_dict)

@login_required
def set_user_type(request):
    context_dict = {}
    logged_user = request.user
    if request.method == 'POST':
        form = UserTypeForm(request.POST)

        if form.is_valid():
            change = form.save(commit=True)
            change.user = logged_user
            change.email = logged_user.email
            change.save()
            return HttpResponseRedirect('/career/change_user_info/')
            #return change_user_info(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = UserTypeForm()

    # Render the form with error messages (if any).
    context_dict['form'] = form

    return render(request, 'registration/set_user_type.html', context_dict)



@login_required
def add_joboffer(request):
    logged_user = UserProfile.objects.get(user_id=request.user.id)
    context_dict = dict()
    if logged_user.user_type == 'c':
        if request.method == 'POST':
            form = JobOfferForm(request.POST, request.FILES)
            if form.is_valid():

                new_jo = form.save(commit=True)
                new_jo.company = logged_user.company_name
                new_jo.save()

                return HttpResponseRedirect('/career/joboffers/')
                #return joboffers(request)
            else:
                # The supplied form contained errors - just print them to the terminal.
                print form.errors
        else:
            # If the request was not a POST, display the form to enter details.
            form = JobOfferForm()
            context_dict['company']= logged_user.company_name
        context_dict['form'] = form
        return render(request, 'career/add_joboffer.html', context_dict)

    else:
        return HttpResponseRedirect('/career/not_a_company/')

@login_required
def apply(request):
    logged_user = UserProfile.objects.get(user_id=request.user.id)
    sender = logged_user
    jo_id = logged_user.last_visited_jo
    joboffer = JobOffer.objects.get(id=jo_id)
    receiver = UserProfile.objects.get(company_name=joboffer.company)
    print jo_id
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():

            applic = form.save(commit=True)
            applic.job_offer = joboffer.title
            applic.sender = sender.email
            applic.receiver = receiver.email
            ml_link = 'http://127.0.0.1:8000/media/' + str(applic.motivation_letter)
            applic.save()

            email_message_sender = "Dear "+str(request.user) +",\nYou have applied for the job offer "+ str(joboffer.title) +" of the company "+str(receiver.company_name)+" on Career Service.\n" \
                            "Thank you for using Career Service!\n" \
                            "\n \n "\
                            "This is your Message to the company: \n"+str(applic.message) +"\n\n"+"Motivation letter: "+"\n"+ml_link

            email_message_receiver = "Dear "+str(receiver.company_name)+",\n"+str(sender.student_name)+" "+str(sender.student_surname)+" has applied for the job offer " + str(joboffer.title) +"\n" \
                            "\nMessage: \n"+str(applic.message) +"\n\n"+"Motivation letter: "+"\n"+ml_link

            send_mail('Career Service: New Application', email_message_sender, 'career.service.info.li@gmail.com',
            [applic.sender], fail_silently=False)

            send_mail('Career Service: New Application', email_message_receiver, 'career.service.info.li@gmail.com',[applic.receiver], fail_silently=False)

            #request.user.email


            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ApplicationForm()

    return render(request, 'career/apply.html', {'form': form})