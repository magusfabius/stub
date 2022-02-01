"""
AuthCanceled at /complete/github/
Authentication process canceled
Request Method:	GET
Request URL:	http://www.astropython.org/complete/github/?redirect_state=uqSXPaGzOQYW8j1FAkqChk4deTnHGES9&code=60bafaf1aec24fcb3a41&state=uqSXPaGzOQYW8j1FAkqChk4deTnHGES9
Django Version:	1.8.1
Exception Type:	AuthCanceled
Exception Value:	
Authentication process canceled
Exception Location:	/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/social/utils.py in wrapper, line 232
Python Executable:	/usr/local/bin/uwsgi
Python Version:	2.7.6
Python Path:	
['/var/www',
 '.',
 '',
 '/var/www',
 '/home/astropython/.virtualenvs/astropython/lib/python2.7',
 '/home/astropython/.virtualenvs/astropython/lib/python2.7/plat-x86_64-linux-gnu',
 '/home/astropython/.virtualenvs/astropython/lib/python2.7/lib-tk',
 '/home/astropython/.virtualenvs/astropython/lib/python2.7/lib-old',
 '/home/astropython/.virtualenvs/astropython/lib/python2.7/lib-dynload',
 '/usr/lib/python2.7',
 '/usr/lib/python2.7/plat-x86_64-linux-gnu',
 '/usr/lib/python2.7/lib-tk',
 '/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages',
 '/home/astropython/astropython/astropython/']
"""


coordinates = [x, y, z, c]

def search_near_me(coordinates):


    # telegram triangolation
    # google maps- multi devices hack
    # iphone maps
    # open maps -> 
    # earth 2
    #


help_list = [ "@me", ["118", search_near_me]]

def critical_response():
    print("404")

def urgency_of_backup(help_list):


Server time:	Sat, 6 Nov 2021 00:59:15 -0500
Traceback Switch to copy-and-paste view
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/django/core/handlers/base.py in get_response
                                response = wrapped_callback(request, *callback_args, **callback_kwargs) ...
▶ Local vars
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/django/views/decorators/cache.py in _wrapped_view_func
                    response = view_func(request, *args, **kwargs) ...
▶ Local vars
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/django/views/decorators/csrf.py in wrapped_view
                    return view_func(*args, **kwargs) ...
▶ Local vars
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/social/apps/django_app/utils.py in wrapper
                        return func(request, backend, *args, **kwargs) ...
▶ Local vars
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/social/apps/django_app/views.py in complete
                                   redirect_name=REDIRECT_FIELD_NAME, *args, **kwargs) ...
▶ Local vars
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/social/actions.py in do_complete
                    user = backend.complete(user=user, *args, **kwargs) ...
▶ Local vars
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/social/backends/base.py in complete
                    return self.auth_complete(*args, **kwargs) ...
▶ Local vars
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/social/utils.py in wrapper
                        return func(*args, **kwargs) ...
▶ Local vars
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/social/backends/oauth.py in auth_complete
                                        *args, **kwargs) ...
▶ Local vars
/home/astropython/.virtualenvs/astropython/local/lib/python2.7/site-packages/social/utils.py in wrapper
                            raise AuthCanceled(args[0]) ...
▶ Local vars
Request information
GET
Variable	Value
state	
u'uqSXPaGzOQYW8j1FAkqChk4deTnHGES9'
code	
u'60bafaf1aec24fcb3a41'
redirect_state	
u'uqSXPaGzOQYW8j1FAkqChk4deTnHGES9'
POST
No POST data

FILES
No FILES data

