#coding: utf-8

## @file CourseUnit.py
#   Este arquivo é responsável pelo armazenamento de todas as camadas 
# correspondentes ao módulo de curso. 
#   O módulo de curso é responsável por mostrar aos alunos as lições, bem como
# administrar a resolução e correção de exercícios.
#   Para tal, uma única janela é criada, e chamadas assíncronas são realizadas
# para atualizar seu conteúdo, sendo elas chamadas de atualização de slides.
#   Slides podem conter fragmentos de lições ou exercícios, depenendo de que
# ponto da lição o usuário está navegando - ou do próprio módulo.
#   O aluno só deve ser capaz de prosseguir no curso (lê-se ir para a próxima
# lição/módulo) se tiver obtido uma pontuação mínima na lição/módulo anterior.

from abc import*
from random import shuffle

import ELO.locale.index as lang

from ELO.models import Courses, Module, Lesson, Exercise, Student

from Course.forms import LessonForm
from Course.macros import LESSONS_URL, GENERAL_URL, EXERCISES_URL, ExerciseType

from django.middleware import csrf
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.forms import ValidationError
from django import template

## Interface da camada de Apresentação do módulo de Curso.
#   É responsável pelo devido processamento do frame de curso; seleção de
# curso, módulo, lição e slide; formatação dos templates de exercícios; 
# bem como o processamento do primeiro nível da administração dos dados
# submetidos em exercícios.
class IfUiCourse:
    __metaclass__ = ABCMeta

    ## Força a criação da camada subjacente.
    def __init__(self, bus):
        try:
            self.bus = bus
        except TypeError as exc:
            del self
            raise exc

    @property
    def bus(self):
        return self.__bus

    @bus.setter
    def bus(self, value):
        if isinstance(value, IfBusCourse):
            self.__bus = value
        else:
            raise TypeError("Expected IfBusCourse instance at UiCourse.__bus. Received " + str(type(value)) + " instead.")

    @bus.deleter
    def bus(self):
        del self.__bus

    ## run() é o principal método de qualquer classe de apresentação.
    #   Este método permite à Factory (ver MainUnit.py) dar controle
    #   do programa para este módulo.
    #
    #   @arg request    Objeto HttpRequest enviado pela requisição do navegador
    #
    #   @arg courseid   Identificador do curso.
    #                       Deve necessariamente ser um inteiro validado
    #                       através do objeto Id (vide BaseUnit.py).
    @abstractmethod
    def run(self, request, courseid=None): pass


