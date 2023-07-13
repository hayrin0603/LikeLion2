from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html')
def study(request):
    return render(request, 'study.html')
def introduce(request):
    return render(request, 'introduce.html')