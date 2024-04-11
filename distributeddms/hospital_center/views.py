from django.shortcuts import render, redirect
from .models import Hospital_center
from .forms import Hospital_centerForm
# Create your views here.
def Hospital_centerView(request):
    hospital_center = Hospital_center.objects.all()
    if request.method == 'POST':
        form = Hospital_centerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = Hospital_centerForm()
    context = {
        'hospital_centers' : hospital_center,
        'form': form
    }
    return render(request, 'hospital_center/hospital_center.html', context)
