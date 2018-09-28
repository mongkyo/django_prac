import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def post_list(request):










    # template = loader.get_template('blog/post_list.html')
    # context = {}
    # content = template.render(context, request)
    # return HttpResponse(content)
    #




    # current_file = os.path.abspath(__file__)
    # blog_dir = os.path.dirname(current_file)
    # app_dir = os.path.dirname(blog_dir)
    # post_list_dir = os.path.join(app_dir, 'templates', 'blog', 'post_list.html')
    #
    #
    #  templates/blog/post_list.html파일의 내용을 읽어온 후,
    #  해당 내용을 아래에서 리턴해주는 HttpResponse인스턴스 생성시 인수로 넣어준다
    #  os.path.abspath(__file__)            <- 코드가 실행중인 파일의 경로를 나타냄
    #  os.path.dirname(<경로>)               <- 특정 경로의 상위 폴더로 이동
    #  os.path.join(<경로>, <폴더/파일명>)      <- 특정 경로에서 하위폴더 또는 하위 파일을 나타냄
    # with open(post_list_dir, 'rt') as f:
    #     content = f.read()
    # return HttpResponse(content)