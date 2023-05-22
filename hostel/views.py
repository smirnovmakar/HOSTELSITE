from django.shortcuts import render, redirect
from .models import User, Rooms
from .forms import UserForm


def glavn(request):
    return render(request, 'hostel/Главная.html')


def vhod(request):
    allusers = User.objects.all()
    if request.method == 'POST':
        for el in allusers:
            if el.user_name == request.POST.get('user_name') and el.password == request.POST.get('password'):
                return redirect('/bron')

    form = UserForm()
    return render(request, 'hostel/Вход.html', {"allusers": allusers, "form": form})


def reg(request):
    allusers = User.objects.all()
    message = None

    if request.method == 'POST':
        email = request.POST.get('email')
        if allusers.filter(email=email).exists():
            message = "Пользователь с таким логином уже существует!"
        else:
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                message = "Регистрация прошла успешно!!"

    form = UserForm()
    return render(request, 'hostel/Регистрация.html', {"allusers": allusers, "form": form, "message": message})


def bron(request):
    allrooms = Rooms.objects.all()
    return render(request, 'hostel/Бронирование.html', {'allrooms': allrooms})


def rooms(request, roomid):
    today_room_is_free = True
    tomorrow_room_is_free = True
    allrooms = Rooms.objects.all()
    for el in allrooms:
        if el.number == str(roomid):
            if el.today_status != "СВОБОДЕН":
                today_room_is_free = False
            if el.tomorrow_status != "СВОБОДЕН":
                tomorrow_room_is_free = False
        if request.method == "POST":
            if "today" in request.POST:
                el = Rooms.objects.get(number=str(roomid))
                el.today_status = "ЗАНЯТ"
            if "tomorrow" in request.POST:
                el = Rooms.objects.get(number=str(roomid))
                el.tomorrow_status = "ЗАНЯТ"
            el.save()
            return redirect(request.path)
    return render(request, f'hostel/room{roomid}.html', {'today_room_is_free': today_room_is_free,
                                                         'tomorrow_room_is_free': tomorrow_room_is_free,
                                                         'roomid': roomid})

def nomera(request):
    return render(request, 'hostel/Номера.html')