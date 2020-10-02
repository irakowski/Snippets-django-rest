from django.db import models
from pygments.lexers import get_all_lexers
##Return an iterable over all registered lexers, yielding tuples in the format:
#(longname, tuple of aliases, tuple of filename patterns, tuple of mimetypes)
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
#getting alias and name as a tuple
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, max_length=100, default='friendly')

    class Meta:
        ordering = ['created']