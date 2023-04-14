from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import User
from .forms import ProfileForm


class UpdateAvatarView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('avatar',)

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return self.request.GET.get('redirect')


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'accounts/profile.html'
    model = User
    form_class = ProfileForm
    success_url = '/accounts/profile/'
    success_message = '保存成功'

    def get_object(self):
        return self.request.user
