from django.http import HttpResponse


def home(request):
    return HttpResponse('''
    <h1>Unique Accent API</h1>
    <h2>Click on this link
    <a href="https://documenter.getpostman.com/view/6304969/TzJvcbyP">
    <small>(https://documenter.getpostman.com/view/6304969/TzJvcbyP)</small>
    </a> 
    to view the Postman documentation
    </h2>
    ''')
