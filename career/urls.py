from django.conf.urls import patterns, url
from career import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^imprint/$', views.imprint, name='imprint'),
        url(r'^disclaimer/$', views.disclaimer, name='disclaimer'),
        url(r'^privacypolicy/$', views.privacypolicy, name='privacypolicy'),
        url(r'^joboffers/$', views.joboffers, name='joboffers'),
        url(r'^joboffers/(?P<joboffer_id>\d+)/$', views.joboffer_detail, name='joboffer_detail'),
        url(r'^set_user_type/$', views.set_user_type, name='set_user_type'),
        url(r'^change_user_info/$', views.change_user_info, name='change_user_info'),
        url(r'^add_joboffer/$', views.add_joboffer, name='add_joboffer'),
        url(r'^apply/$', views.apply, name='apply'),
        url(r'^not_a_company/$', views.not_a_company, name='not_a_company'),
        url(r'^companies/$', views.companies, name='companies'),
        url(r'^students/$', views.students, name='students'),


)