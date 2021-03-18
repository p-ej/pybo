from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    """
    파이보 질문등록
    """
    # 입력 데이터 저장
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid(): # form.is_valid 함수는 POST 요청으로 받은 form이 유효한지 검사한다.
            question = form.save(commit=False)
            # question = form.save(commit=False)는 form으로 Question 모델 데이터를 저장하기 위한 코드이다.
            # 여기서 commit=False는 임시 저장을 의미한다.
            # 즉, 실제 데이터는 아직 저장되지 않은 상태를 말한다.
            question.author = request.user  # 추가한 속성 author 적용
            question.create_date = timezone.now()

            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    파이보 질문수정
    질문 상세 화면에서 <수정>을 누르면 /pybo/question/modify/2/ 페이지가 GET 방식으로 호출되어 질문 수정 화면이 나타나고,
    질문 수정 화면에서 <저장하기>를 누르면 /pybo/question/modify/2/ 페이지가 POST 방식으로 호출되어 데이터 수정이 이뤄진다.
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request,'수정권한이 없으무니다.') # 오류를 위한 messages 모듈을 이용 (넌필드 오류에 해당)
        return redirect('pybo:detail', question_id=question.id) # 요청받은 유저와 질문의 작성자가 다를때

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question) # [질문 수정을 위해 값 덮어쓰기]
        # 위 코드는 조회한 질문 question을 기본값으로 하여 화면으로 전달받은 입력값들을 덮어써서 QuestionForm을 생성하라는 의미이다
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now() # [질문 수정일시를 현재일시로 저장]
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question) # [질문 수정 화면에 기존 제목, 내용 반영]
        # 이처럼 instance 매개변수에 question을 지정하면 기존 값을 폼에 채울 수 있다
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    파이보 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request,'삭제권한이 없으무니다.') # 오류를 위한 messages 모듈을 이용 (넌필드 오류에 해당)
        return redirect('pybo:detail', question_id=question.id) # 요청받은 유저와 질문의 작성자가 다를때
    question.delete()
    return redirect('pybo:index')