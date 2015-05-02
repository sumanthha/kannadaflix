from django.conf.urls import url
from loan import views
urlpatterns = [
    
    url(r'view_loans/$', "loan.views.list_loans"),
    url(r'apply_loan/$', "loan.views.apply_loan"),
    
]
