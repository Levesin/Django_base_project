from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):

    return render(request=request,
                  template_name="index.html")


class AboutUsView(TemplateView):

    template_name = "base/basic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "about_us"

        return context
