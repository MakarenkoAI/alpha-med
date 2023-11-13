from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddRoomForm, FindPatient
from .models import Record, Room
import datetime

def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы вошли в учетную запись.")
            return redirect('home')
        else:
            messages.success(request, 'Вы не зарегистрированы.')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "Вы вышли из учетной записи.")
    return redirect('home')

def search(request):
    return render(request, 'search.html')

def new1(request):
    first_name = request.GET['first_name']
    last_name = request.GET['last_name']
    records = Record.objects.filter(first_name=first_name,last_name = last_name)
    #records = Record.objects.all()
    return render(request, 'new1.html', {'records': records,'first_name': first_name, 'last_name':last_name})

def new2(request):
    data = request.GET['data']
    records = Record.objects.filter(data__gte=data)
    #records = Record.objects.all()
    return render(request, 'new2.html', {'records': records,'data': data})

def new3(request):
    age = request.GET['age']
    male = request.GET['male']
    diff = Record.age(age)
    records = Record.objects.filter(male=male,databirth__lte=diff)
    return render(request, 'new3.html', {'records': records,'age': age, 'male':male})

def register_user(request):
	if request.method == 'POST': 
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Вы зарегистрированы.")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})
	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
         customer_record = Record.objects.get(id=pk)
         return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'Вы не зарегистрированы.')
        return redirect('home')
    
def delete_record(request, pk):
     if request.user.is_authenticated: 
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Запись удалена.")
        return redirect('home')  
     else:
        messages.success(request, 'Вы не зарегистрированы.')
        return redirect('home')  
     
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Запись добавлена.")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Вы должны зайти в учетную запись.")
		return redirect('home')
      

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись изменена.")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "Войдите в учетную запись.")
        return redirect('home')

def room(request):
    rooms = Room.objects.all()
    if request.user.is_authenticated:
         return render(request, 'room.html', {'rooms':rooms})
    else:
        messages.success(request, 'Вы не зарегистрированы.')
        return redirect('home')
     
def one_room(request, pk):
    if request.user.is_authenticated:
         room = Room.objects.get(id=pk)
         return render(request, 'one_room.html', {'room':room})
    else:
        messages.success(request, 'Вы не зарегистрированы.')
        return redirect('home')
    
def delete_room(request, pk):
     if request.user.is_authenticated: 
        delete_it = Room.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Запись удалена.")
        return redirect('room')  
     else:
        messages.success(request, 'Вы не зарегистрированы.')
        return redirect('home')  
     
def add_room(request):
	form = AddRoomForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_room = form.save()
				messages.success(request, "Запись добавлена.")
				return redirect('room')
		return render(request, 'add_room.html', {'form':form})
	else:
		messages.success(request, "Вы должны зайти в учетную запись.")
		return redirect('room')
      
def update_room(request, pk):
    if request.user.is_authenticated:
        current_room = Room.objects.get(id=pk)
        form = AddRoomForm(request.POST or None, instance=current_room)
        if form.is_valid():
            form.save()
            messages.success(request, "Запись изменена.")
            return redirect('room')
        return render(request, 'update_room.html', {'form':form})
    else:
        messages.success(request, "Войдите в учетную запись.")
        return redirect('home')
    
