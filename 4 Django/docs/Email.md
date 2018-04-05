



# Email

Email is simple to set up in Django. You can read more about setting up email in the [official docs](https://docs.djangoproject.com/en/2.0/topics/email/). You may also consider using [anymail](https://github.com/anymail/django-anymail).

Add the following fields to your `settings.py`.

```python
EMAIL_HOST = 'smtp.email-host-provider-domain.com'
EMAIL_HOST_USER = 'yourusername@youremail.com'
EMAIL_HOST_PASSWORD = 'your password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Your Name <you@email.com>'
```

Then in a view you can just use the `send_mail` function.

```python
from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```


## SMTP Servers / Email Services

- [gmail](https://mail.google.com/mail/u/0/#settings/general)
  - [digital ocean guide](https://www.digitalocean.com/community/tutorials/how-to-use-google-s-smtp-server)
- [https://sendgrid.com/](https://sendgrid.com/)
  - [sendgrid official doc](https://sendgrid.com/docs/Integrate/Frameworks/django.html)
  - [sibtc guide](https://simpleisbetterthancomplex.com/tutorial/2016/06/13/how-to-send-email.html)
- [https://www.mailgun.com/](https://www.mailgun.com/)
  - [sibtc guide](https://simpleisbetterthancomplex.com/tutorial/2017/05/27/how-to-configure-mailgun-to-send-emails-in-a-django-app.html)




