from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import MyStatus

# Create your views here.
def test_view(request):
    return HttpResponse("test_url")

# この下にトップページを作るよ
def stmn_top_page(request):
    my_status = MyStatus.objects.get(id=1)
    print(my_status)
    d = {
        "my_status": my_status
    }
    # print(my_status.get.nam)
    return render(request, 'mypage/index.html', d)

