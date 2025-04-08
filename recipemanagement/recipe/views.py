from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import PageForm
from .models import Page
from datetime import datetime
from zoneinfo import ZoneInfo

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        datetime_now = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(request, "recipe/index.html", {"datetime_now": datetime_now})

class PageCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PageForm()
        return render(request, "recipe/page_form.html", {"form": form})

    def post(self, request):
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("recipe:index")

        return render(request, "recipe/page_form.html", {"form": form})

class PageListView(LoginRequiredMixin, View):
    def get(self, request):
        page_list = Page.objects.all()
        return render(request, "recipe/page_list.html", {"page_list": page_list})

class PageDerailView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "recipe/page_detail.html", {"page": page})

class PageUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(instance=page)
        return render(request, "recipe/page_update.html", {"form": form})

    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("recipe:page_detail", id=id)
        return render(request, "recipe/page_form.html", {"form": form})

class PageDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        return render(request, "recipe/page_confirm_delete.html", {"page": page})
    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        page.delete()
        return redirect("recipe:page_list")

index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail = PageDerailView.as_view()
page_update = PageUpdateView.as_view()
page_delete = PageDeleteView.as_view()