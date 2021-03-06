from django.core.checks import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.humanize.templatetags.humanize import naturaltime, register
from django.db.models import Q
from django.contrib.auth.models import Group
from .models import User, Message
from Medicas.models import Doctor_Profiles
from django.contrib.humanize.templatetags.humanize import naturaltime
import json

@login_required
def chatroom(request, pk:int):
    # if register.user.groups.filter(name='NguoiDung'):
    otheruser = get_object_or_404(User,pk=pk)
    messages = Message.objects.filter(Q(receiver=request.user, sender=otheruser))
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=otheruser, sender=request.user) )
    users=User.objects.exclude(pk=request.user.pk)
    if request.user.groups.filter(name='NguoiDung'):
        BacSi=Doctor_Profiles.objects.get(name_id=pk)
        return render(request, "chatapp/chat.html", {"otheruser": otheruser, 'users': users, "user_messages": messages, 'BacSi':BacSi })
    else:
        return render(request, "chatapp/chat.html", {"otheruser": otheruser, 'users': users, "user_messages": messages, })

@login_required
def ajax_load_messages(request, pk):
    otheruser = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False, receiver=request.user)
    
    print("messages")
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent": message.sender == request.user,

        "date_created": naturaltime(message.date_created),

    } for message in messages]
    messages.update(seen=True)
    
    if request.method == "POST":
        message = json.loads(request.body)['message']
        
        m = Message.objects.create(receiver=otheruser, sender=request.user, message=message)
        message_list.append({
            "sender": request.user.username,
            "username": request.user.username,
            "message": m.message,
            "date_created": naturaltime(m.date_created),
            "sent": True,
        })
    print(message_list)
    return JsonResponse(message_list, safe=False)

