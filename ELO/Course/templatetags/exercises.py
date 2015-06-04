#coding: utf-8

## @file exercises.py
#   Este é o arquivo de cria a template tag {% exercise %}.
#
#   Ele é responsável por definir o funcionamento e o comportamento da tag
# perante todas as suas 4 diferentes utilizações.
#   O processo de renderização de um template dentro do Django compreende
# dois processos; no primeiro, as template e html tags são traduzidas em nodes
# que, no segundo processo, voltam a se tornar o html correspondente à página
# final.

from django import template

from Course.forms import *
from Course.macros import ExerciseType, FORM_WRAPPER, DND_WRAPPER

import ELO.locale.index as lang

## Variável necessária para inicializar tags e filters dentro do Django.
register = template.Library()

## Função chamada no momento da inserção do tag no template.
#
#   Essa função é a responsável por preparar o node do template no momento
# da compilação do arquivo html. Para mais informações, ler documentação
# do arquivo exercises.py.
#   No caso da tag {% exercise %}, ela deve ser responsável por preparar uma
# form de exercício no template, independentemente do seu tipo.
@register.tag
def exercise(parser, token):

    toklist = token.split_contents()

    ## @if
    #   Responsável pelo processamento no caso do usuário utilizar a tag
    # {% exercise %}.
    #
    #   Nesse caso, a tag não irá passar argumentos adicionais para o Node.
    #   Utilize esta tag caso você tenha uma variável no contexto chamada
    #   "exercise" (sem aspas) que contenha o objeto retornado pelo método
    #   IfBusCourse.createExercise().
    if len(toklist) == 1:
        return ExerciseToken()

    ## @if
    #   Responsável pelo processamento no caso do usuário utilizar as tags
    # {% exercise arg1 %} ou {% exercise "arg1" %}.
    #
    #   Nesse caso, a tag passará exatamente um argumento para o Node.
    #
    #   Utilize a tag {% exercise arg1 %} quando arg1 for um objeto no seu
    # contexto retornado pelo método IfBusCourse.createExercise().
    #
    #   Utilize a tag {% exercise "arg1" %} quando arg1 for uma string de
    # formatação válida.
    #   Strings de formatação válidas para essa tag são strings do tipo:
    #       *[%_[*]]
    #   Ou seja, são strings simples, ou duas strings separadas pela string
    # de escape '%_'.
    #   Essa string de formatação serve para adicionar um anunciado
    # dentro da form de exercício. É mais utilizado para exercícios do tipo
    # ExerciseType.FillTheBlank. Os campos de input serão inseridos no lugar
    # do %_.
    if len(toklist) == 2:
        return ExerciseToken.halfTag(toklist[1])

    ## Mensagem de erro para quantidade inapropriada de argumentos para a tag.
    exc_msg = lang.DICT['TEMPLATE_TAG_MA'] % token.contents.split()[0]

    ## @if
    #   Responsável pelo processamento no caso do usuário utilizar a tag
    # {% exercise arg1 "arg2" %}
    #
    #   Nesse caso, a tag passará exatamente dois argumentos para o Node.
    #
    #   Utilize esta tag caso arg1 for um objeto no seu contexto retornado pelo
    # método IfBusCourse.createExercise() e arg2 for uma string de formatação
    # válida.
    #   Strings de formatação válidas para essa tag são strings do tipo:
    #       *[%_[*]]
    #   Ou seja, são strings simples, ou duas strings separadas pela string
    # de escape '%_'.
    #   Essa string de formatação serve para adicionar um anunciado
    # dentro da form de exercício. É mais utilizado para exercícios do tipo
    # ExerciseType.FillTheBlank. Os campos de input serão inseridos no lugar
    # do %_.
    if len(toklist) == 3:

        exerciseName = toklist[1]
        formatString = toklist[2]

        if formatString[0]!=formatString[-1] or formatString not in ["'",'"']:
            raise template.TemplateSyntaxError(exc_msg)
        else:
            return ExerciseToken.completeTag(exerciseName, formatString[1:-1])
    else:
        raise template.TemplateSyntaxError(exc_msg)

## Classe do tipo Node responsável pela renderização da tag {% exercise %}.
class ExerciseToken(template.Node):

    exercise = None
    formatString = None

    ## Construtor chamado no caso da criação ser feita através da tag
    #   {% exercise %}
    def __init__(self): pass

    ## Construtor chamado no caso da criação ser feita através da tag
    #   {% exercise arg1 "arg2" %}.
    @classmethod
    def completeTag(cls, exercise, formatString):
        ex = cls()
        ex.exercise = exercise
        ex.formatString = formatString.split("%_")
        return ex

    ## Construtor chamado no caso da criação ser feita através da tag
    #   {% exercise arg1 %} ou {% exercise "arg1" %}.
    @classmethod
    def halfTag(cls, token):
        ex = cls()
        if token[0] == token[-1] and token[0] in ["'", '"']:
            ex.formatString = token[1:-1].split("%_")
        else:
            ex.exercise = token
        return ex

    ## Método chamado pelo Django para a renderização do nó no contexto.
    def render(self, context):
        try:
            if not self.exercise:
                exerciseNode = context['exercise']
            else:
                exerciseNode = self.exercise.resolve(context)

            if not self.formatString:
                self.formatString = ["", ""]
            elif len(self.formatString) < 2:
                self.formatString.append("")

            wrapper = FORM_WRAPPER

            if exerciseNode.type == ExerciseType.MultipleChoice:
                exercise = MultipleChoiceExercise(exerciseNode.options)()

            elif exerciseNode.type == ExerciseType.FillTheBlank:
                exercise = FillTheBlankExercise()

            elif exerciseNode.type == ExerciseType.CrossWords:
                exercise = CrossWordsExercise()
                init_str = "_".join(exerciseNode.words)
                exercise.fields['bloat'].initial = init_str

            elif exerciseNode.type == ExerciseType.Unscramble:
                exercise = UnscrambleExercise()
                init_str = " ".join(exerciseNode.words)
                exercise.fields['bloat'].initial = init_str

            elif exerciseNode.type == ExerciseType.DragAndDrop:
                exercise = DragAndDropExercise()
                exercise.fields['bloat'].initial = init_str
                wrapper = DND_WRAPPER

            else:
                exercise = ''

            if exercise != '':
                exercise.fields['exercise_id'].initial = exerciseNode.id

            return wrapper(exercise,
                                exerciseNode.csrf,
                                self.formatString)

        except template.VariableDoesNotExist:
            return ""
