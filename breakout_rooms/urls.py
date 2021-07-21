from typing import List
from django.urls import path
from .views import *

# CRUD 
# Create
# Read 
    # - List
    # - Detail
# Update 
# Delete 


urlpatterns = [
    path('', list_rooms, name="list_rooms"),
    path('<int:room_id>/', room_detail, name="room_detail"),
    path('new/', new_room, name="new_room"),
    path('<int:room_id>/update/', update_room, name="update_room"),
    path('<int:room_id>/delete/', delete_room, name="delete_room"),

    path('<int:room_id>/participants/', list_participants, name="list_participants"),
    path('<int:room_id>/participants/<int:participant_id>/', participant_detail, name="participant_detail"),
    path('<int:room_id>/participants/new/', new_participant, name="new_participant"),

]