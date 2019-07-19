import requests
from django.http import HttpResponse
from django.shortcuts import render

def bio(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.

    bio_html = open("content/bio.html").read()
    pages = [{
             "link_title": "Bio",
             "link": "bio"
             },
             {
             "link_title": "Project",
             "link": "project"
             },
             {
             "link_title": "Contact",
             "link": "contact"
             }]
    context = {
        "content": bio_html,
        "pages": pages
    }
    return render(request, 'base.html', context)

def project(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    project_html = open("content/project.html").read()
    pages = [{
             "link_title": "Bio",
             "link": "bio"
             },
             {
             "link_title": "Project",
             "link": "project"
             },
             {
             "link_title": "Contact",
             "link": "contact"
             }]
    context = {
        "content": project_html,
        "pages": pages
    }
    return render(request, 'base.html', context)

def contact(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    contact_html = open("content/contact.html").read()
    pages = [{
             "link_title": "Bio",
             "link": "bio"
             },
             {
             "link_title": "Project",
             "link": "project"
             },
             {
             "link_title": "Contact",
             "link": "contact"
             }]
    context = {
        "content": contact_html,
        "pages": pages
    }
    return render(request, 'base.html', context)

def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/ypan710/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)
