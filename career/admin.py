from django.contrib import admin
from career.models import UserProfile, JobOffer, Application#, Students, Corporates
#superuser: career_admin  PW: admin


#class CategoryAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug':('name',)}

#admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
admin.site.register(JobOffer)
admin.site.register(Application)