from django.contrib import admin
from django.urls import path,include
from signup import views
urlpatterns = [
    path('',views.signup1,name='signup1'),
    path('signup/', views.signup, name='signup'),
    path('loginselect',views.loginselect,name='loginselect'),
    path('home' , views.home , name='home'),
    path('login_v',views.login_v,name='login_v'),
    path('home1' , views.home1 , name='home1'),
    path('e1' , views.e1 , name='e1'),
    path('e2' , views.e2 , name='e2'),
    path('e3' , views.e3 , name='e3'),
    path('add' , views.add , name='add'),
    path('history' , views.history , name='history'),
    path('logout', views.logout_view, name='logout'),
    path("add_expense", views.add_expense, name="add_expense"),
    path("set_year_month", views.set_year_month, name="set_year_month"),
    path("e3_view",views.e3_view, name="e3_view"),
    path("user_expenses",views.user_expenses, name="user_expenses"),
    path("update/<int:expense_id>/", views.update_expense, name="update_expense"),
    path("delete/<int:expense_id>/", views.delete_expense, name="delete_expense"),
    path("search/", views.search_expense, name="search_expense"),
    path('yearly-expense/', views.yearly_expense_details, name='yearly_expense'),
    path('monthly-expense/', views.monthly_expense_details, name='monthly_expense'),
    path('total-expense/', views.total_expense_details, name='total_expense'),
    path('yearly-expense1/', views.yearly_expense_details1, name='yearly_expense1'),
    path('monthly-expense1/', views.monthly_expense_details1, name='monthly_expense1'),
    path('total-expense1/', views.total_expense_details1, name='total_expense1'),
    path('e21' , views.e21 , name='e21'),
    path('history1' , views.history1 , name='history1'),
    path("search1/", views.search_expense1, name="search_expense1"),
    path("user_expenses1",views.user_expenses1, name="user_expenses1"),
    path("set_year_month1", views.set_year_month1, name="set_year_month1"),
    path("e31_view",views.e31_view, name="e31_view"),
    path('success/', views.success_page, name="success_page"),
    


]