## Interface da camada de Negócio do módulo de Curso.
#   É responsável pelo processamento inteligente dos dados, validação
# e recuperação de dados.
#   Esta camada é a interface necessária de comunicação entre a camada
# de apresentação - o usuário - e a camada de persistência - o servidor.
class IfBusCourse:
    __metaclass__ = ABCMeta

    ## Garante a criação da camada subjacente.
    def __init__(self, pers):
        try:
            self.pers = pers
        except TypeError as exc:
            del self
            raise exc

    @property
    def pers(self):
        return self.__pers
    
    @pers.setter
    def pers(self, value):
        if isinstance(value, IfPersCourse):
            self.__pers = value
        else:
            raise TypeError("Expected IfPersCourse instance at BusCourse.__pers. Received " + str(type(value)) + "instead.")

    @pers.deleter
    def pers(self):
        del self.__pers


    ## Método que recupera uma lista dos módulos ou lições.
    #
    #   @arg user       Objeto usuário, como no contido no cookie user.
    #
    #   @arg accesstype String contendo "MODULE", "LOCK" ou "LESSON"
    #
    #   @return         Lista contendo todas os módulos cadastrados,
    #                       lições destravadas ou cadastrados para o
    #                       usuário 'user', variando sob o argumento
    #                       accesstype.
    @abstractmethod
    def getCompleted(self, user, accesstype): pass

    ## Método que recupera um objeto que representa um curso.
    #
    #   @arg user       Objeto usuário, como no contido no cookie user.
    #
    #   @arg courseid   Identificador do curso.
    #                       Deve ser um inteiro de acordo com o padrão de Id().
    #
    #   @return         Retorna um objeto curso com os seguintes atributos:
    #                       - NAME    : Identifica o nome do curso;
    #                       - ID      : Identifica univocamente o curso;
    #                       - STUDENTS: Lista de Ids de alunos cadastrados;
    #                       - MODULES : Lista de dicionários que representam
    #                                       cada um dos módulos.
    @abstractmethod
    def getCourse(self, user, courseid): pass

    ## Método que recupera um objeto que representa uma lição.
    #
    #   @arg lessonid   Identificador do curso.
    #                       Deve ser um inteiro de acordo com o padrão de Id().
    #
    #   @return         Retorna um objeto lição, com os seguintes atributos:
    #                       - url       : Caminho para a lição a partir de
    #                                     ELO/templates/Course/lessons/;
    #                       - name      : Nome da lição;
    #                       - slides    : Número de slides da lição em questão;
    #                       - exercises : Lista de ids de exercícios que a
    #                                       lição possui.
    @abstractmethod
    def getLesson(self, lessonid): pass

    ## Método que cria e formata um objeto que representa um exercício.
    #
    #   @arg ex_url     Objeto Link()-compatível que leva ao exercício.
    #   
    #   @arg request    Objeto request fornecido pelo navegador.
    #
    #   @return         Retorna um objeto exercício.
    @abstractmethod
    def createExercise(self, request, ex_url): pass

    ## Método que corrige um exercício.
    #
    #   @arg ex_url     Objeto Link()-compatível que leva ao exercício.
    #
    #   @arg answer     Resposta fornecida pelo usuário.
    #
    #   @return         Booleano: true significa certo e false, errado.
    @abstractmethod
    def correctExercise(self, ex_url, answer): pass


## Interface da camada de Persistência para o módulo de Curso.
#   Deve ser capaz de acessar de forma transparente o banco de dados.
#   Deve também ser a única forma de acessar tais dados dentro deste módulo.
class IfPersCourse:

    ## Pseudométodo que faz a chamada dos métodos atômicos desta camada.
    #
    #   @arg    s   self
    #
    #   @arg    x   field   Nome do campo a ser filtrado.
    #
    #   @arg    y   value   Valor que deve haver no campo.
    #
    #   @arg    z   dbase   Objeto do modelo a ser utilizado.
    #                           Deve ser importado de ELO.models.
    retrieve=lambda s,x,y,z: s.fetch(s.getid(x, y, z), z)

    ## Método que recupera o Id() de um objeto.
    #
    #   @arg field  Nome do campo a ser filtrado.
    #
    #   @arg value  Valor que deve haver no campo.
    #
    #   @arg db     Objeto do modelo a ser utilizado.
    #                   Deve ser importado de ELO.models.
    @abstractmethod
    def getid(self, field, value, db): pass

    ## Realiza uma pesquisa no banco de dados.
    #
    #   @arg id     Identificador do objeto requisitado.
    #                   Pode ser obtido através do método getid().
    #   
    #   @arg db     Objeto do modelo a ser utilizado.
    #                   Deve ser importado de ELO.models.
    @abstractmethod
    def fetch(self, id, db): pass


