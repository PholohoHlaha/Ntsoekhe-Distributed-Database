from django.shortcuts import render, redirect
from .models import PatientRecord
from .forms import PatientRecordForm
# Create your views here.
def Northern_records(request):
    patientRecord = PatientRecord.objects.all()
    if request.method == 'POST':
        form = PatientRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PatientRecordForm()
    context = {
        'patientRecords' : patientRecord,
        'form': form
    }
    return render(request, 'Northern_records/Northern_records.html', context)
