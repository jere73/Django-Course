""" Posts.views"""
from django.shortcuts import render
# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Jesica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'name': 'Via Lactea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'Pepito perez',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    },
]

# Create your views here.
def lists_posts(request):
    """List existing posts."""
    
    return render(request, 'feed.html', {'posts': posts})