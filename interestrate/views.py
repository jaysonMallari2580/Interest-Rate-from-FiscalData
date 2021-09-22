from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Interestrate
from .serializers import *

import logging

@api_view(['GET', 'POST'])
def interestrates_list(request):
    """
    List  interestrates, or create a new interestrate.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        interestrates = Interestrate.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(interestrates, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = InterestrateSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/interestrates/?page=' + str(nextPage), 'prevlink': '/api/interestrates/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = InterestrateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def interestrates_detail(request, pk):
    """
    Retrieve, update or delete a interestrate by id/pk.
    """
    try:
        interestrate = Interestrate.objects.get(pk=pk)
    except Interestrate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InterestrateSerializer(interestrate,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InterestrateSerializer(interestrate, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        interestrate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)