COOKIES
Variable	Value
sessionid	
'ggzzh3lvmlgjwp96c8osz6rb9vjg6zyc'
_ga	
'GA1.2.2116016310.1636178282'
_gid	
'GA1.2.1283272050.1636178282'
META
Variable	Value
wsgi.multiprocess	
True
HTTP_COOKIE	
'_ga=GA1.2.2116016310.1636178282; _gid=GA1.2.1283272050.1636178282; sessionid=ggzzh3lvmlgjwp96c8osz6rb9vjg6zyc'
uwsgi.version	
'2.0.17.1'
SCRIPT_NAME	
u''
REQUEST_METHOD	
'GET'
PATH_INFO	
u'/complete/github/'
SERVER_PROTOCOL	
'HTTP/1.1'
QUERY_STRING	
'redirect_state=uqSXPaGzOQYW8j1FAkqChk4deTnHGES9&code=60bafaf1aec24fcb3a41&state=uqSXPaGzOQYW8j1FAkqChk4deTnHGES9'
HTTP_X_REAL_IP	
'37.163.56.213'
CONTENT_LENGTH	
''
HTTP_USER_AGENT	
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63'
HTTP_CONNECTION	
'close'
SERVER_NAME	
'www.astropython.org'
REMOTE_ADDR	
'10.0.0.66'
wsgi.url_scheme	
'http'
SERVER_PORT	
'80'
uwsgi.node	
'green-liveweb7'
DOCUMENT_ROOT	
'/usr/local/openresty/nginx/html'
wsgi.input	
<uwsgi._Input object at 0x7f1803b47e28>
HTTP_HOST	
'www.astropython.org'
wsgi.multithread	
False
HTTP_UPGRADE_INSECURE_REQUESTS	
'1'
REQUEST_URI	
'/complete/github/?redirect_state=uqSXPaGzOQYW8j1FAkqChk4deTnHGES9&code=60bafaf1aec24fcb3a41&state=uqSXPaGzOQYW8j1FAkqChk4deTnHGES9'
HTTP_ACCEPT	
'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
wsgi.version	
(1, 0)
HTTP_X_FORWARDED_FOR	
'37.163.56.213'
wsgi.errors	
<uwsgi_file__bin_user_wsgi_wrapper.ErrorLogFile object at 0x7f1812fc6750>
REMOTE_PORT	
'55466'
HTTP_ACCEPT_LANGUAGE	
'en-GB,en-US;q=0.9,en;q=0.8'
wsgi.run_once	
False
CONTENT_TYPE	
''
wsgi.file_wrapper	
''
CSRF_COOKIE	
u'vXDk4tcccpBvXyoFdyXeeZ2dllt87Mq9'
HTTP_ACCEPT_ENCODING	
'gzip, deflate'
Settings
Using settings module astropython.settings
Setting	Value
COMPRESS_URL	
'/static/'
COMPRESS_OUTPUT_DIR	
u'CACHE'
SECURE_SSL_REDIRECT	
False
COMPRESS_TEMPLATE_FILTER_CONTEXT	
{u'STATIC_URL': '/static/'}
SECURE_BROWSER_XSS_FILTER	
False
COMPRESS_DATA_URI_MAX_SIZE	
1024
CSRF_COOKIE_SECURE	
False
LANGUAGE_CODE	
'en-us'
ROOT_URLCONF	
'astropython.urls'
MANAGERS	
()
COMPRESS_CSS_HASHING_METHOD	
u'mtime'
BASE_DIR	
'.'
SILENCED_SYSTEM_CHECKS	
[]
DEFAULT_CHARSET	
'utf-8'
IGNORABLE_404_URLS	
()
SESSION_SERIALIZER	
'django.contrib.sessions.serializers.JSONSerializer'
STATIC_ROOT	
'static/static_root'
COMPRESS_CLOSURE_COMPILER_ARGUMENTS	
u''
USE_THOUSAND_SEPARATOR	
False
COMPRESS_OFFLINE_MANIFEST	
u'manifest.json'
ALLOWED_HOSTS	
['*']
MESSAGE_STORAGE	
'django.contrib.messages.storage.fallback.FallbackStorage'
SOCIAL_AUTH_FACEBOOK_SCOPE	
['email']
COMPRESS_YUI_JS_ARGUMENTS	
u''
SERVER_EMAIL	
'root@localhost'
SECURE_HSTS_SECONDS	
0
STATICFILES_FINDERS	
('django.contrib.staticfiles.finders.FileSystemFinder',
 'django.contrib.staticfiles.finders.AppDirectoriesFinder')
