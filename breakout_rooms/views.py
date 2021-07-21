from django.shortcuts import render, redirect, reverse
from .models import BreakoutRoom, Participant
from .forms import BreakoutRoomForm, ParticipantForm

def list_rooms(request):
    rooms = BreakoutRoom.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, "breakout_rooms/list_rooms.html", context)

def room_detail(request, room_id):
    room = BreakoutRoom.objects.get(pk=room_id)
    context = {
        "room": room
    }
    return render(request, "breakout_rooms/room_detail.html", context)

def new_room(request):
    if request.method == "POST":
        form = BreakoutRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_rooms"))
    if request.method == "GET":
        form = BreakoutRoomForm()
        return render(request, "breakout_rooms/new_room.html", {"form": form})

def update_room(request, room_id):
    obj = BreakoutRoom.objects.get(pk=room_id)
    if request.method == "POST":
        form = BreakoutRoomForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_rooms"))
    if request.method == "GET":
        form = BreakoutRoomForm(instance=obj)
        return render(request, "breakout_rooms/update_room.html", {'form': form})

def delete_room(request, room_id):
    obj = BreakoutRoom.objects.get(pk=room_id)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse("list_rooms"))
    if request.method == "GET":
        return render(request, "breakout_rooms/delete_room.html", {"name": obj.topic})

def list_participants(request, room_id):
    participants = Participant.objects.filter(breakout_room__id=room_id)
    context = {
        "participants": participants
    }
    return render(request, "breakout_rooms/list_participants.html", context)

def participant_detail(request, room_id, participant_id):
    participant = Participant.objects.get(pk=participant_id)
    context = {
        "participant": participant
    }
    return render(request, "breakout_rooms/detail_participant.html", context)

def new_participant(request, room_id):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('list_participants', kwargs={"room_id":room_id}))
    if request.method == "GET":
        form = ParticipantForm()
        return render(request, "breakout_rooms/new_participant.html", {'form': form})
