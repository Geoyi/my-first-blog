from django.shortcuts import render

def post_list(request):
    return render(request, 'geoyiblog/post_list.html', {})
