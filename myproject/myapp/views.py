from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
        <h1>Главная страница</h1>
        <p>Добро пожаловать на сайт!</p>
    """)

def data_view(request):
    # Уникальное содержимое для страницы data
    return HttpResponse("""
        <h1>Страница Data</h1>
        <p>Это страница с важными данными:</p>
        <ul>
            <li>Данные 1</li>
            <li>Данные 2</li>
            <li>Данные 3</li>
        </ul>
    """)

def test_view(request):
    # Уникальное содержимое для страницы test
    return HttpResponse("""
        <h1>Страница Test</h1>
        <p>Это страница для тестирования. Здесь пример кода:</p>
        <pre>
        def hello():
            print("Привет, мир!")
        </pre>
    """)

