import email
from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseBadRequest
from .models import *
import random
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        if uid.role == "Doctor":
            did = Doctor.objects.get(user_id = uid) 
            d_count=Doctor.objects.all().count()
            context = {
                'uid' : uid,
                'did' : did,
                "d_count":d_count,
             }
            return render(request,"myapp/index.html",context)

        else:
            pid = Patient.objects.get(user_id = uid) 
            # d_count=Doctor.objects.all().count()
            context = {
                'uid' : uid,
                'pid' : pid,
                # "d_count":d_count,
             }
            return render(request,"myapp/indexpat.html",context)
    else:
        return redirect("login")

def register(request):
    if "email" in request.session:
        return redirect("home")
    else:
        if request.POST:
        
            p_firstname=request.POST['firstname']
            p_lastname=request.POST['lastname']
            p_role=request.POST['role']
            p_email=request.POST['email']
            p_contact=request.POST['contact']
            l1=["ass789",'4334hd','sdss454','dsf72d','546fdc','sd743b']
            password=random.choice(l1)+p_email[3:6]+p_contact[4:7]
            uid=user.objects.create(email=p_email,password=password,role=p_role)
            send_mail("AUTHENTICATION","WELCOME TO MEDICO-EXPERT YOUR PASSWORD IS:"+str(password),"alkpvt2015@gmail.com",[p_email])
            if p_role == "Doctor":
                did=Doctor.objects.create(user_id=uid,firstname=p_firstname,lastname=p_lastname,mobile=p_contact)
                if did:
                    print("insert successfully")
                    context={
                        "s_msg":"Successfully Register"

                    }
                    return render(request,"myapp/register.html",context)
                else:
                    return render(request,"myapp/register.html")

            elif p_role == "Patient":
                pid=Patient.objects.create(user_id=uid,firstname=p_firstname,lastname=p_lastname,mobile=p_contact)
                if pid:
                    print("insert successfully")
                    context={
                        "s_msg":"Successfully Register"

                    }
                    return render(request,"myapp/register.html",context)
                else:
                    return render(request,"myapp/register.html")

            else:
                # return render(request,"myapp/register.html")
                pass
            print("----->firstname",p_firstname)
            return render(request,"myapp/register.html")

        else:
            print("------>Page Loaded")
            return render(request,"myapp/register.html")

def login(request):
    if "email" in request.session:
        return redirect('home')
    else:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']
            print("------>login",email)
            try:
                uid=user.objects.get(email = email)
                print("------>login",uid.password)
                
                if uid.password == password:
                    if uid.is_verify:
                        request.session["email"] = uid.email
                        if uid.role == "Doctor":
                            did=Doctor.objects.get(user_id = uid)
                            context={
                                "uid":uid,
                                "did":did,
                            }
                            # send_mail("WELCOME","WELCOME TO MEDICO-EXPERT","alkpvt2015@gmail.com",[email])
                            return render(request,"myapp/index.html",context)
                        else:
                            pid=Patient.objects.get(user_id = uid)
                            context={
                                "uid":uid,
                                "pid":pid,
                            }
                            # send_mail("WELCOME","WELCOME TO MEDICO-EXPERT","alkpvt2015@gmail.com",[email])
                            return render(request,"myapp/indexpat.html",context)
                    else:
                        context={
                            'email':uid.email
                        }
                        return render(request,"myapp/changepassword.html",context)
                else:  
                    print("=======>Wrong password")
                    context={
                                "e_msg" : "Invalid Password"
                            } 
                    return render(request,"myapp/login.html",context)
            except user.DoesNotExist:
                    context={
                
                        'e_msg':"Email address does not exist"
                    }
                    return render(request,"myapp/login.html",context)
        else:
            return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
       print("------>logout")
       return render(request,"myapp/login.html")

