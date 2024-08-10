from django.shortcuts import render, redirect

from apps.tags.models import Tag

# Create your views here.
def create_tag(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        tags = Tag.objects.all()
        lst = []
        for tag in tags:
            if tag.title == title:
                lst.append(title)
        if lst == []:
            result = Tag.objects.create(title=title)

        return redirect("/category")

    return render(request, 'base/create_tag.html', locals())