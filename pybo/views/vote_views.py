from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer


# 질문 추천 함수
@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo 질문추천등록
    이때 자기 추천 방지를 위해 추천자와 글쓴이가 동일하면 추천 시 오류가 발생하도록 하였다
    Question 모델의 voter 필드는 ManyToManyField로 정의했으므로 question.voter.add(request.user)와
    같이 add 함수로 추천인을 추가해야 한다.
    같은 사용자가 하나의 질문을 여러 번 추천해도 추천 수가 증가하지는 않는다. ManyToManyField는 중복을 허락하지 않는다.
    """

    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)


# 답변 추천 함수
@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    파이보 답글추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없다.')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)
