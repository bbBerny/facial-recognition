from django.shortcuts import render
import os
from django.conf import settings
import markdown2 as mk
from django.http import HttpResponse

# Create your views here.
def  index(request):
    # Read md file
    readme_path = os.path.join(settings.BASE_DIR, 'readme.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Extract title
    first_line = md_text.splitlines()[0] if md_text else 'Title not found!'
    project_title = first_line.lstrip('# ').strip() if md_text else 'Project!'

    # Convert markdown to html
    content_html = mk.markdown(md_text, extras=['fenced-code-blocks', 'tables'])
    template_name = 'MainApp/index.html'
    return render(
        request,
        template_name,
        {'project_title': project_title,
                'content': content_html
         })

def login(request):
    return HttpResponse('Login Page')

def logout(request):
    return HttpResponse('Logout Page')

def register(request):
    return HttpResponse('Register Page')