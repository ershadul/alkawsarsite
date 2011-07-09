# -*- coding: utf-8 -*-

import math

from django.http import *
from django.conf import settings
from django.http import *
from django.shortcuts import render_to_response

from alkawsarsite.articles.models import Article
from alkawsarsite.authors.models import Author
from alkawsarsite.issues.models import Issue
from alkawsarsite.sections.models import Section
from alkawsarsite.languages import default_language
from alkawsarsite.languages import is_valid_language
from alkawsarsite.fatawas.models import Fatawa
from alkawsarsite.studentadvices.models import StudentAdvice
from alkawsarsite.questions.forms import QuestionForm
from alkawsarsite.questions.models import Question
from alkawsarsite.topics.models import Topic
from alkawsarsite.utils.paginator import DiggPaginator as Paginator

def index(request):
    
    sections = []
    regular_sections = request.current_issue.sections.filter(is_regular=True).all()
    other_articles = Article.objects.filter(
                            issue=request.current_issue,
                            is_published=True
                            ).exclude(section__in=regular_sections).order_by('order', 'id').all()
    
    for section in regular_sections:
        section.articles = section.article_set.filter(issue=request.current_issue).all()
        sections.append(section)

    popular_articles = Article.objects.filter(is_published=True, language=request.language).order_by('-n_clicks').all()[:10]

    return render_to_response('new_layout.html',
            {'language': request.language, 
             'issue' : request.current_issue,
             'back_issues': request.back_issues, 
             'other_articles': other_articles,
             'locals': request.locals,
             'user': request.user,
             'sections': sections,
             'popular_articles': popular_articles
             }
    )

def issue_fatawas(request, year, month):
    try:
        section = Section.objects.filter(language=request.language, slug_title='question-answer').all()[0:1].get()
        issue = Issue.objects.filter(year=year, month=month, language=request.language).all()[0:1].get()
        other_sections = issue.sections.exclude(id=section.id).all()
    except Exception, e:
        raise Http404
    fatawa_set = Fatawa.objects.filter(issue=issue, is_published=True).order_by('serial').all()
    
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    paginator = Paginator(fatawa_set, settings.FATAWA_PAGESIZE)
    try:
        page = paginator.page(page_number)
        fatawas = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        fatawas = page.object_list
    
    return render_to_response('fatawas.html', 
            {
             'language': request.language, 
             'issue' : issue,
             'current_issue': request.current_issue,
             'back_issues': request.back_issues, 
             'locals': request.locals,
             'user': request.user,
             'fatawas': fatawas,
             'page': page,
             'section': section,
             'other_sections': other_sections
             }
    )

def all_fatawas(request):
    
    section = Section.objects.filter(language=request.language, slug_title='question-answer').all()[0:1].get()
    sections = Section.objects.filter(is_published=True, language=request.language).all()
    fatawa_set = Fatawa.objects.filter(is_published=True, language=request.language).order_by('-serial').all()
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    paginator = Paginator(fatawa_set, settings.FATAWA_PAGESIZE)
    try:
        page = paginator.page(page_number)
        fatawas = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        fatawas = page.object_list
    
    return render_to_response('all_fatawas.html', 
            {
             'language': request.language, 
             'section': section,
             'locals': request.locals,
             'user': request.user,
             'fatawas': fatawas,
             'page': page,
             'sections': sections, 
             'current_issue': request.current_issue,
             'back_issues': request.back_issues, 
             }
    )

