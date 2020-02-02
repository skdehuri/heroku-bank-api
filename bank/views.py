from rest_framework import viewsets, filters, pagination, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from bank.models import Branch
from bank.serializers import BranchSerializer


class CustomPagination(pagination.LimitOffsetPagination):
    """
    Custom Paginated Response

    """
    def get_paginated_response(self, data):
        return Response({
            'branches': data
        })


class SearchViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View for Search API

    """
    queryset = Branch.objects.all()
    pagination_class = CustomPagination
    serializer_class = BranchSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['^ifsc', '^bank__name', '^branch', '^address', '^city', '^district', '^state']
    ordering_fields = ['ifsc']
    ordering = ['ifsc']

    @action(detail=False, url_path='autocomplete', methods=['get'], url_name='autocomplete')
    def autocomplete(self, request):
        """
        Function to query branch data based on query for autocomplete api
        :param request: request received from web server
        :return: paginated response
        """
        if 'q' in request.GET and request.GET.get('q'):
            q = request.GET.get('q')
            queryset = Branch.objects.filter(branch__icontains=q).order_by('ifsc')
            context = self.paginate_queryset(queryset)
            serializer = BranchSerializer(context, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            return Response({'branches': []})

