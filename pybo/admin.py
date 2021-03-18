from django.contrib import admin
from .models import Question
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

    # search_field는 Gui의 label, textfiled 이런느낌인듯


admin.site.register(Question, QuestionAdmin)