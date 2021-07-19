import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',
        'views': 232},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
        'views': 132},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/'
        ,'views': 72} 
        ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'views': 38},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/',
        'views': 64},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/',
        'views': 21} 
        ]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
        'views': 94},
        {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'views': 86} 
        ]

    categories = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }


    for cat, cat_data in categories.items():
        cat_views = cat_data['views']
        cat_likes = cat_data['likes']
        c = add_cat(cat, cat_views, cat_likes)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

# Print added categories
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}, Category Likes: {c.likes}, Category Views: {c.views}, Page View: {p.views}')

def add_page(category, title, url, views=0):
    p = Page.objects.get_or_create(category=category, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c 

# And start execution here:
if __name__ == '__main__':
    print('Start Rango population script...')
    populate()