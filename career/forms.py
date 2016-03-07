from django import forms
from career.models import UserProfile, JobOffer, Application
from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#


class Html5DateInput(forms.DateInput):
    input_type = 'date'


class UserProfileFormStudent(forms.ModelForm):
    #self.fields['issuer'].queryset = Issuer.all(user)
    # def __init__(self,user,*args,**kwargs):
    #     super(UserProfileForm,self).__init__(*args,**kwargs)
    #     self.fields['user'] = user

    #email = forms.EmailField(max_length=70, help_text="Email: ")
    student_surname = forms.CharField(max_length=15, help_text='Surname: ')
    student_name = forms.CharField(max_length=15, help_text='Name: ')
    student_dateOfBirth = forms.DateField(help_text='Date of birth: ', widget=Html5DateInput())

    STUDY_CHOICES = (
    (u'B', u'Business Administration'),
    (u'A', u'Architecture'),
    (u'E', u'Entrepreneurship'),
    (u'F', u'Finance'),
    (u'I', u'Information Systems'),
    )
    student_studyProgram = forms.ChoiceField(choices=STUDY_CHOICES, help_text='Study Program: ')

    DEGREE_CHOICES = (
    (u'B', u'BSc'),
    (u'M', u'MSc'),
    )
    student_degree \
        = forms.ChoiceField(choices=DEGREE_CHOICES, help_text='Degree: ')

    phone_number = forms.CharField(max_length=20, help_text="Phone number: ")


    class Meta:
        model = UserProfile
        #exclude = ('user', 'picture', 'email', 'last_visited_jo','user_type', 'company_name', 'business_sector', 'contact_person', 'link_to_website')
        fields = ('student_surname','student_name', 'phone_number', 'student_dateOfBirth', 'student_studyProgram', 'student_degree')
        #widgets = {
            #'student_dateOfBirth': Html5DateInput()}


class UserProfileFormCompany(forms.ModelForm):

    # def __init__(self,logged_user,*args,**kwargs):
    #     user = forms.ModelChoiceField(queryset=User.objects.all())
    #     super(UserProfileFormCompany,self).__init__(*args,**kwargs)
    #     self.fields['user'].queryset = User.objects.filter(account=logged_user)

    #self.fields['user'].queryset = UserProfile.all()
    company_name = forms.CharField(max_length=15, help_text='Company Name: ')
    business_sector = forms.CharField(max_length=15, help_text='Business Sector: ')
    contact_person = forms.CharField(max_length=15, help_text='Contact Person: ')
    link_to_website = forms.URLField(help_text='Website: ')

    phone_number = forms.CharField(max_length=20, help_text="Phone number: ")

    class Meta:
        model = UserProfile
        exclude = ('user', 'picture', 'student_surname', 'student_name', 'student_dateOfBirth', 'email', 'phone_number', 'student_studyProgram', 'student_degree', 'last_visited_jo', 'user_type')
        #fields = ('user','email', 'phone_number', 'user_type')


class UserTypeForm(forms.ModelForm):
    USER_CHOICES = (
    (u's', u'Student'),
    (u'c', u'Company'),
    )
    #user_type = forms.ChoiceField(choices=USER_CHOICES, help_text="Choose User: ")
    class Meta:
        model = UserProfile
        #exclude = ('user', 'picture', 'student_surname', 'student_name', 'student_dateOfBirth', 'email', 'phone_number', 'student_studyProgram', 'student_degree', 'last_visited_jo')
        fields = ('user_type',)


class JobOfferForm(forms.ModelForm):
    title = forms.CharField(max_length=70, help_text="Please enter the title of the job offer.")
    #company = forms.CharField(max_length=70, help_text="Company: ")
    position = forms.CharField(max_length=70, help_text="Position:")

    location = forms.CharField(max_length=70, help_text="Location:")
    workloadPercentage = forms.IntegerField(help_text="Workload percentage:") #create min and max restricitons
    expectations = forms.CharField(max_length=500, help_text="Expectations:", widget=forms.Textarea)
    requirements = forms.CharField(max_length=500, help_text="Requirements:", widget=forms.Textarea)

    pdf_file = forms.FileField(
        label='Select a file',
        help_text='Upload Job Offer (PDF)')

    class Meta:
        model = JobOffer
        fields = ('title', 'position', 'location', 'workloadPercentage', 'expectations', 'requirements', 'pdf_file')
        widgets = {
            'expectations': forms.Textarea(),
            'requirements': forms.Textarea()}


class ApplicationForm(forms.ModelForm):
    message = forms.CharField(max_length=500, help_text="Message: ", widget=forms.Textarea)
    motivation_letter = forms.FileField(
        label='Select a file',
        help_text='Upload Motivation Letter (PDF)')

    class Meta:
        model = Application
        exclude = ('receiver', 'sender', 'job_offer')








