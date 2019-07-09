from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .mixin import FormUserNeededMixin, UserOwnerMixin
from .forms import TweetModelForm
from .models import Tweet

# Create your views here.
class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class = TweetModelForm
	template_name = 'create.html'
	success_url = "create"
	login_url = "/admin/login/"

	# def form_valid(self, form):
	# 	if self.request.user.is_authenticated():
	# 		form.instance.user = self.request.user
	# 		return super(TweetCreateView, self).form_valid(form)
	# 	else:
	# 		form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
	# 		return self.form_invalid(form)


class TweetDetailView(DetailView):
	template_name = "detail.html"
	queryset = Tweet.objects.all()

	# def get_object(self):
	# 	print(self.kwargs)
	# 	pk = self.kwargs.get("pk")
	# 	print(pk)
	# 	return Tweet.objects.get(id=pk)
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	template_name = "update.html"
	form_class = TweetModelForm
	success_url = "/tweets/"

class TweetDeleteView(LoginRequiredMixin, DeleteView):
	queryset = Tweet.objects.all()
	template_name = "delete.html"
	success_url = "/tweets/"
	

class TweetListView(ListView):
	template_name = "list.html"
	def get_queryset(self, *args, **kwargs):
		qs = qs.filter(content__icontains=q)
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(content__icontains=query)
		return qs 
	# queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)

		return context

# def tweet_create_view(request, id=1):
# 	form = TweetModelForm(request.POST or None)
# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.user = request.user
# 		instance.save()
# 	context = {
# 		"form":form
# 	}
# 	return render(request, "create.html", context)

# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	context = {
# 		"object_list" : queryset
# 	}
# 	for i in queryset:
# 		print(i.content)
# 	return render(request, "list.html", context)