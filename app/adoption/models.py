from django.db import models
from adopter.models import Adopter


class QuestionType(models.TextChoices):
    TEXT = 'text', 'Text'
    SELECT = 'select', 'Select'
    CHECKBOX = 'checkbox', 'Checkbox'

class Question(models.Model):
    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=QuestionType.choices)
    value = models.IntegerField(default=1)
    parent_question = models.ForeignKey('self', null=True, blank=True, related_name='sub_questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    value = models.IntegerField(default=1)

    def __str__(self):
        return self.text

class Questionnaire(models.Model):
    title = models.CharField(max_length=255)
    shelter = models.ForeignKey('shelter.Shelter', on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title

class AdoptionApplication(models.Model):
    user = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    pet = models.ForeignKey('pet.Pet', on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    answers = models.JSONField()

    def get_score(self):
        score = 0
        for question_id, answer in self.answers.items():
            question = Question.objects.get(id=question_id)
            if question.question_type == QuestionType.CHECKBOX:
                score += question.value if answer else 0
            else:
                option = question.options.filter(id=answer).first()
                if option:
                    score += option.value
        return score
