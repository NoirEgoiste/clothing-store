from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("delete-account", views.delete_account, name="delete-account"),
    path(
        "profile-management",
        views.profile_management,
        name="profile-management",
    ),
    # Password management.
    path(
        "reset-password",
        auth_views.PasswordResetView.as_view(
            template_name="account/password/password-reset.html",
        ),
        name="reset_password",
    ),
    path(
        "reset-password-sent",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password/reset-password-sent.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password/password-reset-form.html",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset-password-complete",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password/password-reset-complete.html",
        ),
        name="password_reset_complete",
    ),
    # Email verification.
    path(
        "email-verification/<str:uidb64>/<str:token>/",
        views.email_verification,
        name="email-verification",
    ),
    path(
        "email-verification-sent",
        views.email_verification_sent,
        name="email-verification-sent",
    ),
    path(
        "email-verification-success",
        views.email_verification_success,
        name="email-verification-success",
    ),
    path(
        "email-verification-failed",
        views.email_verification_failed,
        name="email-verification-failed",
    ),
]
