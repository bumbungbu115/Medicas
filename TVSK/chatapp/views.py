from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Room, Message
# Create your views here.

def chatroom(request):
    return render(request, 'chatapp/room.html')

def inbox(request, inbox):
    username=request.GET.get('username')
    chat_details=Room.objects.get(name=inbox)
    return render(request,'chatapp/inbox.html',{
        'username':username,
        'inbox':inbox,
        'chat_details':chat_details
    })

def check(request):
    inbox=request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=inbox).exists():
        return redirect('chatroom/'+inbox+'/?username='+username)
    else:
        new_room = Room.objects.create(name=inbox)
        new_room.save()
        # return redirect('/'+room+'/?username='+username)
        return redirect('chatroom/'+inbox+'/?username='+username)

def send(request):
    username=request.POST['username']
    room_id=request.POST['room_id']
    message=request.POST['message']

    new_message=Message.objects.create(value=message, user=username,room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getmessage(request,inbox):
    chat_details=Room.objects.get(name=inbox)
    message=Message.objects.filter(room=chat_details.id)
    return JsonResponse({"message":list(message.values())})