from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def profile(request):
    return render(request,'app-profile.html')
def calender(request):
    return render(request,'app-calender.html')
def chartist(request):
    return render(request,'chart-chartist.html')
def chartjs(request):
    return render(request,'chart-chartjs.html')
def flot(request):
    return render(request,'chart-flot.html')
def morris(request):
    return render(request,'chart-morris.html')
def peity(request):
    return render(request,'chart-peity.html')
def sparkline(request):
    return render(request,'chart-sparkline.html')
def compose(request):
    return render(request,'email-compose.html')
def inbox(request):
    return render(request,'email-inbox.html')
def read(request):
    return render(request,'email-read.html')
def summernote(request):
    return render(request,'form-editor-summernote.html')
def element(request):
    return render(request,'form-element.html')
def pickers(request):
    return render(request,'form-pickers.html')
def validation(request):
    return render(request,'form-validation-jquery.html')
def wizard(request):
    return render(request,'form-wizard.html')
def index2(request):
    return render(request,'index2.html')
def layout(request):
    return (request,'layout-blank.html')
def jqvmap(request):
    return render(request,'map-jqvmap.html')
def error400(request):
    return render(request,'page-error-400.html')
def error403(request):
    return render(request,'page-error-403.html')
def error404(request):
    return render(request,'page-error-404.html')
def error500(request):
    return render(request,'page-error-500.html')
def error503(request):
    return render(request,'page-error-503.html')
def lockscreen(request):
    return render(request,'page-lock-screen.html')
def login(request):
    return render(request,'page-login.html')
def register(request):
    return render(request,'page-register.html')
def bootstrap(request):
    return render(request,'table-bootstrap-basic.html')




    