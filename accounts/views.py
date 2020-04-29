from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm, UserSearchForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction


class ProfileView(View):
    template_name = 'pages/profile.html'

    @method_decorator(login_required)
    def get(self, request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })

    @method_decorator(login_required, transaction.atomic)
    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        else:
            messages.error(request, 'Please correct the error below.')

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })


class UsersView(View):
    template_name = 'pages/users.html'

    search_form = UserSearchForm

    def get(self, request):
        name = request.GET.get('username', '')
        users = User.objects.all().filter(username__contains=name)
        current_page = Paginator(users, 9)
        page = request.GET.get('page')
        search_form = self.search_form(request.GET)
        try:
            users_list = current_page.page(page)
        except PageNotAnInteger:
            users_list = current_page.page(1)
        except EmptyPage:
            users_list = current_page.page(current_page.num_pages)

        return render(request, self.template_name, {'page': page, 'users': users_list, 'form': search_form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/registration_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            from_email = settings.EMAIL_HOST_USER

            send_mail(mail_subject, message, from_email, [to_email])
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/registration.html', {'form': form})


def activate(request, uid64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('accounts:login')
    else:
        return HttpResponse('Activation link is invalid!')
