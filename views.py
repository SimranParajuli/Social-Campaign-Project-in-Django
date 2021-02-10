from django.shortcuts import render
from django.http import HttpResponse
from .forms import CampaignForm
from .forms import DonateForm
from webapp.models import Campaign
from .forms import ContactForm




def home(request):
    return render(request,'webapp/home.html',context={'campaign':Campaign.objects.all})


def campaign(request):
    if request.method == 'POST':
        campaign_form = CampaignForm(request.POST)
        if campaign_form.is_valid():
            campaign_form.save()
            return render(request,'webapp/home.html')
    else:
        campaign_form = CampaignForm()
        return render(request, 'webapp/campaign.html', {'form': campaign_form})

def donate(request):
    if request.method == 'POST':
        donate_form = DonateForm(request.POST)
        if donate_form.is_valid():
            donate_form.save()
            return HttpResponse('saved')
    else:
        donate_form = DonateForm()
        return render(request, 'webapp/donate.html', {'form': donate_form})

def contact(request):
    contact_form = ContactForm()
    return render(request,'webapp/contact.html', {'form': contact_form})

def index(request):
    return render(request,'webapp/index.html')

def about(request):
    return render(request,'webapp/about.html')