def issue_advices(request, year, month):
    try:
        section = Section.objects.filter(language=request.language, slug_title='student-advicing').all()[0:1].get()
        issue = Issue.objects.filter(year=year, month=month, language=request.language).all()[0:1].get()
        other_sections = issue.sections.exclude(id=section.id).all()
    except Exception, e:
        raise Http404
    
    advice_set = StudentAdvice.objects.filter(issue=issue, is_published=True).all()
    
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    paginator = Paginator(advice_set, settings.FATAWA_PAGESIZE)
    try:
        page = paginator.page(page_number)
        advices = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        advices = page.object_list
        
    return render_to_response('advices.html', 
            {
             'language': request.language, 
             'issue' : issue,
             'current_issue': request.current_issue,
             'back_issues': request.back_issues, 
             'locals': request.locals,
             'user': request.user,
             'advices': advices,
             'page': page,
             'section': section,
             'other_sections': other_sections
             }
    )
    
def all_advices(request):
    section = Section.objects.filter(language=request.language, slug_title='student-advicing').all()[0:1].get()
    sections = Section.objects.filter(is_published=True, language=request.language).all()
    advice_set = StudentAdvice.objects.filter(language=request.language, is_published=True).order_by('-serial').all()
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    paginator = Paginator(advice_set, settings.FATAWA_PAGESIZE)
    try:
        page = paginator.page(page_number)
        advices = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        advices = page.object_list
    return render_to_response('all_advices.html', 
            {
             'language': request.language, 
             'section': section,
             'locals': request.locals,
             'user': request.user,
             'advices': advices,
             'page': page,
             'sections': sections, 
             'current_issue': request.current_issue,
             'back_issues': request.back_issues, 
             }
    )
    
def show_issue(request, year, month):
    try:
        issue = Issue.objects.filter(year=year, month=month, language=request.language).all()[0:1].get()
    except:
        raise Http404
    
    sections = []
    regular_sections = issue.sections.filter(is_regular=True).all()
    other_articles = Article.objects.filter(
                            issue=issue,
                            is_published=True
                            ).exclude(section__in=regular_sections).all()
    
    for section in regular_sections:
        section.articles = section.article_set.filter(issue=issue).all()
        sections.append(section)
    popular_articles = Article.objects.filter(is_published=True).order_by('-n_clicks').all()[:10]
    return render_to_response('new_layout.html',
            {'language': request.language, 
             'issue' : issue,
             'current_issue': request.current_issue,
             'back_issues': request.back_issues, 
             'locals': request.locals,
             'user': request.user,
             'other_articles': other_articles,
             'sections': sections,
             'popular_articles': popular_articles
             }
    )

def back_issues(request):
    issues = Issue.objects.filter(language=request.language, is_published=True, is_default=False).all()
    return render_to_response('back_issues.html',
            {'language': request.language, 
             'back_issues': issues,
             'locals': request.locals,
             'user': request.user
             }
    )
    
def show_authors(request):
    author_list = Author.objects.filter(language=request.language).all()
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    paginator = Paginator(author_list, 10)
    try:
        page = paginator.page(page_number)
        authors = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        authors = page.object_list
        
    return render_to_response('authors.html', {
         'authors': authors,
         'language': request.language,
         'page': page,
         'locals': request.locals,
         'user': request.user,
         'current_issue' : request.current_issue,
         'back_issues': request.back_issues
         })

def show_author(request, slug_name):
    try:
        author = Author.objects.filter(slug_name=slug_name, language=request.language).all()[0:1].get()
    except Exception, e:
        raise Http404
    article_list = author.article_set.all()
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    paginator = Paginator(article_list, 10)
    try:
        page = paginator.page(page_number)
        related_articles = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        related_articles = page.object_list
    
    other_authors = Author.objects.filter(language=request.language).exclude(id=author.id).all()
    
    return render_to_response('author_page.html', 
        {
         'author': author,
         'page': page,
         'language': request.language,
         'locals': request.locals,
         'user': request.user,
         'current_issue' : request.current_issue,
         'back_issues': request.back_issues,
         'other_authors': other_authors,
         'related_articles': related_articles
        }
    )