class UiCourse(IfUiCourse):

    def run(self, request, courseid=None):
        
        user = request.session['user']

        if request.method == "GET":
            if courseid:
                if courseid in map(lambda x: x["id"], user["courses"]):
                    course = self.bus.getCourse(user, courseid)
                    return render(request, GENERAL_URL("frame.html"), 
                        {'course':course})
                else:
                    ld = lang.DICT
                    raise PermissionDenied(ld["EXCEPTION_403_STD"])
            else:   
                raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])

        elif request.method == "POST":
            lesson_form = LessonForm(request.POST)
            try:
                if lesson_form.is_valid():
                    lessonid = lesson_form.cleaned_data['lesson_id']
                    lessonid = lessonid.value

                    slidenum = lesson_form.cleaned_data['slide_number']
                    slidenum = slidenum.value

                    gc = self.bus.getCompleted

                    if unicode(lessonid) not in gc(user, 'LOCK') and\
                       unicode(lessonid) not in gc(user, 'LESSON'):
                            ld = lang.DICT
                            raise PermissionDenied(ld["EXCEPTION_403_STD"])
                        

                    lesson = self.bus.getLesson(lessonid)

                    maxslides = lesson['slides']+len(lesson['exercises'])

                    if slidenum >= maxslides or slidenum < 0:
                        raise PermissionDenied(lang.DICT["EXCEPTION_403_STD"])

                    if slidenum < lesson['slides']:
                        lurl = lesson['url']
                        url = LESSONS_URL(lurl + "/" + str(slidenum) + ".html")

                        return render(request, url, { 'max': maxslides })
                    else:
                        exercise_id = slidenum - lesson['slides']
                        exercise_url = lesson['exercises'][exercise_id]
                        url = EXERCISES_URL(exercise_url + ".html")

                        exercise=self.bus.createExercise(request, exercise_url)

                        return render(request, url, { 'max': maxslides,
                                                      'exercise': exercise })
                else:
                    raise ValueError(lang.DICT['EXCEPTION_INV_LES'])
            except ValueError as exc:
                return render(request, GENERAL_URL("assync_std.html"),
                        {'error': exc})
                

