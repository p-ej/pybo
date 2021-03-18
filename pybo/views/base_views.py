from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator # 페이징
from django.db.models import Q, Count
from ..models import Question


# 질문 목록 기능 구현하기
def index(request):
    """
    파이보 목록 출력
    [GET 방식 요청 URL 예]
    localhost:8000/pybo/?page=1
    get('page', '1')에서 '1'은 /pybo/ URL처럼 page 파라미터가 없는 URL을 위해 기본값으로 1을 지정한 것이다. 페이징 구현에 사용한 클래스는 Paginator이다.
    """
    # 입력 파라미터
    page = request.GET.get('page','1') # 페이지
    kw = request.GET.get('kw','') # 검색어
    # index 함수를 자세히 살펴보자. page = request.GET.get('page', '1')은 다음과 같은 GET 방식 요청 URL에서 page값을 가져올 때 사용한다.
    so = request.GET.get('so','recent') # 정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter','-create_date')
        # 추천순(추천 수가 같으면 최신순으로 정렬한다.)
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
        # 인기 답변이 많이 달림순
    else:  # recent
        question_list = Question.objects.order_by('-create_date')
        # 최근 등록된 질문

    # 조회

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)| # 제목검색 , icontains는 대소문자 가리지 않고 검색을 해줌
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw) # 답변 글쓴이
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so} # page와 kw가 추가됨
    # 입력으로 받은 page와 kw값을 템플릿 searchForm에 전달하기 위해 context 안에 'page', 'kw'를 각각 page, kw으로 추가했다.
    return render(request, 'pybo/question_list.html', context)
    # pybo/question_list.html 이것을 템플릿이라고 함. MVC MVT 패턴
    # context = {'question_list': question_list}


def detail(request, question_id):
    """
    파이보 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id) # 404에러가 날시 표시
    # question = Question.objects.get(id=question_id)
    context = {'question': question}

    return render(request, 'pybo/question_detail.html', context)