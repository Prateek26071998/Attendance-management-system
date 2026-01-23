from pathlib import Path
import os
import dj_database_url

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# SECURITY
# --------------------------------------------------
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-dev-only-change-this"
)

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".onrender.com",
]


# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Your apps
    "accounts",
    "attendance",
]


# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------------------------------------
# URLS & WSGI
# --------------------------------------------------
ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# --------------------------------------------------
# DATABASE
# --------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}


# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True
USE_TZ = True


# --------------------------------------------------
# STATIC FILES (CRITICAL FOR RENDER)
# --------------------------------------------------
STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.User"