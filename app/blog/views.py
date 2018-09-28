from django.http import HttpResponse
from django.utils import timezone


def post_list(request):
    # 현재 지역에 맞는 날짜&시간 객체 할당
    current_time = timezone.now()
    """

    :param request: 실제 HTTP요청에 대한 정보를 가진 객체
    :return:
    """

    # templates/blog/post_list.html파일의 내용을 읽어온 후,
    # 해당 내용을 아래에서 리턴해주는 HttpResponse인스턴스 생성시 인수로 넣어준다
    # os.path.abspath(__file__)            <- 코드가 실행중인 파일의 경로를 나타냄
    # os.path.dirname(<경로>)               <- 특정 경로의 상위 폴더로 이동
    # os.path.join(<경로>, <폴더/파일명>)      <- 특정 경로에서 하위폴더 또는 하위 파일을 나타냄

    return HttpResponse()