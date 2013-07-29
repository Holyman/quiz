from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from models import *

class ChoiceInline(admin.TabularInline):
    """
    This is the ChoiceInline found in the admin Question interface.
    """

    model = Choice
    fields = ['answer', 'id', 'correct']
    readonly_fields = ['id']
    max_num = 4


class AdminQuestion(admin.ModelAdmin):
    """
    This is the admin Question interface. It contains an instance of the
    Question model and the ChoiceInline.
    """

    fieldsets = [
        (None, {'fields': ['question']})
    ]
    inlines = [ChoiceInline]
    list_display = ['question', 'correct_answer_string', 'id']


class UserAnswerInline(admin.TabularInline):
    """
    This is the UserAnswerInline found in the admin User interface. It displays
    all the UserAnswers bound to the current user.
    """

    model = UserAnswer
    fields = ['question', 'choice', 'is_correct']
    readonly_fields = ['question', 'choice', 'is_correct']
    # can_delete = False
    extra = 0

    def has_add_permission(self, request):
        """
        This function overrides the default and removes the "add" button.
        """
        return False


class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'has_taken_quiz', 'num_correct_answers']
    readonly_fields = ['user', 'num_correct_answers', 'has_taken_quiz']
    inlines = [UserAnswerInline]
    list_display = ['__unicode__', 'has_taken_quiz', 'num_correct_answers']

admin.site.register(Question, AdminQuestion)
admin.site.register(UserProfile, UserProfileAdmin)

