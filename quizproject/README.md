# quizproject

Jeg tror det meste av koden er lett forståelig, så utelater det mest trivielle her, men det er noen ting som kanskje ikke er så lett å legge merke til med en gang.
All HTML ligger i templates. Templates/reistration er den første siden man ser med login-formet. Templates/main inneholder filen base.html som er meny/konkuranseregler og footer. Home.html er selve quizen. Logout er i grunn bare en side som redirecter til root, altså til login.html. Result.html er siden du kommer til når du har levert, og den du kommer til hvis du logger inn igjen etter du har levert. Denne viser hvor mange rette svar du har. 

### Gjøre quizen aktiv
Det finnes en fil som ligger i static/js/orakel.js I filen er det kommentarer for hvordan man skal sette aktiviseringstidspunkt. Det er viktig at det er på riktig form og at det er på engelsk. 


### UserProfile
Det er laget en egen klasse, `UserProfile`, som har innholder koblingen `user = models.OneToOneField(User)`. I tillegg er det en hjelpefunksjon, `create_user_profile()` og et funksjonskall `post_save.connect()` som kobler den innebygde `User`-klassen med `UserProfile`-klassen, og sørger for at sistnevne opprettes når en bruker opprettes. For å aksessere data i denne klassen kan man i kalle `userprofile = user.get_profile()`, evt. `request.user.get_profile()`. Husk linjen `from django.contrib.auth.models import User` om du skal bruke dette.

### Login/logout
Foran et par av funksjonene i *views.py* står det `@login_required`. Dette betyr at man må være logget inn for å kjøre denne funksjonen. Om man ikke er det, så blir man av default omdirigert(redirect) til templaten *registration/login.html*. Du kan flytte på denne templaten og overkjøre default, og du må gjerne gjøre det. Les mer om [*login_required*][1].

### LDAP
Innlogging skjer med LDAP. Alt går egentlig automatisk. Den eneste koden som skal til finnes i *settings.py* og er:

```python
### i toppen ###

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

...
### i bunnen ###

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldaps://at.ntnu.no"

AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=people,dc=ntnu,dc=no", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
```

### Templates
Når du skal liste spørsmålene og alternativene i en template, er det veldig viktig at du beholder `name` og `value` i linja `<input type="radio" name="{{ question.id }}" value="{{ choice.id }}" />`. Hvis ikke vil ikke spørsmålsvalideringen fungere.

### Requirements
Du trenger **South** for å kjøre prosjektet slik som det ligger nå. Om du velger å ikke bruke **South** må du kommentere den linjen ut under `INSTALLED_APPS` i *settings.py*. Om du velger å bruke det kan du lese mer om [South][2].

### Andre ting
Det er bare å flytte om på ting i *views.py*. F.eks er det kanskje ikke naturlig at brukeren ikke får beskjed om at han/hun allerede har tatt quizen før etter at h?n har besvart for andre gang. Jeg har heller ikke laget noe resultatliste eller noe, men resultatet til hver enkelt bruker kan enkelt hentes ut ved `userprofile.num_correct_answers()`, evt. `user.get_profile().num_correct_answers()`. Sistnevte er kanskje nyttig i forbindelse med `users = User.objects.all()` for så å gå gjennom lista ved å kjøre `for user in users:`.


[1]: https://docs.djangoproject.com/en/1.2/topics/auth/#the-login-required-decorator
[2]: http://south.readthedocs.org/en/latest/tutorial/part1.html
