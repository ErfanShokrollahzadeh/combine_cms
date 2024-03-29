# from datetime import datetime
# from django.shortcuts import render
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# from rest_framework.parsers import FormParser, MultiPartParser
# from rest_framework import generics
# from mezzanine import blog
# from mezzanine.generic.models import ThreadedComment
# from django.db.models import Q

# from api.serializers import UserSerializer, GroupSerializer, ProjectSerializer, BlogPostSerializer
# from api.models import Project


# @permission_classes((IsAdminUser, ))
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# @permission_classes((IsAdminUser, ))
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# @permission_classes((IsAuthenticatedOrReadOnly, ))
# class ProjectViewSet(viewsets.ModelViewSet):
#     """
#     Projects API endpoint.
#     """
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     parser_classes = (MultiPartParser, FormParser, )


# @permission_classes((IsAuthenticatedOrReadOnly, ))
# class BlogPostViewSet(viewsets.ModelViewSet):
#     """
#     BlogPosts API endpoint.
#     """
#     # Filter to show only blogposts with 'published' status (in mezzanine published=2, draft=1), also filters out expired posts with Q objects
#     queryset = blog.objects.filter(status=2).filter(
#         Q(expiry_date__gte=datetime.now()) | Q(expiry_date=None))
#     serializer_class = BlogPostSerializer
#     parser_classes = (MultiPartParser, FormParser, )