SESSION_CACHE_ALIAS	
'default'
COMPRESS_CSSTIDY_ARGUMENTS	
u'--template=highest'
SESSION_COOKIE_DOMAIN	
None
SESSION_COOKIE_NAME	
'sessionid'
COMPRESS_YUGLIFY_JS_ARGUMENTS	
u'--terminal'
TIME_INPUT_FORMATS	
('%H:%M:%S', '%H:%M:%S.%f', '%H:%M')
SECURE_REDIRECT_EXEMPT	
[]
DATABASES	
{'default': {'ATOMIC_REQUESTS': False,
             'AUTOCOMMIT': True,
             'CONN_MAX_AGE': 0,
             'ENGINE': 'django.db.backends.mysql',
             'HOST': 'astropython.mysql.pythonanywhere-services.com',
             'NAME': 'astropython$db',
             'OPTIONS': {},
             'PASSWORD': u'********************',
             'PORT': '',
             'TEST': {'CHARSET': None,
                      'COLLATION': None,
                      'MIRROR': None,
                      'NAME': None},
             'TIME_ZONE': 'America/Chicago',
             'USER': 'astropython'}}
EMAIL_SSL_KEYFILE	
u'********************'
FILE_UPLOAD_DIRECTORY_PERMISSIONS	
None
SOCIAL_AUTH_TWITTER_SECRET	
u'********************'
COMPRESS_YUI_BINARY	
u'java -jar yuicompressor.jar'
FILE_UPLOAD_PERMISSIONS	
None
FILE_UPLOAD_HANDLERS	
('django.core.files.uploadhandler.MemoryFileUploadHandler',
 'django.core.files.uploadhandler.TemporaryFileUploadHandler')
TEMPLATE_CONTEXT_PROCESSORS	
('django.contrib.auth.context_processors.auth',
 'django.template.context_processors.debug',
 'django.template.context_processors.i18n',
 'django.template.context_processors.media',
 'django.template.context_processors.static',
 'django.template.context_processors.tz',
 'django.contrib.messages.context_processors.messages')
