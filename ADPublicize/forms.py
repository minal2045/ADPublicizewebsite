from django import forms
from ADPublicize.models import advertiser, publiser, contactus, SavLoc, advRequest
class AdvertiserForm(forms.ModelForm):
    class Meta:
        model = advertiser
        fields = "__all__"

class PubliserForm(forms.ModelForm):
    class Meta:
        model = publiser
        fields = "__all__"

class ContactusForm(forms.ModelForm):
    class Meta:
        model = contactus
        fields = "__all__"

class AddlocationForm(forms.ModelForm):
    class Meta:
        model = SavLoc
        fields = "__all__"

class AdvRequestForm(forms.ModelForm):
    class Meta:
        model = advRequest
        fields = "__all__"