def show_topic(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Exception, e:
        raise Http404
    article_list = topic.article_set.filter(is_published=True).all()
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    paginator = Paginator(article_list, 10)
    try:
        page = paginator.page(page_number)
        related_articles = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        related_articles = page.object_list
    
    #related_articles = topic.article_set.filter(is_published=True).all()
    other_topics = Topic.objects.filter(language=request.language).exclude(id=topic.id).order_by('name').all()

    return render_to_response('topic_page.html',
        {
         'topic': topic,
         'page': page,
         'language': request.language,
         'locals': request.locals,
         'user': request.user,
         'current_issue' : request.current_issue,
         'back_issues': request.back_issues,
         'other_topics': other_topics,
         'related_articles': related_articles
        }
    )

def contact(request):
    return render_to_response('contact_us.html', 
        {
         'language': request.language,
         'locals': request.locals,
         'user': request.user,
         'current_issue' : request.current_issue,
         'back_issues': request.back_issues
        }
    )

def about_us(request):
    return render_to_response('about_us.html', 
        {
         'language': request.language,
         'locals': request.locals,
         'user': request.user,
         'current_issue' : request.current_issue,
         'back_issues': request.back_issues
        }
    )

def change_language(request):
    language = request.GET.get('lang', default_language)
    if is_valid_language(language):
        request.language = language
    else:
        request.language = default_language
    return  HttpResponseRedirect('/')

def all_sections(request):
    sections = Section.objects.filter(language=request.language, is_published=True).all()
    return render_to_response('sections.html',
            {'language': request.language, 
             'sections': sections,
             'locals': request.locals,
             'user': request.user
             }
    )

def issue_section(request, year, month, slug_title):
    try:
        section = Section.objects.filter(slug_title=slug_title, language=request.language)[0:1].get()
        issue = Issue.objects.filter(year=year, month=month, language=request.language).all()[0:1].get()
        other_sections = issue.sections.exclude(id=section.id).all()
    except Exception, e:
        return HttpResponseNotFound('<h1>Page not fount</h1>')
    
    articles = section.article_set.filter(issue=issue, is_published=True).all()
    
    return render_to_response('issue_section_page.html',
            {
             'language': request.language, 
             'issue': issue,
             'current_issue': request.current_issue,
             'back_issues': request.back_issues, 
             'articles': articles, 
             'section': section,
             'other_sections': other_sections,
             'locals': request.locals,
             'user': request.user
            }
    )    
    
def show_section(request, slug_title):
    
    try:
        section = Section.objects.filter(slug_title=slug_title, language=request.language)[0:1].get()
    except Exception, e:
        #print e
        return HttpResponseNotFound('<h1>Page not fount</h1>')
    
    article_list = section.article_set.all()
    
    sections = Section.objects.filter(is_published=True, language=request.language).all()
    
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    paginator = Paginator(article_list, settings.PAGESIZE)
    try:
        page = paginator.page(page_number)
        articles = page.object_list
    except:
        page = paginator.page(paginator.num_pages)
        articles = page.object_list
            
    return render_to_response('section_page.html',
            {
             'language': request.language, 
             'sections': sections, 
             'current_issue': request.current_issue,
             'back_issues': request.back_issues, 
             'articles': articles, 
             'section': section,
             'page': page,
             'locals': request.locals,
             'user': request.user
            }
    )    

def show_article(request, guid):
    try:
        article = Article.objects.get(guid=guid)
        article.n_clicks += 1
        article.save()
        return HttpResponsePermanentRedirect(article.get_absolute_url())
    except:
        return HttpResponseNotFound('<h1>Article not found</h1>')
    
    other_section_articles = []
    other_issue_articles = []
    
    #if article.section:
    #    other_section_articles = article.section.article_set.exclude(guid=article.guid).filter(is_published=True).all()[0:10]
    if article.issue:
        other_issue_articles = article.issue.article_set.exclude(guid=article.guid).filter(is_published=True).all()
    
    return render_to_response('article_page.html', {
        'article': article,
        'issue': article.issue,
        'language': request.language,
        'locals': request.locals,
        'user': request.user,
        'current_issue' : request.current_issue,
        'back_issues': request.back_issues,
        #'other_section_articles': other_section_articles,
        'other_issue_articles': other_issue_articles
    })

def article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.n_clicks += 1
        article.save()
    except:
        return HttpResponseNotFound('<h1>Article not found</h1>')
    
    other_section_articles = []
    other_issue_articles = []
    
    #if article.section:
    #    other_section_articles = article.section.article_set.exclude(guid=article.guid).filter(is_published=True).all()[0:10]
    if article.issue:
        other_issue_articles = article.issue.article_set.exclude(guid=article.guid).filter(is_published=True).all()
    
    return render_to_response('article_page.html', {
        'article': article,
        'issue': article.issue,
        'language': request.language,
        'locals': request.locals,
        'user': request.user,
        'current_issue' : request.current_issue,
        'back_issues': request.back_issues,
        #'other_section_articles': other_section_articles,
        'other_issue_articles': other_issue_articles
    })
    
def show_article_print(request, guid):
    try:
        article = Article.objects.get(guid=guid)
        return HttpResponsePermanentRedirect(article.get_absolute_url() + '/print')
    except:
        return HttpResponseNotFound('<h1>Article not found</h1>')
    return render_to_response('article_print.html', {
        'article': article,
        'issue': article.issue,
        'language': request.language,
        'locals': request.locals,
        'user': request.user
        }
    )

def article_print(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except:
        return HttpResponseNotFound('<h1>Article not found</h1>')
    return render_to_response('article_print.html', {
        'article': article,
        'issue': article.issue,
        'language': request.language,
        'locals': request.locals,
        'user': request.user
    })

def help_font(request):
    return render_to_response('help_font.html',
        {
            'language': request.language, 
            'issue': request.current_issue,
            'current_issue': request.current_issue,
            'back_issues': request.back_issues, 
            'locals': request.locals,
            'user': request.user
        }
    )
    
def ask_question(request):
    data = {}
    errors = {}
    if request.method == 'POST':
        data = request.POST.copy()
        form = QuestionForm(data)
        if form.is_valid():
            try:
                qa = Question()
                qa.question = data['question']
                if request.user.is_authenticated():
                    qa.user = request.user
                else:
                    qa.name = data['name']
                    qa.email = data['email']
                    qa.url = data['url']
                qa.save()
                if request.language == 'bengali':
                    data['successful_msg'] = u'আলহামদুলিল্লাহ! আপনার প্রশ্নটি সফলভাবে সংগৃহীত হয়েছে ।'
                else:
                    data['successful_msg'] = 'Your question has been save successfully'
            except Exception, e:
                errors['exception'] = 'Sorry!, something wrong happend, we could not save your question'
        else:
            if request.language == 'bengali':
                if form.errors.has_key('question'):
                    errors['question'] = u'আপনার প্রশ্নটি টাইপ করুন'
                if form.errors.has_key('name'):
                    errors['name'] = u'আপনার নাম টাইপ করুন'
                if form.errors.has_key('email'):
                    errors['email'] = u'আপনার ইমেইল টাইপ করুন'
                if form.errors.has_key('url'):
                    errors['url'] = u'সঠিক ওয়েব ঠিকানা  টাইপ করুন'
            else:
                errors['question'] = 'Please type in your question'
    return render_to_response('ask_question.html',
        {'data': data,
         'errors': errors,
         'locals': request.locals,
         'language': request.language
         }
    )

def show404(request):
    return render_to_response('404.html')

def show500(request):
    return render_to_response('500.html', {'error_data': request.error_data })

def subscribe_agent(request):
    return render_to_response('subscriber_agent.html', {
        'language': request.language,
        'locals': request.locals,
        'user': request.user,
        'current_issue' : request.current_issue,
        'back_issues': request.back_issues,
    })