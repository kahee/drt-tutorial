from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from ..apis.viewsets import SnippetViewSet

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight',
}, renderer_classes=[renderers.StaticHTMLRenderer])

app_name = 'snippets'
urlpatterns = [
    path('', snippet_list, name='snippet-list'),
    path('<int:pk>/', snippet_detail, name='snippet-detail'),
    path('<int:pk>/highlight/', snippet_highlight, name='snippet-highlight')
]

urlpatterns = format_suffix_patterns(urlpatterns)
