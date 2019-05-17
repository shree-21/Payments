from django.shortcuts import render, redirect
from my_app.models import CustomUser
from my_app.forms import SignupForm, SelectValue
from django.db.models.signals import post_save
from notifications.signals import notify
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def my_handler(sender, instance, created, **kwargs):
    notify.send(instance, verb='was saved')

# post_save.connect(my_handler, sender=MyModel)

def selected_tenant(request):
    tenants = CustomUser.objects.all()
    form = SelectValue()

    print("its working!")

    if request.method == 'POST':
        form = SelectValue(data=request.POST)
        s = request.POST.get('drop')
        msg = "Your Payment for next month can be paid from here. no later than after first week. Payment due: $1825"
        print(msg)
        notify_tenant(request, s, msg)
        print(s)
        return redirect('my_app/send.html')

    context = {'tenants': tenants}
    return render(request, 'my_app/tenant_list.html' , context)

def notify_tenant(request, email, msg):
    print("notify")
    user_email = request.POST.get('drop')
    print("still working!!!")
    user = CustomUser.objects.get(email=user_email)
    print(user)
    
    
    n = notify.send(request.user, recipient=user, verb='Notifications: ' + msg)
    print("notifications", n)

def get_notifications(request):
    tenants = CustomUser.objects.all()
    context = {'tenants': tenants}
    return render(request, 'my_app/notifications.html', context)

class RentView(TemplateView):
    template_name = 'my_app/payments.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
 
def charge(request): 
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=5000,
            currency='usd',
            description='Monthly Rent',
            source=request.POST['stripeToken']
        )
        return render(request, 'my_app/charge.html')