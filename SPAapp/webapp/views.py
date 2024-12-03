from datetime import datetime
from django.shortcuts import render, redirect
from .models import User, Comment, Post
import re


def main_page(request):
    """Main page of application"""
    if request.method == "POST":
        return redirect('login')
    return render(request, 'main.html')


def login(request):
    """Login page of application"""
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(UserName=name, Password=password)
        if users:
            return redirect('postboard')
        else:
            return render(
                request, 'login.html',
                {'error': 'ERROR: Invalid username or password. This user does not exist'}
            )
    return render(request, 'login.html')


def register(request):
    """Register page of application"""
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        captcha = request.POST.get('captcha')
        # username
        if 100 < len(name) < 2:
            return render(
                request, 'register.html',
                {'error': 'ERROR: Username is too short. Minimum length is 2 and maximum length is 100'}
            )
        elif re.search(r'[^a-zA-Z0-9]', name):
            return render(
                request, 'register.html',
                {'error': 'ERROR: Username must contain only letters and numbers'}
            )
        # email
        elif 100 < len(email) < 12:
            return render(
                request, 'register.html',
                {'error': 'ERROR: Email is too short. Minimum length is 12 and maximum length is 100'}
            )
        elif re.search(r'[^a-zA-Z0-9@._]', email):
            return render(
                request, 'register.html',
                {'error': 'ERROR: Invalid email format'}
            )
        # password
        elif 20 < len(password) < 4:
            return render(
                request, 'register.html',
                {'error': 'ERROR: Password is too short. Minimum length is 4 and maximum length is 20'}
            )
        elif password != request.POST.get('password2'):
            return render(
                request, 'register.html',
                {'error': 'ERROR: Passwords do not match'}
            )
        elif re.search(r'[^a-zA-Z0-9]', password):
            return render(
                request, 'register.html',
                {'error': 'ERROR: Password must contain only letters and numbers'}
            )
        # captcha
        elif 100 < len(captcha) < 2:
            return render(
                request, 'register.html',
                {'error': 'ERROR: CAPTCHA is too short. Minimum length is 2 and maximum length is 100'}
            )
        elif re.search(r'[^a-zA-Z0-9]', captcha):
            return render(
                request, 'register.html',
                {'error': 'ERROR: CAPTCHA must contain only letters and numbers'}
            )

        user = User(
            UserName=request.POST.get('username'),
            Email=request.POST.get('email'),
            RegisterDate=datetime.now(),
            HomePage=request.POST.get('homepage'),
            CAPTCHA=request.POST.get('captcha'),
            Password=request.POST.get('password'),
        )
        user.save()
        return redirect('postboard')
    return render(request, 'register.html')


def postboard(request):
    """PostBoard page of application"""
    if request.method == "POST":
        sort_by = request.POST.get('sort')
        result = Post.objects.all().order_by('-id')[0:25]
        if sort_by == '1':
            result = Post.objects.all().order_by('User')
            return render(
                request, 'postboard.html',
                {'result': result}
            )
        elif sort_by == '2':
            result = Post.objects.all().order_by('Created')
            return render(
                request, 'postboard.html',
                {'result': result}
            )
        elif sort_by == '3':
            result = Post.objects.all().order_by('User__Email')
            return render(
                request, 'postboard.html',
                {'result': result}
            )
    result = Post.objects.all().order_by('-id')[0:25]
    if not result:
        return render(
            request, 'postboard.html',
            {'error': 'ERROR: No posts found. Please create your first post and show it to the world'}
        )
    return render(
        request, 'postboard.html',
        {'result': result}
    )


def add_post(request):
    """Create a new Post of user"""
    if request.method == "POST":
        user = request.POST.get('username')
        text = request.POST.get('comment')
        users = User.objects.filter(UserName=user)
        if users:
            user_data = User.objects.get(UserName=user)
            post_data = Post(
                Text=text,
                Created=datetime.now(),
                User=user_data
            )
            post_data.save()

            result = Post.objects.all().order_by('-id')[0:25]
            return render(
                request, 'postboard.html',
                {'result': result}
            )
        else:
            return render(
                request, 'add_post.html',
                {'error': 'ERROR: Unable to publish post. User with that name not found'}
            )
    return render(request, 'add_post.html')


def delete_post(request):
    """Delete Post of user"""
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_data = Post.objects.get(id=post_id)
        post_data.delete()
        result = Post.objects.all().order_by('-id')[0:25]
        return render(
            request, 'postboard.html',
            {'result': result}
        )

    result = Post.objects.all().order_by('-id')[0:25]
    if not result:
        return render(
            request, 'postboard.html',
            {'error': 'ERROR: No posts found'}
        )
    else:
        return render(
            request, 'delete_post.html',
            {'result': result}
        )


def add_comment(request):
    """Create a new comment of user"""
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        user = request.POST.get('username')
        text = request.POST.get('comment')
        users = User.objects.filter(UserName=user)
        post_id = Post.objects.get(id=post_id)
        if users:
            comment_data = Comment(
                Text=text,
                Created=datetime.now(),
                User=user,
                Post=post_id
            )
            comment_data.save()

            comments_data = Comment.objects.filter(Post=post_id).order_by('-id')[0:25]
            return render(
                request, 'comments.html',
                {'comments_data': comments_data}
            )
        else:
            return render(
                request, 'add_comment.html',
                {'error': 'ERROR: Unable to publish comment. User with that name not found'}
            )

    result = Post.objects.all()
    if not result:
        return render(
            request, 'add_comment.html',
            {'error': 'ERROR: No posts found. Please create your first post and show it to the world'}
        )
    return render(
        request, 'add_comment.html',
        {'result': result}
    )


