from django.shortcuts import redirect, render
from django.http import HttpResponse, request
import pickle
from django.contrib.auth.models import User
from users.models import Profile
from .forms import PredictionForm, DietForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def predict(request):
    us = User.objects.get(username=request.user.username)
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            event = form.save(commit=True)
            event.profile = request.user
            event.save()         
    else:
        form = PredictionForm()        
    return render(request, 'predict.html', {'form':form})

def result(request):
    us = User.objects.get(username=request.user.username)

    age = int(request.POST.get('age'))
    us.profile.age = age

    gender = str(request.POST.get('gender'))
    us.profile.gen = gender
    
    family_history = str(request.POST.get('family_history'))
    us.profile.fam = family_history
        
    physical_activity = str(request.POST.get('physical_activity'))
    us.profile.phy = physical_activity
    
    bmi = int(request.POST.get('bmi'))
    us.profile.bmi = bmi
    
    smoking = str(request.POST.get('smoking'))
    us.profile.smoking = smoking
    
    alcohol = str(request.POST.get('alcohol_intake'))
    us.profile.alc = alcohol
    
    sleep_hours = int(request.POST.get('sleep_hours'))
    us.profile.sleep = sleep_hours
    
    regular_medicine = str(request.POST.get('regular_medicine'))
    us.profile.med = regular_medicine
    
    junkfood = str(request.POST.get('junkfood'))
    us.profile.junk = junkfood
    
    stress = str(request.POST.get('stress'))
    us.profile.stress = stress
    
    blood_pressure_level = str(request.POST.get('blood_pressure_level'))
    us.profile.bpl = blood_pressure_level
    
    pregnancies = int(request.POST.get('pregnancies'))
    us.profile.preg = pregnancies
    
    urination_frequency =str(request.POST.get('urination_frequency'))
    us.profile.uri = urination_frequency
    
    us.profile.save()

    if (age<40):
        age_p = 1
    elif(age>=40 and age<50):
        age_p= 2
    elif(age>=50 and age<60):
        age_p = 3
    else:
        age_p=4

    if (gender=="male"):
        gen_p = 1
    elif(gender=="female"):
        gen_p = 0

    if (family_history=="yes"):
        fam_p = 1
    elif(family_history=="no"):
        fam_p = 0

    if (physical_activity=="none"):
        phy_p = 4
    elif(physical_activity=="less than half an hr"):
        phy_p= 3
    elif(physical_activity=="more than half an hr"):
        phy_p = 2
    elif(physical_activity=="one hr or more"):
        phy_p=1

    if (smoking=="yes"):
        smoking_p = 1
    elif(smoking=="no"):
        smoking_p = 0

    if (alcohol=="yes"):
        alco_p = 1
    elif(alcohol=="no"):
        alco_p = 0

    if (regular_medicine=="yes"):
        med_p = 1
    elif(regular_medicine=="no"):
        med_p = 0

    if (junkfood=="always"):
        junk_p = 4
    elif(junkfood=="very often"):
        junk_p= 3
    elif(junkfood=="often"):
        junk_p = 2
    elif(junkfood=="occassionally"):
        junk_p=1

    if (stress=="always"):
        stress_p = 4
    elif(stress=="very often"):
        stress_p= 3
    elif(stress=="sometimes"):
        stress_p = 2
    elif(stress=="not at all"):
        stress_p=1

    if (blood_pressure_level=="high"):
        bpl_p = 1
    elif(blood_pressure_level=="normal"):
        bpl_p= 2
    elif(blood_pressure_level=="low"):
        bpl_p = 3

    if (urination_frequency=="not much"):
        uri_p = 1
    elif(urination_frequency=="quite often"):
        uri_p= 0

    X_test = [[age_p,gen_p,fam_p,phy_p,bmi,smoking_p,alco_p,sleep_hours,
                med_p,junk_p,stress_p,bpl_p,pregnancies,uri_p]]
    pickle_in = open("H:\softwares\Code_Medical\model\RF.pickle","rb")

    linear = pickle.load(pickle_in)
    prediction = linear.predict(X_test)

    ret = ""

    if(prediction==1):
        ret = "positive"

    else:
        ret = "negative"

    context = {'age' : age,'gender' : gender,'family_history' : family_history,
    'physical_activity' : physical_activity,'bmi' : bmi,
    'smoking' : smoking,'alcohol' : alcohol,'sleep_hours' : sleep_hours,
    'regular_medicine' : regular_medicine,'junkfood' : junkfood,
    'stress' : stress,'blood_pressure_level' : blood_pressure_level,
    'pregnancies' : pregnancies,'urination_frequency' : urination_frequency,'pred_result': ret}

    us.profile.pred_result = ret
    us.profile.save()
    
    if(us.profile.pred_result=="positive"):
        return render(request,'result.html',context)

    elif(us.profile.pred_result=="negative"):
        return render(request,'neg.html',context)

def diet(request):
    if request.method == "POST":
        form = DietForm(request.POST)
        if form.is_valid():
            form.save()         
    else:
        form = DietForm()        
    return render(request, 'diet.html', {'form':form})

def diet_details(request):
    us = User.objects.get(username=request.user.username)

    hgt = int(request.POST.get('height'))
    us.profile.height = hgt

    wgt = int(request.POST.get('weight'))
    us.profile.weight = wgt

    acti = str(request.POST.get('activity'))
    us.profile.activity = acti

    age = us.profile.age
    gen = us.profile.gen

    bmr = 0
    if(gen=="male"):
        bmr = (10*wgt)+(6.25*hgt)-(5*age)+5
    elif (gen == "female"):
        bmr = (10 * wgt) + (6.25 * hgt) - (5 * age) -161

    tot_cal = 0
    if(acti=="little"):
        tot_cal = bmr*1.2
    elif(acti=="light"):
        tot_cal = bmr*1.375
    elif (acti == "moderate"):
        tot_cal = bmr * 1.55
    elif (acti == "hard"):
        tot_cal = bmr * 1.725
    elif (acti == "very hard"):
        tot_cal = bmr * 1.9
    
    us.profile.cal_req = tot_cal
    us.profile.save()

    return render(request, "details.html")

def diet_chart(request):
    us = User.objects.get(username=request.user.username)
    cal = us.profile.cal_req
    if(cal>1100 and cal<1500):
        return render(request, '1200.html')
    elif(cal>=1500 and cal<1800):
        return render(request, '1500.html')
    elif(cal>=1800 and cal<2000):
        return render(request, '1800.html')
    elif(cal>=2000 and cal<2500):
        return render(request, '2000.html')
    elif(cal>=2500 and cal<=3000):
        return render(request, '2500.html')
    elif(cal<1100 or cal>3000):
        return render(request,'sorry.html')