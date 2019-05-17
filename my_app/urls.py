from django.conf.urls import url
from my_app import views 

app_name = 'my_app'

urlpatterns = [
    # url(r'^tenants/', views.tenant_list_view, name='tenant_list'),
    # url(r'^notifications/', views.notify_tenant, name='notify'),
    url(r'^sent/', views.selected_tenant, name='tenant_list'),
    url(r'^notifications/', views.get_notifications, name='get_notified'),
    url(r'^payments/', views.RentView.as_view(), name='payment'),
    url(r'^charge/', views.charge, name='charge'),
]