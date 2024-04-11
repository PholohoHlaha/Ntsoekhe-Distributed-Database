from django.shortcuts import render, redirect
from .models import Tertiary_center
from .forms import Tertiary_centerForm
# Create your views here.
def Tertiary_centerView(request):
    tertiary_center = Tertiary_center.objects.all()
    if request.method == 'POST':
        form = Tertiary_centerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = Tertiary_centerForm()
    context = {
        'tertiary_centers' : tertiary_center,
        'form': form
    }
    return render(request, 'Tertiary_center/Tertiary_center.html', context)