class BusCourse(IfBusCourse):


    def getCompleted(self, user, accesstype):
        userdata = self.pers.retrieve('NAME', user['name'], Student)

        return userdata.get(accesstype + '_COMPLETED', [])

    def getCourse(self, user, courseid):
        compmlist = self.getCompleted(user, 'MODULE')
        compllist = self.getCompleted(user, 'LESSON')
        ulocklist = self.getCompleted(user, 'LOCK')
        coursedata = self.pers.fetch(courseid, Courses)
        modulelist = []
        
        for moduleid in coursedata['MODULE']:
            sfm = self.pers.fetch(moduleid, Module)
            modulename = sfm['NAME'][0]

            lessonlist = []

            for lessonid in sfm['LESSON']:
                lessoname = self.pers.fetch(lessonid, Lesson)['NAME']
                lessoncomplete = True if lessonid in compllist else False
                lessonunlocked = True if lessonid in ulocklist else False
                lessonlist = lessonlist + [{'id': lessonid,
                                            'name':lessoname[0],
                                            'complete':lessoncomplete,
                                            'unlocked':lessonunlocked }]

            modulelist = modulelist + [{'id':       moduleid,
                                        'name':     modulename,
                                        'lessons':  lessonlist,
                                        'complete':True \
                                            if moduleid in compmlist \
                                            else False
                                      }]
        
        coursedata['MODULE'] = sorted(modulelist, key=lambda x: x['id'])

        return coursedata

    def getLesson(self, lessonid):

        lessondata = self.pers.fetch(lessonid, Lesson)

        lesson = {}
        exercises_url = []
        lesson['url'] = lessondata['LINK'][0]
        lesson['name'] = lessondata['NAME'][0]
        lesson['slides'] = int(lessondata['SLIDES'][0])

        for e_id in lessondata['EXERCISE']:
            e_link = self.pers.fetch(e_id, Exercise)['LINK']
            exercises_url = exercises_url + e_link

        lesson['exercises'] = exercises_url

        return lesson

    def createExercise(self, request, ex_url):

        ex_data = self.pers.retrieve('LINK', ex_url, Exercise)

        exercise = {'url': ex_url, 
                    'type': int(ex_data['TYPE'][0]),
                    'csrf': csrf.get_token(request)}

        exerciseType = int(ex_data['TYPE'][0])

        ## Exercício de Múltipla Escolha.
        #
        #   TYPE: 1
        #   ITEM_k, k natural: nome da k-ésima opção
        #   CORRECT: k | k é a resposta correta
        if exerciseType == ExerciseType.MultipleChoice:
            options = []
            i = "1"
            while "ITEM_" + i in ex_data:
                options.append((int(i),ex_data["ITEM_" + i][0]))
                i = str(int(i)+1)

            exercise['options'] = options

        ## Exercício de preencher o vazio.
        #
        #   TYPE: 2
        #   CORRECT: uma das possíveis soluções
        elif exerciseType == ExerciseType.FillTheBlank:
            pass # nothing to do here

        ## Exercício de desembaralhar.
        #
        #   TYPE: 3
        #   WORD_k, k natural: k-ésima palavra a ser desembaralhada.
        elif exerciseType == ExerciseType.Unscramble:
            words = []
            i = "1"
            while "WORD_" + i in ex_data:
                words.append((int(i), ex_data["WORD_" + i][0]))
                i = str(int(i)+1)

            exercise['words'] = shuffle(words)

        ## Exercício de Palavras-cruzadas.
        #
        #   TYPE: 4
        #   WORD: palavra que pode ser dividida em xydw:
        #       x: coordenada x da primeira letra da palavra dentro da matriz;
        #       y: coordenada y da primeira letra da palavra dentro da matriz;
        #       d: direção em que a palavra cresce ('N', 'S', 'W', 'E');
        #       w: palavra propriamente dita.
        elif exerciseType == ExerciseType.CrossWords:
            wordList = []
            
            for word in ex_data["WORD"]:
                x,y,d,w = word.split()
                wordlist.append({'x':x,
                                 'y':y,
                                 'direction':d,
                                 'size':str(len(w)),})

            exercise['words'] = wordList

        ## Exercício de Arrastar e Soltar.
        #
        #   TYPE: 5
        #   ITEM_k, k natural: k-ésima imagem
        elif exerciseType == ExerciseType.DragAndDrop:
            images = []
            i = "1"

            while "ITEM_" + i in ex_data:
                images.append((int(i), ex_data["ITEM_" + i][0]))
                i = str(int(i)+1)

            shuffle(images)

            exercise['images'] = images
            exercise['number'] = len(images)

        return type("Exercise", (), exercise)

    def correctExercise(self, ex_url, answer):
        
        ex_data = self.pers.retrieve('LINK', ex_url, Exercise)
        exerciseType = int(ex_data['TYPE'][0])

        if exerciseType == ExerciseType.MultipleChoice:
            return True if answer == ex_data['CORRECT'][0] else False

        elif exerciseType == ExerciseType.FillTheBlank:
            return True if answer in ex_data['CORRECT'] else False

        elif exerciseType == ExerciseType.Unscramble:
            i = "1"
            while "WORD_" + i in ex_data:
                if answer[i] != ex_data["WORD_" + i]:
                    return False

            return True

        elif exerciseType == ExerciseType.CrossWords: pass
            for ans in ex_data["WORD"]:
                if not (ans in answer):
                    return False
            return True

        elif exerciseType == ExerciseType.DragAndDrop:
            i = "1"
            while "ITEM_" + i in ex_data:
                if ex_data["ITEM_" + i] != answer[i]:
                    return False

            return True

        else: return False


class PersCourse(IfPersCourse):

    def getid(self, field, value, db):
        model_data = db.objects.get(field=field, value=value)
        return model_data.identity

    def fetch(self, id, db):
        model_data = db.objects.filter(identity=id)
        format_data = {}

        ## @for
        #   Cria um dicionário de listas, no fomato:
        #
        #   CAMPO_NO_BANCO_DE_DADOS => [ VALOR_1, VALOR_2 ... VALOR_N ]
        for i in model_data.values():
            format_data[i['field']]=format_data.get(i['field'],[])+[i['value']]

        return format_data
