from django.shortcuts import render
from rest_framework.views import APIView
from product.models import *
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class ProductList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None,id=None):
        if id is None:
          new = Product.objects.filter().order_by('-created_at')
          new_serializer = ProductSerializer(new, many=True)
          popular = Product.objects.filter().order_by('-sold')
          popular_serializer = ProductSerializer(popular, many=True)
          return Response({
              'new': new_serializer.data,
              'popular': popular_serializer.data
          }, status=status.HTTP_200_OK)
        else:
          product = Product.objects.filter(id=id)
          serializer = ProductSerializer(product,many=True)
          return Response({
              'data': serializer.data
          }, status=status.HTTP_200_OK)



class PopularproductList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        products = Product.objects.filter().order_by('-sold')
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data}, status=status.HTTP_200_OK)


class OrderView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
      
        all_orders =  Order.objects.all()
        all_serializer = OrderSerializer(all_orders, many=True)
        orders_delivered = Order.objects.filter(
            ~Q(status=0), user=request.user.id)
        delivered_serializer = OrderSerializer(orders_delivered, many=True)
        orders_active = Order.objects.filter(status=0, user=request.user.id)
        active_serializer = OrderSerializer(orders_active, many=True)
        return Response(
            {
                'all': all_serializer.data,
                'active': active_serializer.data,
                'delivered': delivered_serializer.data

            }, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print(request.data)
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Order Placed Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
