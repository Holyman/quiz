from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Question(models.Model):
    """
    This is the question model. It only contains the question-string, but the
    Choice model has a foreignkey realtionship to it.
    """

    question = models.CharField(max_length=100)

    def __unicode__(self):
        return self.question

    def is_correct(self, choice_id):
        """
        This function checks if a choice given by its id is in the choice_set of
        a question and if the choice is marked as correct
        Input: Question object(self) and Choice id
        Output: Boolean. Returns True if choice is in the choice set and choice
        itself is True. Returns False in all other cases.
        """

        try:
            choice = Choice.objects.get(id=choice_id)
            if choice in self.choice_set.all() and choice.is_correct():
                return True
        except Error:
            return False
        return False

    def correct_answer_string(self):
        """
        This function returns a string of the correct answers, so it can be used
        in the Question list_view.
        """
        correct_answers = self.choice_set.filter(correct=True)
        string = ""
        for a in correct_answers:
            string += a.__unicode__() + ", "
        string = string[:-2]
        return string

class Choice(models.Model):
    """
    This model contains a single answer, and a boolean to set the answer True
    or False. It has a foreignkey relationship to the Question model. Every
    Question instance will have several choices bound to it.
    """

    answer = models.CharField(max_length=100)
    correct = models.BooleanField()
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.answer

    def is_correct(self):
        return self.correct


class Quiz(models.Model):
    """
    This is the class for the QuizInline in the admin User interface. It is not
    used atm.
    """

    user = models.OneToOneField(User)
    answer_string = models.CharField(max_length=100, null=True, blank=True)
    num_correct_answers = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'quizzes'

    def __unicode__(self):
        return "User: %s ; Answer string: %s" % (self.user, self.answer_string)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    has_taken_quiz = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s's profile" % self.user

    def num_correct_answers(self):
        """
        This function dynamically finds the number of correct answers for this
        UserProfile, every time user_profile.num_correct_answers() is called.
        """
        answers = self.useranswer_set.all()
        if not answers:
            return 0

        num_correct = 0
        for a in answers:
            if a.is_correct():
                num_correct += 1
        return num_correct

    def has_taken_quiz(self):
        """
        This function checks if the UserProfile has any UserAnswers. Returns
        True if set is not empty and False in all other cases.
        """
        if self.useranswer_set.all():
            return True
        return False

    def answers(self):
        """
        This function dynamically finds the number of correct answers for this
        UserProfile, every time user_profile.num_correct_answers() is called.
        """
        answers = self.useranswer_set.all()

        return answers
 


def create_user_profile(sender, instance, created, **kwargs):
    profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class UserAnswer(models.Model):
    """
    This model contains a relationship between a single User instance and a
    single Choice instance. If a User answers 10 questions, then the User will
    have 10 instances of this class bound to itself.
    """

    userprofile = models.ForeignKey(UserProfile)
    choice = models.ForeignKey(Choice)

    def __unicode__(self):
        return self.choice.question.__unicode__() + "     Bruker svarte: " \
            + self.choice.__unicode__() +  "     Riktig svar: " \
            + self.choice.question.correct_answer_string()

    def question(self):
        """
        This function makes if possible to use "question" as a field in
        UserAnswerInline.
        """

        return self.choice.question

    def choise(self):
        """
        This function makes if possible to use "question" as a field in
        UserAnswerInline.
        """

        return self.choice

    def correct(self):
        """
        This function makes if possible to use "question" as a field in
        UserAnswerInline.
        """

        return self.choice.question.correct_answer_string()

    def is_correct(self):
        return self.choice.is_correct()



