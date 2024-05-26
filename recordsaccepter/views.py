from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Records
# Create your views here.
def home(request):
    if request.method == "POST":
        form = Records(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('thanks')
    else:
        form = Records()
    return render(request, 'inputrecords.html', {"form": form})

def thanks(request):
    return HttpResponse("your record is saved")