from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') # 작성자 표시
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일시
    voter = models.ManyToManyField(User, related_name='voter_question')  # voter 추가 추천기능때 사용할 것
    # ManyToManyField 다대다 관계 voter = models.ManyToManyField(User)는 추천인 voter 필드를 ManyToManyField 관계로 추가한 것이다
    n_hit = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.subject

    @property
    def update_counter(self):
        self.n_hit = self.n_hit + 1
        self.save()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer') # 작성자 표시
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정일시
    voter = models.ManyToManyField(User, related_name='voter_answer')


# 댓글 모델
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 댓글 작성자
    content = models.TextField() # 댓글 내용
    create_date = models.DateTimeField() # 댓글 작성일시
    modify_date = models.DateTimeField(null=True, blank=True) # 댓글 수정일시
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE) # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE) # 이 댓글이 달린 답변

