from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


urlpatterns = [
    # URLs used for function-based views
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    # URLs used for class-based views
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
