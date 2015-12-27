from django.db import models

# Create your models here.
from family.models import TimeStampedModel
from django.contrib.auth.models import User


class Account(TimeStampedModel):  # use models.Model if timestamp is not needed (or if it will be stored in fixtures)
    """
    Put a really good comment here to describe the new model.
    A few tips when defining the fields:
      Set db_index=True if you'll be filtering by a particular field (foreign keys have this set by default)
      Set default values for fields if there is ever a situation where that field is not required to be set
      Use blank=True and null=True whenever no specific default value makes sense
    """
    user = models.OneToOneField(User, primary_key=True, related_name='account',
                                help_text="Used to make user specific settings")
    title = models.TextField(help_text='Always include help text')


    #class Meta:
    #    ordering = ['display_order']
    #    verbose_name_plural = 'My classes'  # only override if adding an "s" to the end is the improper plural
    #    unique_together = ('fk1', 'fk2')  # Use if this model is a unique link between two foreign keys

    def __unicode__(self):
        return str('%s - %s' % (self.id, self.title))

    # Define LOTS of methods for your model.  Remember, fat models, thin views, dumb templates.
    # ALL business logic should be in your model, even if it's currently only needed in one view.