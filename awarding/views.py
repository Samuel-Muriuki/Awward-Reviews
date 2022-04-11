from django.http  import HttpResponseRedirect,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Profile,Rating
import random
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

