from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'HomeWay - Главная',
        'background': 'static/main/img/header_bg.jpg'
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'HomeWay - О компании',
        'background': 'static/main/img/about_bg.jpg'
    }
    return render(request, 'main/about.html', data)


def error(request):
    data = {
        'title': 'Страница не найдена'
    }

    return render(request, 'main/404.html', data)


def work(request):
    data = {
        'title': 'HomeWay - Работа в компании',
        'background': 'static/main/img/work-bg.jpg'
    }
    return render(request, 'main/homeway.html', data)


def footer(request):
    return render(request, 'main/footer.html')


def footer_light(request):
    return render(request, 'main/footer-light.html')
