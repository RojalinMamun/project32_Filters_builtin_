from django.shortcuts import render

# Create your views here.

def built_in_filters(request):
    import datetime 
    dt=datetime.datetime.now()
    d={'data':'HELLo HoW aRe yOu','dt':dt,'c':5}
    return render(request,'built_in_filters.html',d)
