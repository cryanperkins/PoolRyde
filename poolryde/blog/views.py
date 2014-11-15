from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from blog.models import Blog
import json

# Create your views here.

def article(request):
    name = 'Ryan'
    html = "<html><body>Hi %s. Welcome to the blog!</body></html>" % name
    return HttpResponse(html)


def article_template(request):
    name = 'Ryan'
    t = get_template('article.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def article_template_simple(request):
    name = "Ryan"
    return render_to_response('article.html', {'name': name})



#class ArticleTemplate(ListView):

    # model = Blog
    # template_name = 'article_class.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(ArticleTemplate, self).get_context_data(**kwargs)
    #     context['name'] = 'Ryan'
    #     return context


def blog_api(request):

    item_list = Blog.objects.all()

    output_list = []

    for item in item_list:
        output_item = {}
        output_item["id"] = item.id
        output_item["title"] = item.title
        output_list.append(output_item)

        return HttpResponse(
            json.dumps(output_list),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
