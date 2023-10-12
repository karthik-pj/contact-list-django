from django.shortcuts import render, redirect
from .models import Info

# Create your views here.
def home(request):
    new=Info.objects.all()
    search_input=request.GET.get('search-area')
    if search_input:
        new=Info.objects.filter(name__icontains=search_input)
    else:
        new=Info.objects.all()
        search_input=''
    return render(request, 'index.html', {'new' : new, 'search_input': search_input})
    

def add_details(request):
    if request.method=='POST':
        new_info=Info(
            name=request.POST['name'],
            number=request.POST['number'],
            relationship=request.POST['relationship'],
        )
        new_info.save()
    return render(request, 'add.html')

def profile(request, pk):
    prof=Info.objects.get(id=pk)
    return render(request, 'profile.html', {'prof': prof})

def edit(request,pk):
    prof=Info.objects.get(id=pk)
    
    if request.method=='POST':
        prof.name=request.POST['name']
        prof.relationship=request.POST['relationship']
        prof.number=request.POST['number']
        prof.save()
        
        return redirect('/home',{str(Info.id)})
    return render(request, 'edit.html', {'prof': prof})

def delete(request,pk):
    prof=Info.objects.get(id=pk)
    if request.method=='POST':
        prof.delete()
        redirect('/')
    return render(request, 'delete.html', {'prof': prof})   