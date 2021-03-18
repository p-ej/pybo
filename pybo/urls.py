from django.urls import path

from .views import base_views, question_views, answer_views, comment_views, vote_views

app_name = 'pybo' # namespace url 별칭사용을 위한 네임스페이스 지정

urlpatterns = [
    # URL 별칭 사용하기
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'), # 매핑완료 목록의 상세내용

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'), # 수정 버튼의 URL 매핑
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'), # 삭제 버튼의 URL 매핑

    # answer_views.py
    path('answer/create/<int:question_id>/',answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'), # 답변(댓글) 수정 url 매핑
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'), # 답변(댓글) 삭제 url 매핑

    # comment_views.py
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

    # 추천 vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
]