def profile(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        if uid.role == "Doctor":
            did = Doctor.objects.get(user_id = uid)
            context = {
                'uid':uid,
                'did':did,
            }
            return render(request,"myapp/profile.html",context)
        else:
            pid = Patient.objects.get(user_id = uid)
            context = {
                'uid':uid,
                'pid':pid,
            }
            return render(request,"myapp/profile.html",context)
    else:
       
        return redirect("login")
def doc_profile(request):
    try:
        if request.POST:
            print("inside the doc profile")
            uid=user.objects.get(email = request.session['email'])
            did=Doctor.objects.get(user_id = uid)
            print("----------->firstname=",request.POST['firstname'])
            did.firstname = request.POST['firstname']
            did.lastname = request.POST['lastname']
            did.qualification =request.POST['qualification']
            did.specification = request.POST['specification']
            did.available_time = request.POST['available_time']
            did.experience=request.POST['experience']
            did.clinic_name = request.POST['clinic_name']
            did.clinic_city = request.POST['clinic_city']
            did.clinic_address = request.POST['clinic_address']
            did.mobile = request.POST['mobile']
            if "pic" in request.FILES:
                did.pic = request.FILES['pic']
            did.save()
            # uid.save()
            context={
                    "uid":uid,
                    "did":did,
                    "s_msg":"Successfully Profile Updated",
            }
            print("---------> goimg to profilepage")
            return render(request,"myapp/profile.html",context)
        else:
            print("inside the else part")
            return redirect("login")
    except Exception as e:
         print("------>Exception",e)
         return redirect("login")
  
def doc_pass_change(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        if uid.role == "Doctor":
            did=Doctor.objects.get(user_id=uid)
            currentpassword=request.POST['currentpassword']
            newpassword=request.POST['newpassword']
            if uid.password==currentpassword:
                uid.password=newpassword
                uid.save()
                del request.session['email']
                context={
                "uid":uid,
                "did":did,
                "s_msg":"Successfully Password Reset"
                }
                print("---------> successsfully change")
                return render(request,"myapp/login.html",context)
            else:
                e_msg="invalid Password"
                context={
                "uid":uid,
                "did":did,
                "e_msg":e_msg,
                }
                print("--------->invalid")
                return render(request,"myapp/profile.html",context)

def all_doctors(request):
    if "email" in request.session:
        uid = user.objects.get(email = request.session['email'])
        if uid.role=="Doctor":
            did=Doctor.objects.get(user_id = uid)
            dall=Doctor.objects.filter().exclude(user_id=uid)
            context={
                "uid":uid,
                "did":did,
                "dall":dall,
                }
            return render(request,"myapp/all-doctors.html",context)
        else:
            pass

def p_all_doctors(request):
    if "email" in request.session:
        uid = user.objects.get(email = request.session['email'])
        pid=Patient.objects.get(user_id = uid)
        dall=Doctor.objects.all()
        context={
            "uid":uid,
            "pid":pid,
            "dall":dall,
            }
        return render(request,"myapp/p-all-doctors.html",context)
    else:
        pass

def view_doc(request,pk):
    if "email" in request.session:
        uid = user.objects.get(email = request.session['email'])
        if uid.role=="Doctor":
            did=Doctor.objects.get(user_id = uid)
            did_s=Doctor.objects.get(id=pk)
            context={
                "uid":uid,
                "did":did,
                "did_s": did_s,
                }
            return render(request,"myapp/doc-spec-profile.html",context)
        elif uid.role=="Patient": 
            pid=Patient.objects.get(user_id = uid)
            did_s=Doctor.objects.get(id=pk)
            context={
                "uid":uid,
                "pid":pid,
                "did_s": did_s,
                }
            return render(request,"myapp/doc-spec-profile.html",context)
        else:
            pass

def changepassword(request):
    try:
        if request.POST:
            email = request.POST['email']
            oldpassword = request.POST['oldpassword']
            newpassword = request.POST['newpassword']
            confirmpassword = request.POST['confirmpassword']

            uid=user.objects.get(email = email)
            if uid.password == oldpassword and newpassword == confirmpassword:
                uid.password = newpassword
                uid.is_verify = True
                uid.is_active = True
                uid.save()
                context={
                    's_msg':"Successfully password REset"
                }
                print("Successfully password REset")
                return render(request,"myapp/login.html",context)
            else:
                context={
                    'e_msg':"Invalid Password or doesnot match password"
                }
                return render(request,"myapp/login.html",context)
        else:
            return render(request,"myapp/login.html")
    except:
         return render(request,"myapp/login.html") 

def all_patients(request):
    if "email" in request.session:
        uid= user.objects.get(email = request.session['email'])
        if uid.role == "Doctor":
            did = Doctor.objects.get(user_id = uid)
            print("---->doctor", did)
            pall = Appointment.objects.filter(doctor_id = did, status="PENDING")
            context= {
                'did': did,
                'uid' : uid,
                'pall': pall,
            }
            print("________________ pall",pall)
            return render(request, "myapp/all-patients.html", context)
        else:
            pass

def p_doc_spec_profile(request,pk):
     if "email" in request.session:
         uid=user.objects.get(email = request.session['email'])
         pid=Patient.objects.get(user_id = uid)
         did_s=Doctor.objects.get(id = pk)
         context={
             'uid':uid,
             'pid':pid,
             'did_s':did_s,
             
         }
         return render(request,"myapp/p-doc-spec-profile.html", context) 
                  
def p_book_appointment(request,pk):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        pid=Patient.objects.get(user_id = uid)
        did=Doctor.objects.get(id = pk)
        context={
             'uid':uid,
             'pid':pid,
             'did':did,
             }
        return render(request,"myapp/book-appointment.html",context) 

def p_book_a(request):
    if request.POST:
        pid=request.POST["pid"]
        did=request.POST["did"]
        date=request.POST["date"]
        time=request.POST["time"]
        reason=request.POST["reason"]
        case_status=request.POST["case_status"]

        patient_id = Patient.objects.get(id = pid)
        doctor_id=Doctor.objects.get(id=did)
        paid=Appointment.objects.create(patient_id=patient_id,doctor_id=doctor_id,a_date=date,a_time=time,reason=reason,case_status=case_status)
       
        if paid:
            context={
                'pid':pid,
                "did":did,
                "msg":"Successfully Appoinment request send",
            }
            return render(request,"myapp/book-appointment.html",context) 
    else:
           return render(request,"myapp/book-appointment.html")

def approve_a(request, pk):
    if "email" in request.session:
        uid= user.objects.get(email = request.session['email'])
        if uid.role == "Doctor":
            did = Doctor.objects.get(user_id= uid)
            aid = Appointment.objects.get(id=pk)
            aid.status="APPROVED"
            aid.save()
            send_mail("APPOINTMENT STATUS", "YOUR APPOINTMENT HAS BEEN CONFIRMED BY DOCTOR","alkpvt2015@gmail.com",[aid.patient_id.user_id.email])
            return redirect("all-patients")
        else:
            return redirect("pt-profile")

def reject_a(request, pk):
    if "email" in request.session:
        uid= user.objects.get(email = request.session['email'])
        if uid.role == "Doctor":
            did = Doctor.objects.get(user_id= uid)
            aid = Appointment.objects.get(id=pk)
            aid.status="REJECT"
            aid.save()
            send_mail("APPOINTMENT STATUS", "YOUR APPOINTMENT HAS BEEN NOT CONFIRMED BY DOCTOR","karanjethava4455@gmail.com",[aid.patient_id.user_id.email])
            return redirect("all-patients")
        else:
            return redirect("pat-profile")

def pat_profile(request):
    try:
        if request.POST:
            print("-->inside the pt profile")
            uid= user.objects.get(email= request.session['email'])
            pid = Patient.objects.get(User_id= uid)
            print("-->pt firstname=", request.POST['firstname'])
            pid.firstname = request.POST['firstname']
            pid.lastname = request.POST['lastname']
            pid.age = request.POST['age']
            pid.gender = request.POST['gender']
            pid.birthdate = request.POST['birthdate']
            pid.blood_group = request.POST['blood_group']
            pid.height = request.POST['height']
            pid.weight = request.POST['weight']
            pid.address = request.POST['address']
            pid.mobile = request.POST['mobile']
            if "pic" in request.FILES:
                pid.pic = request.FILES['pic']
            pid.save()
            context= {
                    "uid" : uid,
                    "pid" : pid,
                    "s_msg" : "successfully profile updated!!"
            }
            print("-->going to profile page")
            return render(request, "myapp/pt-profile.html", context)
        else:
            print("-->inside the else part")
            return redirect("login")
    except Exception as e:
        print("-->",e)
        return redirect("login")

def pt_profile(request):
    if "email" in request.session:
        uid=user.objects.get(email = request.session['email'])
        if uid.role == "Patient":
            pid = Patient.objects.get(user_id = uid)
            context = {
                'uid':uid,
                'pid':pid,
            }
            return render(request,"myapp/pt-profile.html",context)