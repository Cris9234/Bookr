from django.shortcuts import render


def index(request):
    title = "Welcome to Bookr"
    welcome = "Welcome to Bookr"
    name = "world"
    return render(request, "base.html", {"title": title, "welcome": welcome, "name": name})

def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-result.html", {"search_text": search_text})
