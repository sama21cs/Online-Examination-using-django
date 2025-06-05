from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('tests/', views.test_list, name='test_list'),
    path('test/<int:test_id>/instructions/', views.test_instructions, name='test_instructions'),
    path('test/<int:test_id>/', views.test_question, name='test_question'),
    path('test/<int:test_id>/<int:question_id>/', views.test_question, name='test_question'),
    path('test/<int:test_id>/<int:question_id>/submit/', views.submit_answer, name='submit_answer'),
    path('test/<int:test_id>/submit/', views.submit_test, name='submit_test'),
]