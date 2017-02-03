from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta, timezone
from .models import *
from .forms import *


def create_article(request, id=None):

	template_name = "create_article.html"

	context = {}

	if not request.user.is_authenticated():
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/create/')
		return HttpResponseRedirect('/login/')

	if request.POST and request.POST['title']:
		form = ArticleForm(request.POST)

		if form.is_valid():
			article = form.save(commit=False)
			article.save()
			context['id'] = article.id

	else:
		article = Article.objects.filter(id=id)
		if len(article):
			form = ArticleForm(instance=article[0])
		else:
			form = ArticleForm()

	context['form'] = form
	context.update(csrf(request))

	return render(request, template_name, context)


def show_article(request, id):

	article = get_object_or_404(Article, id=id)

	if not request.user.is_authenticated() and not article.publish:
		raise Http404('Article does not exist')


	template_name = "show_article.html"

	context = {
		'article': article
	}

	return render(request, template_name, context)


def show_list(request):

	if not request.user.is_authenticated():
		articles = Article.objects.filter(publish=True).order_by('-created')
	else:
		articles = Article.objects.all().order_by('-created')

	template_name = "list.html"

	context = {
		'articles': articles
	}

	return render(request, template_name, context)


def reload_page(request):
	latest_news = Article.objects.filter(publish=True).order_by('-created')[0]
	now = datetime.now(timezone.utc)
	print(latest_news.created)
	if (now - latest_news.created) < timedelta(seconds=5):
		return HttpResponse(1)
	else:
		return HttpResponse(0)
