from tkinter import S
from django.http import  HttpResponseRedirect
from tempfile import tempdir
from django.shortcuts import render
from main import models,forms   
from django.views.generic import(
    ListView,
    DetailView,
    FormView
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class Index(ListView):
    model=models.Question
    template_name='main/index.html'


class Question(PermissionRequiredMixin,SingleObjectMixin,FormView):
    model=models.Question
    template_name='main\question.html'
    form_class=forms.AnswerForm
    permission_required= "add_answer"

    def get_context_data(self, **kwargs):
        #data={}
        try:
            data =super().get_context_data(**kwargs)
            data['answer']=models.Answer.objects.get(
                question=self.get_object(),
                user=self.request.user
            )
            return data
        except :
            return data

        

    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.question=self.get_object()
        obj.user=self.request.user
        obj.save()
        return HttpResponseRedirect('/')

    """def form_invalid(self, form):
        return super().form_invalid(form)"""
    def post(self,request,*args,**kwargs):
        self.object=self.get_object()
        return super().post(request,*args,**kwargs)


    def get(self, request,*args,**kwargs):
        self.object=self.get_object()
        context=self.get_context_data(object=self.object)
        return self.render_to_response(context)