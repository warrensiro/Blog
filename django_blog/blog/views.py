from django.shortcuts import render

posts = [
    {'author': 'Warren',
     'title': 'django',
     'date_posted': 'June 1',
     'content': 'New additions'},
    {'author': 'Siro',
     'title': 'Flask',
     'date_posted': 'June 2',
     'content': 'Even Newer additions'}
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Home'})
