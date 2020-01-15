""" Posts.views"""
from django.http import HttpResponse
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
    
    content = []
    
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}" /></figure>
        """.format(**post))

    return HttpResponse('<br>'.join(content))