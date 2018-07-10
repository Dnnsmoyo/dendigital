from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from .serializers import DocumentSerializer, ProfileSerializer
from .models import Document,Profile
from django.utils import timezone
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, DocumentForm
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied
from allauth.account.views import SignupView, LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

# Create your views here.
class SignupView(SignupView):
    template_name = 'account/signup.html'


class LoginView(LoginView):
    template_name = 'account/login.html'


class LogoutView(LogoutView):
    template_name = 'account/logout.html'
"""
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = '/'
"""
class ProfileCreateView(SuccessMessageMixin,CreateView):
    template_name='myapp/profile_form.html'
    form_class = ProfileForm
    success_url = '/'
    #success_message = "%(name)s was created successfully" 

    def get_all(request):
        profiles = Profile.objects.all()
        return render(request,'myapp/profile_form.html',{'profiles':profiles})

class ProfileDetailView(DetailView):
    template_name='myapp/profile_detail.html'
    queryset = Profile.objects.all()
    context_object_name = 'profile_object'

    """
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView,self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    """
    def profile_detail(request, state=None):
        profile = get_object_or_404(Profile, profile=profile)
        current_profile = Profile.objects.filter(user=request.user)
        context = {'profiles': 'current_profile'}
        return render(request, 'myapp/profile_detail.html', context) 

    def profile_detail(request, state=None):
        profile = get_object_or_404(Profile, profile=profile)
        current_profile = Profile.objects.filter(user=request.user)
        context = {'profiles': 'current_profile'}
        return render(request, 'myapp/profile_update_form.html', context) 

class ProfileUpdate(SuccessMessageMixin,UpdateView):
    form_class = ProfileForm
    template_name = 'myapp/profile_update.html'
    queryset = Profile.objects.all()
    success_url = '/'
    #success_message = "%(name)s was updated successfully"
    
    
   
class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        welcome = RedisMessage('Hello everybody')  # create a welcome message to be sent to everybody
        RedisPublisher(facility='foobar', broadcast=True).publish_message(welcome)
        return super(IndexView, self).get(request, *args, **kwargs)

class DocUploadView(SuccessMessageMixin,CreateView):
    template_name = 'myapp/document_form.html'
    form_class = DocumentForm
    success_url = '/'
    success_message = "document was created successfully"

    def docs(request):
        documents = Document.object.filter(user=request.user)
        return render(request,'myapp/document_form.html',{'documents':documents})

class DocDetailView(DetailView):
    template_name='myapp/document_detail.html'
    queryset = Document.objects.all()
    context_object_name = 'document_object'

    """
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView,self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    """
    def document_detail(request, state=None):
        document = get_object_or_404(Document, document=document)
        current_document = Document.objects.filter(user=request.user)
        context = {'documents': 'current_document'}
        return render(request, 'myapp/document_detail.html', context) 
    
class DocListView(ListView):
    model = Document
    template_name = "myapp/document_list.html"
    paginate_by = 10

    def document_detail(request, state=None):
        document = get_object_or_404(Document, document=document)
        current_document = Document.objects.filter(user=request.user)
        context = {'documents': 'current_document'}
        return render(request, 'myapp/document_list.html', context)
    
class Index2(TemplateView):
    template_name = 'index2.html'


class DocumentList(APIView):
    """
    List all Courses, or create a new Course.
    """
    def get(self, request, format=None):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DocumentDetail(APIView):
    """
    Retrieve, update or delete a Course instance.
    """
    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Document = self.get_object(pk)
        serializer = DocumentSerializer(Document)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Document = self.get_object(pk)
        serializer = DocumentSerializer(Document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Document = self.get_object(pk)
        Document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProfileList(APIView):
    """
    List all Courses, or create a new Course.
    """
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    """
    Retrieve, update or delete a Course instance.
    """
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Profile = self.get_object(pk)
        serializer = ProfileSerializer(Profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Profile = self.get_object(pk)
        serializer = ProfileSerializer(Profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Profile = self.get_object(pk)
        Profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

    
