from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# class Category(models.Model):
#     name = models.CharField(max_length=128, unique=True)
#     slug = models.SlugField(unique=True)
#
#     def __unicode__(self):  # For Python 2, use __str__ on Python 3
#         return self.name
#
#     def save(self, *args, **kwargs):
#             self.slug = slugify(self.name)
#             super(Category, self).save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    email = models.EmailField(max_length=70, null= True, unique= True, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    phone_number = models.CharField(max_length=12, blank=True, default=0000000, null=True)
    #address =

    USER_CHOICES = (
    (u's', u'Student'),
    (u'c', u'Company'),
    )
    user_type = models.CharField(max_length=1, choices=USER_CHOICES, null=True)
    #
    # is_student = models.BooleanField(default=True)
    # is_corporate = models.BooleanField(default=False)
    #
    # STUDENT PROPERTIES!!!
    student_surname = models.CharField(max_length=15, blank=True, null=True)
    student_name = models.CharField(max_length=15, blank=True, null=True)
    student_dateOfBirth = models.DateField(null=True, blank=True)
    #
    STUDY_CHOICES = (
    (u'B', u'Business Administration'),
    (u'A', u'Architecture'),
    (u'E', u'Entrepreneurship'),
    (u'F', u'Finance'),
    (u'I', u'Information Systems'),
    )
    student_studyProgram = models.CharField(max_length=1, choices=STUDY_CHOICES, null=True, blank=True)

    DEGREE_CHOICES = (
    (u'B', u'BSc'),
    (u'M', u'MSc'),
    )
    student_degree= models.CharField(max_length=1, choices=DEGREE_CHOICES, null=True, blank=True)
    # Override the __unicode__() method to return out something meaningful!


    #COMPANY Properties!!:
    company_name = models.CharField(max_length=15, blank=True, null=True)
    business_sector = models.CharField(max_length=15, blank=True, null=True)
    contact_person = models.CharField(max_length=15, blank=True, null=True)
    link_to_website = models.URLField(blank=True, null=True)

    last_visited_jo = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.user.username



class JobOffer(models.Model):
    title = models.CharField(max_length=70)
    company = models.CharField(max_length=70)
    position = models.CharField(max_length=70)

    location = models.CharField(max_length=70)
    workloadPercentage = models.IntegerField(default=100) #create min and max restricitons
    expectations = models.CharField(max_length=500)
    requirements = models.CharField(max_length=500)
    pdf_file = models.FileField(upload_to="job_offer_pdf/")

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.title


class Application(models.Model):
    #sender = models.OneToOneField(UserProfile, related_name="sender")
    sender = models.EmailField(max_length=70)
    #receiver = models.OneToOneField(UserProfile, related_name="receiver")
    receiver = models.EmailField(max_length=70)
    job_offer = models.CharField(max_length=70)
    message = models.CharField(max_length=500, null=True)
    motivation_letter = models.FileField(upload_to="motivation_letter_pdf/")
