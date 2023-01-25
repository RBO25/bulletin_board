import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, mail_managers
from .models import *
from .filters import BulletinFilter


class BulletinList(ListView):
    model = Bulletin
    ordering = 'header'
    template_name = 'bulletins.html'
    context_object_name = 'bulletins'


    @receiver(post_save, sender=Bulletin)
    def notify_feedback(sender, instance, created, **kwargs):
        subject = f'{instance.author}'

        mail_managers(
            subject=subject,
            message=instance.feedback,
        )


    post_save.connect(notify_feedback, sender=Bulletin)


class BulletinDetail(DetailView):
    model = Bulletin
    queryset = Bulletin.objects.all()
    template_name = 'bulletin.html'
    context_object_name = 'bulletin'


    def get_feedback(self, request, *args, **kwargs):
        bulletin = Bulletin(
            author=request.POST['author'],
            feedback=request.POST['feedback'],
        )
        bulletin.save()

        queryset = super().get_queryset()
        self.filterset = BulletinFilter(self.request.GET, queryset)


        send_mail(
            subject=f'{Bulletin.header}',
            message=Bulletin.feedback,
            from_email=os.getenv('DEF_FR_EM'),
            recipient_list=[Bulletin.author]
        )

        return self.filterset.qs()


class BulletinCreate(LoginRequiredMixin, CreateView):
    model = Bulletin
    fields = '__all__'
    template_name = 'bulletin_edit'


class BulletinUpdate(LoginRequiredMixin, UpdateView):
    model = Bulletin
    fields = '__all__'
    template_name = 'bulletin_edit'


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'