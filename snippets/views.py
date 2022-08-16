from django.contrib.auth import get_user_model
from django.views.generic import ListView
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer

User = get_user_model()


@api_view(["GET"])  # new
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "snippets": reverse(
                "snippet-list", request=request, format=format
            ),
        }
    )


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset autmatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.

    Additionally we also provide an extra 'highlight' action.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'retrieve actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetListView(ListView):
    model = Snippet
    template_name = "snippets/snippets_list.html"

    paginate_by = 5
