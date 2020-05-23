from django.shortcuts import render


def start(request):
    # return render(request, '/home/ubpc/promise/frontend/build/index.html')
    return render(request, 'index.html')
    # return render(request, '/home/arty/PycharmProjects/vladBalandin/config/static/index.html')


def sitemap(request):
    # return render(request, '/home/ubpc/promise/frontend/build/index.html')
    return render(request, 'sitemap.xml')


def robots(request):
    # return render(request, '/home/ubpc/promise/frontend/build/index.html')
    return render(request, 'robots.txt')
