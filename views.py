from django.shortcuts import render
from TrainTimmings.models import train
from datetime import date,time

#  Create your views here.
def train_db(request):

    #record1 = train(train_id=int(101),name="Mangalore Express",departure_date=date(int(2021),int(12),int(10)),departure_time=time(int(2),int(30),int(0)),duration="4 Hours")
    #record1.save()
    #record2 = train(train_id=int(102),name="Chennai Express",departure_date=date(int(2022),int(1),int(2)),departure_time=time(int(4),int(55),int(0)),duration="6 Hours")
    #record2.save()
    #record3 = train(train_id=int(103),name="Chamundi Express",departure_date=date(int(2022),int(1),int(19)),departure_time=time(int(11),int(55),int(0)),duration="3 Hours")
    #record3.save()
    #record4 = train(train_id=int(104),name="Shatabdi Express",departure_date=date(int(2021),int(11),int(26)),departure_time=time(int(13),int(45),int(0)),duration="4.5 Hours")
    #record4.save()
    #record5 = train(train_id=int(105),name="Rajdhani Express",departure_date=date(int(2021),int(11),int(26)),departure_time=time(int(11),int(55),int(0)),duration="3.5 Hours")
    #record5.save()
    #record6 = train(train_id=int(106),name="Gatimaan Express",departure_date=date(int(2021),int(11),int(27)),departure_time=time(int(3),int(35),int(0)),duration="2.6 Hours")
    #record6.save()
    #record7 = train(train_id=int(107),name="Amaravati Express",departure_date=date(int(2021),int(11),int(27)),departure_time=time(int(18),int(45),int(0)),duration="2 Hours")
    #record7.save()
    #record8 = train(train_id=int(108),name="Ypr Karvar Express",departure_date=date(int(2021),int(11),int(29)),departure_time=time(int(15),int(25),int(0)),duration="4 Hours")
    #record8.save()
    #record9 = train(train_id=int(109),name="Karnataka Express",departure_date=date(int(2021),int(12),int(1)),departure_time=time(int(14),int(30),int(0)),duration="8 Hours")
    #record9.save()
    #record10 = train(train_id=int(110),name="Basava Express",departure_date=date(int(2021),int(12),int(4)),departure_time=time(int(5),int(45),int(0)),duration="3 Hours")
    #record10.save()
    record = train.objects.all()
    return render(request,"train.html",{"record":record})

