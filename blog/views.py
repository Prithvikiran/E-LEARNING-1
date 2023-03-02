from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Room,Topic,Message
from base.models import User
from .forms import RoomForm,UserForm,MyUserCreationForm

# rooms = [
#     {'id':1,'name':'Let\'s learn DSP'},
#     {'id':2,'name':'Ethical Hackers!'},
#     {'id':3,'name':'Codedamn!!!'},
# ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q)
        )
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms,'topics':topics,'room_count':room_count,'room_messages':room_messages}
    return render(request,'blog/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    participants = room.participants.all()
    room_message = room.message_set.all().order_by('-created')
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('blogs',pk=room.id)

    context = {'room':room,'room_message':room_message,'participants':participants}
    return render(request,'blog/rooms.html',context)

def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        user = request.user
        user.points+=100

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
        )
        return redirect('HomePage')

        # form = RoomForm(request.POST)
        # if form.is_valid():
        #   room = form.save(commit=False)
        #   room.host = request.user
        #   room.save()
        #   return redirect('Home')
    context = {'form':form,'topics':topics}
    return render(request,'blog/room_form.html',context)

def profilePage(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    room_topics = Topic.objects.all()
    context = {'user': user,'rooms':rooms,'room_messages':room_messages,'room_topics':room_topics}
    return render(request,'blog/profile.html',context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(data=request.POST, files=request.FILES,instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic,created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('HomePage')
    context = {'form':form,'topics':topics,'room':room}
    return render(request,'blog/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if(request.user != room.host):
        return HttpResponse('You are not allowed here!')
    if request.method == 'POST':
       room.delete()
       return redirect('HomePage')
    return render(request,'blog/delete_room.html',{'obj':room})


def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)
    if(request.user != message.user):
        return HttpResponse('You are not allowed here!')
    if request.method == 'POST':
       message.delete()
       return redirect('blogs',pk=message.room.id)
    return render(request,'blog/delete_room.html',{'obj':message})


def editUser(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
           form.save()
           return redirect('profile-blog',pk=user.id)
    return render(request,'blog/update-user.html',{'form':form,'user':user})