from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    파이보 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # 추가한 속성 author 적용
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail', question_id=question.id), answer.id))
            # pybo:detail에 #answer_2와 같은 앵커를 추가하기 위해 format과 resolve_url 함수를 사용했다
            # resolve_url 함수는 실제 호출되는 URL을 문자열로 반환하는 장고 함수이다.
        form = AnswerForm()
    context = {'question': question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    파이보 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request,'수정권한이 없음')
        return redirect('pybo:detail', answer_id=answer.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(resolve_url('pybo:detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    파이보 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없음')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id = answer.question.id)