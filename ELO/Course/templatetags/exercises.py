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

from Course.forms import MultipleChoiceExercise
from Course.macros import ExerciseType, FORM_WRAPPER

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
    ## @try
    #   Responsável pelo processamento no caso do usuário utilizar a tag
    # {% exercise %}.
    #
    #   Nesse caso, a tag não irá passar argumentos adicionais para o Node.
    #   Utilize esta tag caso você tenha uma variável no contexto chamada
    #   "exercise" (sem aspas) que contenha o objeto retornado pelo método
    #   IfBusCourse.createExercise().
    try:
        tname = token.split_contents()
        return ExerciseToken()
    except ValueError: pass

    ## @try
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
    try:
        tname, tok = token.split_contents()
        return ExerciseToken(tok)
    except ValueError: pass

    ## Mensagem de erro para quantidade inapropriada de argumentos para a tag.
    exc_msg = lang.DICT['TEMPLATE_TAG_MA'] % token.contents.split()[0]

    ## @try
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
    try:
        tname, exerciseName, formatString = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(exc_msg)
    else:
        if formatString[0]!=formatString[-1] or formatString not in ["'",'"']:
            raise template.TemplateSyntaxError(exc_msg)
        else:
            return ExerciseToken(exerciseName, formatString[1:-1])


## Classe do tipo Node responsável pela renderização da tag {% exercise %}.
class ExerciseToken(template.Node):

    exercise = None
    formatString = None

    ## Construtor chamado no caso da criação ser feita através da tag
    #   {% exercise arg1 "arg2" %}.
    def __init__(self, exercise, formatString):
        self.exercise = exercise
        self.formatString = formatString.split("%_")

    ## Construtor chamado no caso da criação ser feita através da tag
    #   {% exercise arg1 %} ou {% exercise "arg1" %}.
    def __init__(self, token):
        if token[0] == token[-1] and token[0] in ["'", '"']:
            self.formatString = token[1:-1].split("%_")
        else:
            self.exercise = token

    ## Construtor chamado no caso da criação ser feita através da tag
    #   {% exercise %}
    def __init__(self): pass

    ## Método chamado pelo Django para a renderização do nó no contexto.
    def render(self, context):
        try:
            if not self.exercise:
                exerciseNode = context['exercise']
            else:
                exerciseNode = self.exercise.render(context)

            if not self.formatString:
                self.formatString = ["", ""]
            elif len(self.formatString < 2):
                self.formatString.append("")

            if exerciseNode.type == ExerciseType.MultipleChoice:
                exercise = MultipleChoiceExercise()
                exercise.fields['options'].choices = exerciseNode.options

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
                # something goes here, probably

            else:
                exercise = ''

            return FORM_WRAPPER(exercise, 
                                exerciseNode.csrf, 
                                self.formatString)

        except template.VariableDoesNotExist:
            return ""