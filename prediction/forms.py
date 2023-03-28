from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class PredictionForm(forms.Form):
    gender_choice = [('male', 'MALE'), ('female', 'FEMALE')]
    fam_choice = [('yes', 'YES'), ('no', 'NO')]
    phy_choice = [('none', 'NONE'), ('less than half an hr', 'Less than half an hour'), ('more than half an hr', 'More than half an hour'),('one hr or more','One hour or more')]
    smoking_choice = [('yes', 'YES'), ('no', 'NO')]
    alcohol_choice = [('yes', 'YES'), ('no', 'NO')]
    med_choice = [('yes', 'YES'), ('no', 'NO')]
    junk_choice = [('occassionally', 'Occassionally'), ('often', 'Often'), ('very often', 'Very Often'), ('always', 'Always')]
    stress_choice = [('not at all', 'Never'), ('sometimes', 'Sometimes'), ('very often', 'Very Often'), ('always', 'Always')]
    bpl_choice = [('high', 'High'), ('normal', 'Normal'),('low','Low')]
    uri_choice = [('not much', 'Not Much'), ('quite often', 'Often')]

    age = forms.IntegerField()
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender_choice)
    family_history = forms.ChoiceField(widget=forms.RadioSelect, choices=fam_choice)
    physical_activity = forms.ChoiceField(widget=forms.RadioSelect, choices=phy_choice)
    bmi = forms.IntegerField()
    smoking = forms.ChoiceField(widget=forms.RadioSelect, choices=smoking_choice)
    alcohol_intake = forms.ChoiceField(widget=forms.RadioSelect, choices=alcohol_choice)
    sleep_hours = forms.IntegerField()
    regular_medicine = forms.ChoiceField(widget=forms.RadioSelect, choices=med_choice)
    junkfood = forms.ChoiceField(widget=forms.RadioSelect, choices=junk_choice)
    stress = forms.ChoiceField(widget=forms.RadioSelect, choices=stress_choice)
    blood_pressure_level = forms.ChoiceField(widget=forms.RadioSelect, choices=bpl_choice)
    pregnancies = forms.IntegerField()
    urination_frequency = forms.ChoiceField(widget=forms.RadioSelect, choices=uri_choice)

    class Meta:
        model = Profile
        field = ['age','gen','fam','phy','bmi','smoking','alc','sleep','med','junk','stress','bpl','preg','uri']

class DietForm(forms.Form):
    activity_choice = [('little', 'Little'), ('light', 'Light'),('moderate', 'Moderate'), ('hard', 'Hard'),('very hard','Very Hard')]

    height = forms.IntegerField()
    weight = forms.IntegerField()
    activity = forms.ChoiceField(widget=forms.RadioSelect, choices=activity_choice)

    class Meta:
        model = Profile
        field = ['height','weight','activity']