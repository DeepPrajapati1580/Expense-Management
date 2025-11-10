from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.urls import reverse_lazy
from signup.models import User

from django.shortcuts import render, redirect
from .models import Expense
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.db.models import Sum
from .models import Expense
from django.contrib.auth.decorators import login_required


def signup1(request):
    return render(request,'signup.html')




from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib import messages  # For displaying error messages

# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Check if username or email already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken!")
#             return render(request, 'signup.html')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already registered!")
#             return render(request, 'signup.html')

#         # Hash the password before saving
    

#         # Create a new user and save to database
#         user = User(username=username, email=email, password=password)
#         user.save()

#         messages.success(request, "Account created successfully! Please login.")
#         return redirect('loginselect')  # Redirect to the login page

#     return render(request, 'signup.html')  # Load signup page for GET request

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login_v')

    return render(request, 'signup.html')


def loginselect(request):
    return render(request,'loginselect.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_v(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Ensure username exists
        password = request.POST.get('password')  # Get password
        user_type = request.POST.get('userType')  # Get user type (string)

        user = authenticate(request, username=username, password=password)  # Authenticate user
       
        if user is not None:
            login(request, user)  # Login user

            # Store session data
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['user_type'] = user_type

            # Redirect based on user type
            if user_type == "1":
                return redirect('home')  # Redirect to User dashboard
            elif user_type == "0":
                return redirect('home1')  # Redirect to Family dashboard
            else:
                return render(request, 'loginselect.html', {"error": "Invalid account type"})
        else:
            return render(request, 'loginselect.html', {"error": "Invalid credentials"})

    return render(request, 'loginselect.html')  # Render login page for GET request

@login_required(login_url='login_v')
def e1(request):
    return render(request,'e1.html')

@login_required(login_url='login_v')
def e2(request):
    username = request.session.get('username')
    return render(request,'e2.html', {'username': username})

@login_required(login_url='login_v')
def e3(request):
     
    return render(request,'e3.html')

@login_required(login_url='login_v')
def e1(request):
     
    return render(request,'e1.html')


@login_required(login_url='login_v')
def e11(request):
    return render(request,'e11.html')

@login_required(login_url='login_v')
def add(request):
    days = list(range(1, 32))  # Generates numbers 1 to 31
    years = list(range(2020, 2026))  # Generates years 2020 to 2025
    username = request.session.get('username') 
    return render(request, "add.html", {"days": days, "years": years , 'username': username})

@login_required(login_url='login_v')
def history(request):
    return redirect("user_expenses")

from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

@login_required(login_url='login_v')
def logout_view(request):
    request.session.flush() 
    auth_logout(request)  # Call Django's logout function
    return redirect('login_v')  # Redirect to login pageloginselect.html')


@login_required(login_url='login_v')
def home(request):
    user_id = request.session.get('user_id')  
    username = request.session.get('username') 
    
    if not user_id:  # Redirect to login if not logged in
        return redirect('loginselect')

    return render(request, 'home.html', {'username': username})

@login_required(login_url='login_v')
def home1(request):
    user_id = request.session.get('user_id')  
    username = request.session.get('username') 
    if  not user_id:  # Check if user is logged in
        return redirect('loginselect')  # Redirect to loginselect if not logged in
    
    return render(request, 'home1.html',{'username': username})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Expense
@login_required(login_url='login_v')
def add_expense(request):
    if request.method == "POST":
        
        day = request.POST.get("day")
        month = request.POST.get("month")
        year = request.POST.get("year")
        item = request.POST.get("item")
        price = request.POST.get("price")

        if day and month and year and item and price:
            Expense.objects.create(day=day, month=month, year=year, item=item, price=price, username=request.session.get('username') )
            messages.success(request, "Your expense has been successfully added!")
            return redirect("success_page")  # Redirect to success page

    days = range(1, 32)
    years = range(2020, 2031)
    
    return render(request, "add.html", {"days": days, "years": years})

@login_required(login_url='login_v')
def success_page(request):
    return render(request, "success.html")


from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import Expense  # Import the Expense model
@login_required(login_url='login_v')
def set_year_month(request):
    if request.method == "POST":
        username = request.session.get("username")
        year = request.POST.get("year")
        month = request.POST.get("month")

        # Validate inputs
        if not username or year == "Select a year" or month == "Select a month":
            return render(request, "e1.html", {"error": "Please select a valid year and month."})

        # Check if the same username, year, and month exist in the database
        expense_exists = Expense.objects.filter(username=username, year=year, month=month).exists()

        if expense_exists:
            # Store selected year and month in session
            request.session["year"] = year
            request.session["month"] = month

            # Redirect to e3.html and pass year & month in context
            return redirect("e3_view")  # Ensure 'e3_page' exists in urls.py
        else:
            return  redirect("e1") 

    return render(request, "e1.html")  # Show e1.html on GET request

@login_required(login_url='login_v')
def e3_view(request):
    username = request.session.get("username")
    year = request.session.get("year")
    month = request.session.get("month")

    if not username or not year or not month:
        return render(request, "e1.html", {"error": "Invalid session data. Please select year and month again."})

    # Fetch expenses based on session data
    yearly_expense = Expense.objects.filter(username=username, year=year).aggregate(total_price=Sum("price")).get("total_price", 0) or 0
    monthly_expense = Expense.objects.filter(username=username, year=year, month=month).aggregate(total_price=Sum("price")).get("total_price", 0) or 0
    total_expense = Expense.objects.filter(username=username).aggregate(total_price=Sum("price")).get("total_price", 0) or 0

    # Pass values to the template
    context = {
        "username": username,
        "year": year,
        "month": month,
        "yearly_expense": yearly_expense,
        "monthly_expense": monthly_expense,
        "total_expense": total_expense,
    }

    return render(request, "e3.html", context)
@login_required(login_url='login_v')
def user_expenses(request):
    username = request.session.get("username")

    if not username:
        return render(request, "e2.html", {"error": "You must be logged in to view expenses."})

    # Fetch expenses related to the logged-in user
    user_expense_list = Expense.objects.filter(username=username)

    context = {
        "username": username,
        "expenses": user_expense_list,
    }

    return render(request, "history.html", context)  # Ensure you create this template

from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
@login_required(login_url='login_v')
def update_expense(request, expense_id):
    username = request.session.get("username")
    expense = get_object_or_404(Expense, id=expense_id)

    # Ensure only the owner can update the expense
    if expense.username != username:
        return redirect("/history")  

    if request.method == "POST":
        expense.item = request.POST["item"]
        expense.price = request.POST["price"]
        expense.day = request.POST["day"]
        expense.month = request.POST["month"]
        expense.year = request.POST["year"]
        expense.save()
        return redirect("/history")  

    return render(request, "update.html", {"expense": expense})
@login_required(login_url='login_v')
def delete_expense(request, expense_id):
    username = request.session.get("username")
    expense = get_object_or_404(Expense, id=expense_id)

    # Ensure only the owner can delete the expense
    if expense.username != username:
        return redirect("/history")  

    if request.method == "POST":
        expense.delete()
        return redirect("/history")  

    return render(request, "delete.html", {"expense": expense})

from django.shortcuts import render
from .models import Expense

from django.shortcuts import render
from .models import Expense
@login_required(login_url='login_v')
def search_expense(request):
    username = request.session.get("username")  # Get the logged-in user
    expenses = None  
    year_range = range(2020, 2026)  
    days = list(range(1, 32))

    if request.method == "GET":
        day = request.GET.get("day")
        month = request.GET.get("month")
        year = request.GET.get("year")

        if day and month and year:
            expenses = Expense.objects.filter(username=username, day=day, month=month, year=year)

    return render(request, "search.html", {"expenses": expenses, "year_range": year_range,"days": days})

from django.shortcuts import render
from .models import Expense
from django.utils.timezone import now
@login_required(login_url='login_v')
def yearly_expense_details(request):
    current_year = request.session.get("year")
    expenses = Expense.objects.filter(year=current_year, username=request.session.get("username"))
    total_yearly = sum(exp.price for exp in expenses)
    return render(request, 'yearly_expense.html', {'expenses': expenses, 'total_yearly': total_yearly})
@login_required(login_url='login_v')
def monthly_expense_details(request):
    current_month = request.session.get("month")  # Gets month name (e.g., "January")
    current_year = request.session.get("year")
    expenses = Expense.objects.filter(month=current_month, year=current_year, username=request.session.get("username"))
    total_monthly = sum(exp.price for exp in expenses)
    return render(request, 'monthly_expense.html', {'expenses': expenses, 'total_monthly': total_monthly})
@login_required(login_url='login_v')
def total_expense_details(request):
    expenses = Expense.objects.filter(username=request.session.get("username"))
    total_expense = sum(exp.price for exp in expenses)
    return render(request, 'total_expense.html', {'expenses': expenses, 'total_expense': total_expense})

@login_required(login_url='login_v')
def e21(request):
    username = request.session.get("username")
    return render(request,'e21.html',{'username': username})
@login_required(login_url='login_v')
def search_expense1(request):
    username = request.session.get("username")  # Get the logged-in user
    expenses = None  
    year_range = range(2020, 2026)
    days = list(range(1, 32))  

    if request.method == "GET":
        day = request.GET.get("day")
        month = request.GET.get("month")
        year = request.GET.get("year")

        if day and month and year:
            expenses = Expense.objects.filter(username=username, day=day, month=month, year=year)

    return render(request, "search1.html", {"expenses": expenses, "year_range": year_range,"days": days})
@login_required(login_url='login_v')
def history1(request):
    return redirect("user_expenses1")


@login_required(login_url='login_v')
def user_expenses1(request):
    username = request.session.get("username")

    if not username:
        return render(request, "e2.html", {"error": "You must be logged in to view expenses."})

    # Fetch expenses related to the logged-in user
    user_expense_list = Expense.objects.filter(username=username)

    context = {
        "username": username,
        "expenses": user_expense_list,
    }

    return render(request, "history1.html", context)  # Ensure you create this template
@login_required(login_url='login_v')
def set_year_month1(request):
    if request.method == "POST":
        username = request.session.get("username")
        year = request.POST.get("year")
        month = request.POST.get("month")

        # Validate inputs
        if not username or year == "Select a year" or month == "Select a month":
            return render(request, "e11.html", {"error": "Please select a valid year and month."})

        # Check if the same username, year, and month exist in the database
        expense_exists = Expense.objects.filter(username=username, year=year, month=month).exists()

        if expense_exists:
            # Store selected year and month in session
            request.session["year"] = year
            request.session["month"] = month

            # Redirect to e3.html and pass year & month in context
            return redirect("e31_view")  # Ensure 'e3_page' exists in urls.py
        else:
            return render(request, "e11.html")

    return render(request, "e11.html")  # Show e1.html on GET request

@login_required(login_url='login_v')
def e31_view(request):
    username = request.session.get("username")
    year = request.session.get("year")
    month = request.session.get("month")

    if not username or not year or not month:
        return render(request, "e11.html", {"error": "Invalid session data. Please select year and month again."})

    # Fetch expenses based on session data
    yearly_expense = Expense.objects.filter(username=username, year=year).aggregate(total_price=Sum("price")).get("total_price", 0) or 0
    monthly_expense = Expense.objects.filter(username=username, year=year, month=month).aggregate(total_price=Sum("price")).get("total_price", 0) or 0
    total_expense = Expense.objects.filter(username=username).aggregate(total_price=Sum("price")).get("total_price", 0) or 0

    # Pass values to the template
    context = {
        "username": username,
        "year": year,
        "month": month,
        "yearly_expense": yearly_expense,
        "monthly_expense": monthly_expense,
        "total_expense": total_expense,
    }

    return render(request, "e31.html", context)

@login_required(login_url='login_v')
def update_expense1(request, expense_id):
    username = request.session.get("username")
    expense = get_object_or_404(Expense, id=expense_id)

    # Ensure only the owner can update the expense
    if expense.username != username:
        return redirect("/history")  

    if request.method == "POST":
        expense.item = request.POST["item"]
        expense.price = request.POST["price"]
        expense.day = request.POST["day"]
        expense.month = request.POST["month"]
        expense.year = request.POST["year"]
        expense.save()
        return redirect("/history")  

    return render(request, "update.html", {"expense": expense})
@login_required(login_url='login_v')
def delete_expense1(request, expense_id):
    username = request.session.get("username")
    expense = get_object_or_404(Expense, id=expense_id)

    # Ensure only the owner can delete the expense
    if expense.username != username:
        return redirect("/history")  

    if request.method == "POST":
        expense.delete()
        return redirect("/history")  

    return render(request, "delete.html", {"expense": expense})

@login_required(login_url='login_v')
def yearly_expense_details1(request):
    current_year = request.session.get("year")
    expenses = Expense.objects.filter(year=current_year, username=request.session.get("username"))
    total_yearly = sum(exp.price for exp in expenses)
    return render(request, 'yearly_expense1.html', {'expenses': expenses, 'total_yearly': total_yearly})
@login_required(login_url='login_v')
def monthly_expense_details1(request):
    current_month =  request.session.get("month")  # Gets month name (e.g., "January")
    current_year = request.session.get("year")
    expenses = Expense.objects.filter(month=current_month, year=current_year, username=request.session.get("username"))
    total_monthly = sum(exp.price for exp in expenses)
    return render(request, 'monthly_expense1.html', {'expenses': expenses, 'total_monthly': total_monthly})
@login_required(login_url='login_v')
def total_expense_details1(request):
    expenses = Expense.objects.filter(username=request.session.get("username"))
    total_expense = sum(exp.price for exp in expenses)
    return render(request, 'total_expense1.html', {'expenses': expenses, 'total_expense': total_expense})
