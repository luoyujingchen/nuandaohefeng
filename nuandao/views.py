from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import generic

from nuandao.models import Article
from nuandao.util import get_summary


class IndexView(generic.ListView):
    template_name = 'nuandao/index.html'
    context_object_name = 'latest_articles_list'

    def get_queryset(self):
        """return the last five published articles."""
        content = Article.objects.order_by('-publish_date')[:5]
        for c in content:
            c.article_data = get_summary(c.article_data, 366)+'......'
        return content


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    return render(request, 'nuandao/detail.html', {'article': article})
