from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Records
# Create your views here.
def home(request):
    if request.method == "POST":
        form = Records(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            id = request.POST.get('id')
            description = request.POST.get('description')
            date = request.POST.get('date')
            return HttpResponseRedirect('/')
    else:
        form = Records()
    return render(request, 'inputrecords.html', {"form": form})