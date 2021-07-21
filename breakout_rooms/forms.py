from django import forms
from .models import BreakoutRoom, Participant

class BreakoutRoomForm(forms.ModelForm):
    class Meta:
        model = BreakoutRoom
        fields = "__all__"

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"