DEFAULT_CONTENT_TYPE	
'text/html'
COMPRESS_CSS_COMPRESSOR	
u'compressor.css.CssCompressor'
APPEND_SLASH	
True
FIRST_DAY_OF_WEEK	
0
DATABASE_ROUTERS	
[]
DEFAULT_TABLESPACE	
''
SOCIAL_AUTH_FACEBOOK_KEY	
u'********************'
YEAR_MONTH_FORMAT	
'F Y'
COMPRESS_OFFLINE_TIMEOUT	
31536000
STATICFILES_STORAGE	
'django.contrib.staticfiles.storage.StaticFilesStorage'
CACHES	
{'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
COMPRESS_CLEAN_CSS_ARGUMENTS	
u''
SESSION_COOKIE_PATH	
'/'
COMPRESS_PARSER	
u'compressor.parser.AutoSelectParser'
COMPRESS_CACHE_BACKEND	
u'default'
SECURE_CONTENT_TYPE_NOSNIFF	
False
MIDDLEWARE_CLASSES	
('django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.locale.LocaleMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
 'debug_toolbar.middleware.DebugToolbarMiddleware',
 'secretballot.middleware.SecretBallotIpMiddleware',
 'watson.middleware.SearchContextMiddleware',
 'social.apps.django_app.middleware.SocialAuthExceptionMiddleware')
USE_I18N	
True
THOUSAND_SEPARATOR	
','
SECRET_KEY	
u'********************'
LANGUAGE_COOKIE_NAME	
'django_language'
DEFAULT_INDEX_TABLESPACE	
''
LOGGING_CONFIG	
'logging.config.dictConfig'
SIGNING_BACKEND	
'django.core.signing.TimestampSigner'
SOCIAL_AUTH_GITHUB_SECRET	
u'********************'
TEMPLATE_LOADERS	
('django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader')
SOCIAL_AUTH_FACEBOOK_SECRET	
u'********************'
WSGI_APPLICATION	
'astropython.wsgi.application'
TEMPLATE_DEBUG	
False
X_FRAME_OPTIONS	
'SAMEORIGIN'
CSRF_COOKIE_NAME	
'csrftoken'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET	
u'********************'
COMPRESS_CLEAN_CSS_BINARY	
u'cleancss'
FORCE_SCRIPT_NAME	
None
USE_X_FORWARDED_HOST	
False
EMAIL_TIMEOUT	
None
SECURE_SSL_HOST	
None
COMPRESS_CSSTIDY_BINARY	
u'csstidy'
SESSION_COOKIE_SECURE	
False
COMPRESS_DEBUG_TOGGLE	
None
COMPRESS_VERBOSE	
False
CSRF_COOKIE_DOMAIN	
None
FILE_CHARSET	
'utf-8'
DEBUG	
True
SOCIAL_AUTH_LOGIN_URL	
'/'
LANGUAGE_COOKIE_DOMAIN	
None
COMPRESS_JS_FILTERS	
[u'compressor.filters.jsmin.JSMinFilter']
DEFAULT_FILE_STORAGE	
'django.core.files.storage.FileSystemStorage'
INSTALLED_APPS	
('grappelli',
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'debug_toolbar',
 'taggit',
 'secretballot',
 'crispy_forms',
 'compressor',
 'watson',
 'django.contrib.sites',
 'moderation',
 'main',
 'django_cleanup',
 'colorfield',
 'social.apps.django_app.default')
LANGUAGES_BIDI	
('he', 'ar', 'fa', 'ur')
USE_L10N	
True
COMPRESS_YUI_CSS_ARGUMENTS	
u''
SECURE_HSTS_INCLUDE_SUBDOMAINS	
False
STATICFILES_DIRS	
('static/static_files',)
PREPEND_WWW	
False
SECURE_PROXY_SSL_HEADER	
None
PASSWORD_RESET_TIMEOUT_DAYS	
u'********************'
LANGUAGE_COOKIE_AGE	
None
SESSION_COOKIE_HTTPONLY	
True
DEBUG_PROPAGATE_EXCEPTIONS	
False
INTERNAL_IPS	
()
MONTH_DAY_FORMAT	
'F j'
LOGIN_URL	
'/accounts/login/'
SESSION_EXPIRE_AT_BROWSER_CLOSE	
False
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY	
u'********************'
STATE_CHOICES	
(('raw', 'raw'), ('submitted', 'submitted'))
TIME_FORMAT	
'P'
COMPRESS_STORAGE	
u'compressor.storage.CompressorFileStorage'
AUTH_USER_MODEL	
'auth.User'
DATE_INPUT_FORMATS	
('%Y-%m-%d',
 '%m/%d/%Y',
 '%m/%d/%y',
 '%b %d %Y',
 '%b %d, %Y',
 '%d %b %Y',
 '%d %b, %Y',
 '%B %d %Y',
 '%B %d, %Y',
 '%d %B %Y',
 '%d %B, %Y')
COMPRESS_CSS_FILTERS	
[u'compressor.filters.css_default.CssAbsoluteFilter']
AUTHENTICATION_BACKENDS	
('django.contrib.auth.backends.ModelBackend',
 'social.backends.google.GoogleOAuth2',
 'social.backends.github.GithubOAuth2',
 'social.backends.yahoo.YahooOAuth',
 'social.backends.facebook.FacebookOAuth2',
 'social.backends.twitter.TwitterOAuth')
EMAIL_HOST_PASSWORD	
u'********************'
COMPRESS_REBUILD_TIMEOUT	
2592000
GRAPPELLI_ADMIN_TITLE	
'AstroPython Admin'
SESSION_FILE_PATH	
None
CACHE_MIDDLEWARE_ALIAS	
'default'
SESSION_SAVE_EVERY_REQUEST	
False
NUMBER_GROUPING	
0
SESSION_ENGINE	
'django.contrib.sessions.backends.cache'
COMPRESS_YUGLIFY_BINARY	
u'yuglify'
CSRF_FAILURE_VIEW	
'django.views.csrf.csrf_failure'
CSRF_COOKIE_PATH	
'/'
COMPRESS_CACHE_KEY_FUNCTION	
u'********************'
LOGIN_REDIRECT_URL	
'/accounts/profile/'
SOCIAL_AUTH_PIPELINE	
('social.pipeline.social_auth.social_details',
 'social.pipeline.social_auth.social_uid',
 'social.pipeline.social_auth.auth_allowed',
 'social.pipeline.social_auth.social_user',
 'social.pipeline.social_auth.associate_by_email',
 'social.pipeline.user.get_username',
 'social.pipeline.user.create_user',
 'social.pipeline.social_auth.associate_user',
 'social.pipeline.social_auth.load_extra_data',
 'social.pipeline.user.user_details')
INPUT_CHOICES	
(('WYSIWYG', 'WYSIWYG'), ('Markdown', 'Markdown'))
DECIMAL_SEPARATOR	
'.'
COMPRESS_PRECOMPILERS	
()
COMPRESS_MTIME_DELAY	
10
SITE_ID	
1
LOCALE_PATHS	
()
TEMPLATE_STRING_IF_INVALID	
''
LOGOUT_URL	
'/accounts/logout/'
SOCIAL_AUTH_LOGIN_ERROR_URL	
'/'
EMAIL_USE_TLS	
True
TEMPLATE_DIRS	
()
FIXTURE_DIRS	
()
EMAIL_HOST	
'smtp.sendgrid.net'
DATE_FORMAT	
'N j, Y'
MEDIA_ROOT	
'static/media'
DEFAULT_EXCEPTION_REPORTER_FILTER	
'django.views.debug.SafeExceptionReporterFilter'
ADMINS	
()
FORMAT_MODULE_PATH	
None
DEFAULT_FROM_EMAIL	
'webmaster@localhost'
COMPRESS_ROOT	
'/home/astropython/astropython/astropython/static/static_root'
MEDIA_URL	
'/media/'
DATETIME_FORMAT	
'N j, Y, P'
EMAIL_SUBJECT_PREFIX	
'[Django] '
SOCIAL_AUTH_LOGIN_REDIRECT_URL	
'/'
COMPRESS_JS_COMPRESSOR	
u'compressor.js.JsCompressor'
DISALLOWED_USER_AGENTS	
()
ALLOWED_INCLUDE_ROOTS	
()
COMPRESS_MINT_DELAY	
30
LOGGING	
{}
SHORT_DATE_FORMAT	
'm/d/Y'
SOCIAL_AUTH_TWITTER_KEY	
u'********************'
TEMPLATES	
[{'BACKEND': 'django.template.backends.django.DjangoTemplates',
  'DIRS': ['./templates'],
  'OPTIONS': {'context_processors': ['django.contrib.auth.context_processors.auth',
                                     'django.template.context_processors.debug',
                                     'django.template.context_processors.i18n',
                                     'django.template.context_processors.media',
                                     'django.template.context_processors.static',
                                     'django.template.context_processors.tz',
                                     'django.template.context_processors.request',
                                     'django.contrib.messages.context_processors.messages',
                                     'social.apps.django_app.context_processors.backends',
                                     'social.apps.django_app.context_processors.login_redirect'],
              'loaders': (('django.template.loaders.cached.Loader',
                           ('django.template.loaders.filesystem.Loader',
                            'django.template.loaders.app_directories.Loader')),)}}]
TEST_RUNNER	
'django.test.runner.DiscoverRunner'
COMPRESS_ENABLED	
False
CACHE_MIDDLEWARE_KEY_PREFIX	
u'********************'
COMPRESS_OFFLINE	
False
TIME_ZONE	
'America/Chicago'
SOCIAL_AUTH_GITHUB_KEY	
u'********************'
COMPRESS_OFFLINE_CONTEXT	
{u'STATIC_URL': '/static/'}
COMPRESS_YUGLIFY_CSS_ARGUMENTS	
u'--terminal'
EMAIL_BACKEND	
'django.core.mail.backends.smtp.EmailBackend'
COMPRESS_JINJA2_GET_ENVIRONMENT	
<function JINJA2_GET_ENVIRONMENT at 0x7f18123cdcf8>
EMAIL_USE_SSL	
False
DATETIME_INPUT_FORMATS	
('%Y-%m-%d %H:%M:%S',
 '%Y-%m-%d %H:%M:%S.%f',
 '%Y-%m-%d %H:%M',
 '%Y-%m-%d',
 '%m/%d/%Y %H:%M:%S',
 '%m/%d/%Y %H:%M:%S.%f',
 '%m/%d/%Y %H:%M',
 '%m/%d/%Y',
 '%m/%d/%y %H:%M:%S',
 '%m/%d/%y %H:%M:%S.%f',
 '%m/%d/%y %H:%M',
 '%m/%d/%y')
MIGRATION_MODULES	
{}
SESSION_COOKIE_AGE	
1209600
SETTINGS_MODULE	
'astropython.settings'
USE_ETAGS	
False
LANGUAGES	
(('af', 'Afrikaans'),
 ('ar', 'Arabic'),
 ('ast', 'Asturian'),
 ('az', 'Azerbaijani'),
 ('bg', 'Bulgarian'),
 ('be', 'Belarusian'),
 ('bn', 'Bengali'),
 ('br', 'Breton'),
 ('bs', 'Bosnian'),
 ('ca', 'Catalan'),
 ('cs', 'Czech'),
 ('cy', 'Welsh'),
 ('da', 'Danish'),
 ('de', 'German'),
 ('el', 'Greek'),
 ('en', 'English'),
 ('en-au', 'Australian English'),
 ('en-gb', 'British English'),
 ('eo', 'Esperanto'),
 ('es', 'Spanish'),
 ('es-ar', 'Argentinian Spanish'),
 ('es-mx', 'Mexican Spanish'),
 ('es-ni', 'Nicaraguan Spanish'),
 ('es-ve', 'Venezuelan Spanish'),
 ('et', 'Estonian'),
 ('eu', 'Basque'),
 ('fa', 'Persian'),
 ('fi', 'Finnish'),
 ('fr', 'French'),
 ('fy', 'Frisian'),
 ('ga', 'Irish'),
 ('gl', 'Galician'),
 ('he', 'Hebrew'),
 ('hi', 'Hindi'),
 ('hr', 'Croatian'),
 ('hu', 'Hungarian'),
 ('ia', 'Interlingua'),
 ('id', 'Indonesian'),
 ('io', 'Ido'),
 ('is', 'Icelandic'),
 ('it', 'Italian'),
 ('ja', 'Japanese'),
 ('ka', 'Georgian'),
 ('kk', 'Kazakh'),
 ('km', 'Khmer'),
 ('kn', 'Kannada'),
 ('ko', 'Korean'),
 ('lb', 'Luxembourgish'),
 ('lt', 'Lithuanian'),
 ('lv', 'Latvian'),
 ('mk', 'Macedonian'),
 ('ml', 'Malayalam'),
 ('mn', 'Mongolian'),
 ('mr', 'Marathi'),
 ('my', 'Burmese'),
 ('nb', 'Norwegian Bokmal'),
 ('ne', 'Nepali'),
 ('nl', 'Dutch'),
 ('nn', 'Norwegian Nynorsk'),
 ('os', 'Ossetic'),
 ('pa', 'Punjabi'),
 ('pl', 'Polish'),
 ('pt', 'Portuguese'),
 ('pt-br', 'Brazilian Portuguese'),
 ('ro', 'Romanian'),
 ('ru', 'Russian'),
 ('sk', 'Slovak'),
 ('sl', 'Slovenian'),
 ('sq', 'Albanian'),
 ('sr', 'Serbian'),
 ('sr-latn', 'Serbian Latin'),
 ('sv', 'Swedish'),
 ('sw', 'Swahili'),
 ('ta', 'Tamil'),
 ('te', 'Telugu'),
 ('th', 'Thai'),
 ('tr', 'Turkish'),
 ('tt', 'Tatar'),
 ('udm', 'Udmurt'),
 ('uk', 'Ukrainian'),
 ('ur', 'Urdu'),
 ('vi', 'Vietnamese'),
 ('zh-cn', 'Simplified Chinese'),
 ('zh-hans', 'Simplified Chinese'),
 ('zh-hant', 'Traditional Chinese'),
 ('zh-tw', 'Traditional Chinese'))
COMPRESS_CLOSURE_COMPILER_BINARY	
u'java -jar compiler.jar'
FILE_UPLOAD_TEMP_DIR	
None
CSRF_COOKIE_AGE	
31449600
STATIC_URL	
'/static/'
EMAIL_PORT	
587
USE_TZ	
False
SHORT_DATETIME_FORMAT	
'm/d/Y P'
TEST_NON_SERIALIZED_APPS	
[]
PASSWORD_HASHERS	
u'********************'
FILE_UPLOAD_MAX_MEMORY_SIZE	
2621440
ABSOLUTE_URL_OVERRIDES	
{}
LANGUAGE_COOKIE_PATH	
'/'
CACHE_MIDDLEWARE_SECONDS	
600
EMAIL_SSL_CERTFILE	
None
CSRF_COOKIE_HTTPONLY	
False
CRISPY_TEMPLATE_PACK	
'bootstrap3'
EMAIL_HOST_USER	
'astropython-email'
You're seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard page generated by the handler for this status code.