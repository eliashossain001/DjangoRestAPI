# from rest_framework import pagination

# class CustomPagination(pagination.PageNumberPagination):
#     page_size=1
#     page_size_query_param='count'
#     max_page_size=5
#     page_query_param= 'p'

# class CustomPagination(pagination.PageNumberPagination):
#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link() 
#             },
#             'count': self.page.paginator.count,
#             'results': data
#         })