def get_comments(request):
    """Get comments of user for the Post"""
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        sort_by = request.POST.get('sort')
        comments_data = Comment.objects.filter(Post=post_id)
        if comments_data:
            if sort_by == '1':
                comments_data = Comment.objects.filter(Post=post_id).order_by('User')
                return render(
                    request, 'comments.html',
                    {'comments_data': comments_data}
                )
            elif sort_by == '2':
                comments_data = Comment.objects.filter(Post=post_id).order_by('Created')
                return render(
                    request, 'comments.html',
                    {'comments_data': comments_data}
                )
            return render(
                request, 'comments.html',
                {'comments_data': comments_data}
            )
        else:
            return render(
                request, 'comments.html',
                {'error': 'ERROR: No comments found for this post. Please try again'}
            )
    result = Post.objects.all()
    users = User.objects.all()
    if not result:
        return render(
            request, 'comments.html',
            {'error': 'ERROR: No posts found. Please create your first post or comment and show it to the world'}
        )
    else:
        return render(
            request, 'comments.html',
            {'result': result, 'users': users}
        )


def delete_comment(request):
    """Delete comment of user"""
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        comment_data = Comment.objects.get(id=comment_id)
        comment_data.delete()
        return redirect('comments')

    result = Comment.objects.all().order_by('-id')[0:25]
    if not result:
        return render(
            request, 'comments.html',
            {'error': 'ERROR: No comments found'}
        )
    else:
        return render(
            request, 'delete_comment.html',
            {'result': result}
        )


def update_user(request):
    """Update user data"""
    if request.method == "POST":
        user = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        captcha = request.POST.get('captcha')
        homepage = request.POST.get('homepage')
        user_data = User.objects.filter(UserName=user)
        if not user_data:
            return render(
                request, 'update_user.html',
                {'error': 'ERROR: User with that name not found'}
            )
        # email
        elif 100 < len(email) < 12:
            return render(
                request, 'update_user.html',
                {'error': 'ERROR: Email is too short. Minimum length is 12 and maximum length is 100'}
            )
        elif re.search(r'[^a-zA-Z0-9@._]', email):
            return render(
                request, 'update_user.html',
                {'error': 'ERROR: Invalid email format'}
            )
        # password
        elif 20 < len(password) < 4:
            return render(
                request, 'update_user.html',
                {'error': 'ERROR: Password is too short. Minimum length is 4 and maximum length is 20'}
            )
        elif password != request.POST.get('password2'):
            return render(
                request, 'update_user.html',
                {'error': 'ERROR: Passwords do not match'}
            )
        elif re.search(r'[^a-zA-Z0-9]', password):
            return render(
                request, 'update_user.html',
                {'error': 'ERROR: Password must contain only letters and numbers'}
            )
        # captcha
        elif 100 < len(captcha) < 2:
            return render(
                request, 'update_user.html',
                {'error': 'ERROR: CAPTCHA is too short. Minimum length is 2 and maximum length is 100'}
            )
        elif re.search(r'[^a-zA-Z0-9]', captcha):
            return render(
                request, 'update_user.html',
                {'error': 'ERROR: CAPTCHA must contain only letters and numbers'}
            )
        # homepage
        elif re.search(r'[^ht+ps:/?]', homepage):
            return render(
                request, 'update_user.html',
                {'error': 'ERROR: Invalid homepage format'}
            )
        # update user data and save it to DB
        elif email:
            user_data = User.objects.get(UserName=user)
            user_data.Email = email
            user_data.Password = user_data.Password
            user_data.HomePage = user_data.HomePage
            user_data.CAPTCHA = user_data.CAPTCHA
            user_data.save()
            return redirect('login')
        elif password:
            user_data = User.objects.get(UserName=user)
            user_data.Email = user_data.Email
            user_data.Password = password
            user_data.HomePage = user_data.HomePage
            user_data.CAPTCHA = user_data.CAPTCHA
            user_data.save()
            return redirect('login')
        elif captcha:
            user_data = User.objects.get(UserName=user)
            user_data.Email = user_data.Email
            user_data.Password = user_data.Password
            user_data.HomePage = user_data.HomePage
            user_data.CAPTCHA = captcha
            user_data.save()
            return redirect('login')
        elif homepage:
            user_data = User.objects.get(UserName=user)
            user_data.Email = user_data.Email
            user_data.Password = user_data.Password
            user_data.HomePage = homepage
            user_data.CAPTCHA = user_data.CAPTCHA
            user_data.save()
            return redirect('login')
    return render(request, 'update_user.html')


def delete_user(request):
    """Delete user data"""
    if request.method == "POST":
        user = request.POST.get('username')
        user_data = User.objects.filter(UserName=user)
        if not user_data:
            return render(
                request, 'delete_user.html',
                {'error': 'ERROR: User with that name not found'}
            )
        user_data.delete()
        return redirect('login')
    return render(request, 'delete_user.html')











