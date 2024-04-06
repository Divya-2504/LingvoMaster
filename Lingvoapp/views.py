from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def home(request):
    context = {'page':'Home'}
    return render(request,"index.html",context)


def about(request):
    context = {'page':'About'}
    return render(request,"about.html",context)


def contact(request):
    context = {'page':'Contact'}
    return render(request,"contact.html",context)

@login_required(login_url="/signin/")
def account(request):
    context = {'page':'account'}
    return render(request,"account.html",context)


def signup(request):
    if request.method == "POST":
        
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username already taken")
            return redirect('/signup/')

        user = User.objects.create( 
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        login(request,user)
        return redirect('/signin/')
    context = {'page':'Signup'}
    return render(request,"signup.html",context)


def signin(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Username does not exist.")
            return redirect("/signin/")
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(request, "Incorrect Password.")
            return redirect("/signin/")

        else:
            login(request, user)
            return redirect("/")
    context = {'page':'Signin'}
    return render(request,"signin.html",context)


def signout(request):
    logout(request)
    return redirect("/signin/")

@login_required(login_url="/signin/")
def lang_selection(request):
    context = {'page':'Languages'}
    return render(request,'language.html',context)

@login_required(login_url="/signin/")
def userunit(request,userlang):
    context={'page':'Unit','lang':userlang}
    return render(request,"unit.html",context)

@login_required(login_url="/signin/")
def learn(request,userlang,userid,unitid):
    if(userlang == "French"):
        x = "french_words"
    elif(userlang == "Spanish"):
        x = "spanish_words"
    elif(userlang == "German"):
        x = "german_words"
    elif(userlang == "Hindi"):
        x = "hindi_words"
    elif(userlang == "Gujarati"):
        x = "gujarati_words"
    user = User.objects.get(id = userid)
    language = Language.objects.get(language_name = userlang)
    unit2 = Unit.objects.get(unit_id = unitid)
    temp = Question.objects.select_related('unit').filter(unit_id=unit2)

    check = CourseRegistration.objects.filter(user = user,language = language , unit = unit2)
    if check.exists():
        pass
    else:
        course = CourseRegistration.objects.create(user = user,
                                               language = language,
                                                unit = unit2)
        course.save()
    unit1 = Unit.objects.get(unit_id = unitid)
    data = UnitContent.objects.filter(unit = unit1).values_list("english_words",x)
    print(data)
    print(x)
    context = {'page':'Learn','data':data,"id" :temp.first().question_id }
    return render(request,"learn.html",context)

@login_required(login_url="/signin/")
def quiz(request,userlang,userid,unitid,qid):
    user = User.objects.get(id = userid)
    language = Language.objects.get(language_name = userlang)
    unit2 = Unit.objects.get(unit_id = unitid)
    temp = Question.objects.select_related('unit').filter(unit_id=unit2)
    print(temp.first().question_id , temp.last().question_id)
    # question_start_id = temp.first().question_id
    question_last_id = temp.last().question_id
    print(unit2)
    check = CourseRegistration.objects.filter(user = user,language = language , unit = unit2)
    if check.exists():
        pass
    else:
        return redirect(f"/selection/{userlang}/{userid}/{unitid}")
    
    if(userlang == "French"):
        x = "french_question"
    elif(userlang == "Spanish"):
        x = "spanish_question"
    elif(userlang == "German"):
        x = "german_question"
    elif(userlang == "Hindi"):
        x = "hindi_question"
    elif(userlang == "Gujarati"):
        x = "gujarati_question"
    else :
        pass
    question = Question.objects.filter(question_id=qid,unit = unit2).values_list(x).first()[0]
    answer = Answer.objects.filter(question_id=qid).values_list("option_1","option_2","option_3","option_4","correct_answer").first()
    print(answer)
    y=userlang
    # print(full_row_value)
    # print(question)
    if request.method == "POST":
        submitted_answer = request.POST.get("answer")
        correct_answer = answer[4]
        if submitted_answer == correct_answer:
            qid+=1
            if qid > question_last_id:
                return redirect(f"/selection/{userlang}")
            else:
                return redirect(f"/selection/{userlang}/{userid}/{unitid}/quiz/{qid}")
        else:
            messages.error(request, "Incorrect Choice!")


    context = {'page':'Question','data':question,'option':answer[:4],'qid':qid,'lang':y}
    return render(request,"quiz.html",context)