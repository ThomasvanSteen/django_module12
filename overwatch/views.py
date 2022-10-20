from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Overwatch
from .forms import OverwatchCreate
from django.http import HttpResponse
#DataFlair
def index(request):
    shelf = Overwatch.objects.all()
    return render(request, 'overwatch/library.html', {'shelf': shelf})
def upload(request):
    upload = OverwatchCreate()
    if request.method == 'POST':
        upload = OverwatchCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
            return render(request, 'overwatch/upload_form.html', {'upload_form':upload})
def update_overwatch(request, overwatch_id):
    overwatch_id = int(overwatch_id)
    try:
        overwatch_sel = Overwatch.objects.get(id = overwatch_id)
    except Overwatch.DoesNotExist:
        return redirect('index')
    overwatch_form = OverwatchCreate(request.POST or None, instance = overwatch_sel)
    if overwatch_form.is_valid():
       overwatch_form.save()
       return redirect('index')
    return render(request, 'overwatch/upload_form.html', {'upload_form':overwatch_form})
def delete_overwatch(request, overwatch_id):
    overwatch_id = int(overwatch_id)
    try:
        overwatch_sel = Overwatch.objects.get(id = overwatch_id)
    except Overwatch.DoesNotExist:
        return redirect('index')
    overwatch_sel.delete()
    return redirect('index')