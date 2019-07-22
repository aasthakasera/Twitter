from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .mixin import FormUserNeededMixin, UserOwnerMixin
from .forms import TweetModelForm
from .models import Tweet 

# Create your views here.
class RetweetView(View):
	def get(self, request, pk, *args, **kwargs):
		tweet = get_object_or_404(Tweet, pk=pk)
		if request.user.is_authenticated:
			new_tweet = Tweet.objects.retweet(request.user, tweet)
			return HttpResponseRedirect("/")
		return HttpResponseRedirect(tweet.get_absolute_url())

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class = TweetModelForm
	template_name = 'create.html'
	success_url = "create"
	login_url = "/admin/login/"


class TweetDetailView(DetailView):
	template_name = "detail.html"
	queryset = Tweet.objects.all()

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	template_name = "update.html"
	form_class = TweetModelForm
	success_url = "/tweets/"

class TweetDeleteView(LoginRequiredMixin, DeleteView):
	queryset = Tweet.objects.all()
	template_name = "delete.html"
	success_url = "/tweets/"
	

class TweetListView(LoginRequiredMixin, ListView):
	template_name = "list.html"
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) |
				Q(user__username__icontains=query)|
				Q(title__icontains=query)
				)
		return qs 

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		context['create_form'] = TweetModelForm()
		context['create_url'] = reverse_lazy("tweet:create")
		return context

