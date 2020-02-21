from django.template import Library
from ..models import Article
register = Library()

@register.filter
def dateFormat(data):
    return "%d-%d-%d"%(data.year,data.month,data.day)

@register.filter
def authorFormat(author,info):
    return info+":"+author.upper()

@register.simple_tag
def get_latestarticles(num=3):
    return Article.objects.all().order_by("-create_time")[:num]
