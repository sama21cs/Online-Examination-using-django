from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Test, Question, UserResponse, Feedback, Profile
from django.http import JsonResponse
import json
from django.utils import timezone
from datetime import timedelta

def home(request):
    tests = Test.objects.all()
    return render(request, 'home.html', {'tests': tests})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST.get('phone', '')
        user = User.objects.create_user(
            username=email, email=email, password=password,
            first_name=first_name, last_name=last_name
        )
        Profile.objects.create(user=user, phone=phone)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'test_list.html', {'tests': tests})

@login_required
def test_instructions(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
        if request.method == 'POST':
            print(f"Processing test start for user {request.user.username}, test {test.title}")
            if 'terms' in request.POST:
                UserResponse.objects.filter(user=request.user, test=test).delete()
                Feedback.objects.filter(user=request.user, test=test).delete()
                request.session['test_start_time'] = timezone.now().isoformat()
                request.session['test_id'] = test_id
                print(f"Redirecting to test question page for test {test_id}")
                return redirect('test_question', test_id=test_id)
            else:
                print("Terms not accepted")
                return render(request, 'test_instructions.html', {
                    'test': test,
                    'error': 'Please accept the terms and conditions to proceed.'
                })
        return render(request, 'test_instructions.html', {'test': test})
    except Test.DoesNotExist:
        return render(request, 'error.html', {'error': 'Test not found.'})

@login_required
def test_question(request, test_id, question_id=None):
    try:
        test = Test.objects.get(id=test_id)
        if request.session.get('test_id') != test_id:
            print(f"Test {test_id} not active for user {request.user.username}")
            return redirect('home')
        questions = Question.objects.filter(test=test).order_by('id')
        if not questions.exists():
            return render(request, 'error.html', {'error': 'No questions available for this test.'})
        
        question_list = list(questions)
        if question_id:
            question = Question.objects.get(id=question_id)
            question_index = question_list.index(question) + 1
        else:
            question = questions.first()
            question_index = 1

        responses = UserResponse.objects.filter(user=request.user, test=test)
        attempted = responses.exclude(answer='').count()
        marked_for_review = responses.filter(marked_for_review=True).count()
        unattempted = test.total_questions - attempted

        start_time = request.session.get('test_start_time')
        remaining_seconds = 0
        if start_time:
            start_time = timezone.datetime.fromisoformat(start_time)
            elapsed = timezone.now() - start_time
            remaining_seconds = max(0, test.duration * 60 - elapsed.total_seconds())

        context = {
            'test': test,
            'question': question,
            'questions': questions,
            'question_index': question_index,
            'tracker': {
                'total': test.total_questions,
                'attempted': attempted,
                'unattempted': unattempted,
                'marked_for_review': marked_for_review
            },
            'remaining_seconds': int(remaining_seconds)
        }
        print(f"Rendering test_question with context: {context}")
        return render(request, 'test_question.html', context)
    except Test.DoesNotExist:
        return render(request, 'error.html', {'error': 'Test not found.'})
    except Question.DoesNotExist:
        return render(request, 'error.html', {'error': 'Question not found.'})

@login_required
def submit_answer(request, test_id, question_id):
    if request.method == 'POST':
        try:
            question = Question.objects.get(id=question_id)
            test = question.test
            if request.session.get('test_id') != test_id:
                print(f"Test {test_id} not active for user {request.user.username}")
                return redirect('home')
            
            answer = request.POST.get('answer', '')
            marked_for_review = 'marked_for_review' in request.POST
            is_correct = answer == question.correct_answer if question.is_mcq and answer else False
            UserResponse.objects.update_or_create(
                user=request.user,
                test=question.test,
                question=question,
                defaults={
                    'answer': answer,
                    'is_correct': is_correct,
                    'marked_for_review': marked_for_review
                }
            )
            action = request.POST.get('action', 'next')
            print(f"Action: {action}, Question: {question_id}, Answer: {answer}, Marked for Review: {marked_for_review}")
            if action == 'previous':
                previous_question = Question.objects.filter(test=question.test, id__lt=question_id).order_by('-id').first()
                if previous_question:
                    return redirect('test_question', test_id=test_id, question_id=previous_question.id)
            elif action == 'next':
                next_question = Question.objects.filter(test=question.test, id__gt=question_id).order_by('id').first()
                if next_question:
                    return redirect('test_question', test_id=test_id, question_id=next_question.id)
                return redirect('submit_test', test_id=test_id)
            elif action == 'submit':
                return redirect('submit_test', test_id=test_id)
            return redirect('test_question', test_id=test_id, question_id=question_id)
        except Question.DoesNotExist:
            return render(request, 'error.html', {'error': 'Question not found.'})
    return redirect('test_question', test_id=test_id, question_id=question_id)

@login_required
def submit_test(request, test_id):
    try:
        test = Test.objects.get(id=test_id)
        if request.session.get('test_id') != test_id:
            print(f"Test {test_id} not active for user {request.user.username}")
            return redirect('home')
        responses = UserResponse.objects.filter(user=request.user, test=test)
        summary = {
            'marked': responses.filter(is_correct=True).count(),
            'unmarked': responses.filter(answer='').count(),
            'review': responses.filter(marked_for_review=True).count(),
        }
        if request.method == 'POST':
            if 'skip_feedback' in request.POST:
                responses.delete()
                request.session.pop('test_start_time', None)
                request.session.pop('test_id', None)
                return redirect('home')
            try:
                rating = request.POST.get('rating')
                experience = request.POST.get('experience')
                quality = request.POST.get('quality')
                difficulty = request.POST.get('difficulty')
                Feedback.objects.create(
                    user=request.user,
                    test=test,
                    rating=int(rating) if rating else None,
                    experience=int(experience) if experience else None,
                    quality=int(quality) if quality else None,
                    difficulty=int(difficulty) if difficulty else None,
                )
                responses.delete()
                request.session.pop('test_start_time', None)
                request.session.pop('test_id', None)
                return render(request, 'feedback.html', {
                    'test': test,
                    'summary': summary,
                    'feedback_submitted': True
                })
            except Exception as e:
                return render(request, 'feedback.html', {
                    'test': test,
                    'summary': summary,
                    'feedback_submitted': False,
                    'error': f'Error submitting feedback: {str(e)}'
                })
        return render(request, 'feedback.html', {
            'test': test,
            'summary': summary,
            'feedback_submitted': False
        })
    except Test.DoesNotExist:
        return render(request, 'error.html', {'error': 'Test not found.'})