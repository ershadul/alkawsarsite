# -*- coding: utf-8 -*-

# issue model

from django.db import models
from alkawsarsite.languages import *
from alkawsarsite.sections.models import Section
from alkawsarsite import util

class Issue(models.Model):
    twelve_months = ( ('01' , 'January'),
               ('02', 'Febuary'),
               ('03', 'March'),
               ('04', 'April'),
               ('05', 'May'),
               ('06', 'June'),
               ('07', 'July'),
               ('08', 'August'),
               ('09', 'September'),
               ('10', 'October'),
               ('11', 'November'),
               ('12', 'December')
              )
    some_years = (
        ('2017', '2017'),
        ('2016', '2016'),
        ('2015', '2015'),
        ('2014', '2014'),
        ('2013', '2013'),
        ('2012', '2012'),
        ('2011', '2011'),
        ('2010', '2010'),
        ('2009', '2009'),
        ('2008', '2008'),
        ('2007', '2007'),
        ('2006', '2006'),
        ('2005', '2005'),
        ('2004', '2004'),
    )
    language = models.CharField(max_length=15, choices=languages, default=default_language)
    title = models.CharField(max_length=128)
    title_alias = models.CharField(max_length=128, null=True, blank=True)
    slug_title = models.SlugField(max_length=128)

    year = models.CharField(max_length=5, choices=some_years)
    month = models.CharField(max_length=2, choices=twelve_months)
    issue_year = models.CharField(max_length=10, blank=True, default='0')
    issue_number = models.CharField(max_length=10, blank=True, default='0')

    is_default = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    url = models.CharField(max_length=256, blank=True, default='')
    guid = models.CharField(max_length=40, blank=True, unique=True, db_index=True, default=util.get_uuid)

    image = models.CharField(max_length=50, blank=True, null=True)

    sections = models.ManyToManyField(Section, blank=True)


    class Meta:
        ordering = ['language', '-year' ,'-month']

    def save(self, force_insert=False, force_update=False):
        if Issue.objects.filter(slug_title=self.slug_title, language=self.language).exclude(pk=self.id).count() != 0:
                raise Exception('Duplicate slug title !!!')
        if self.is_default:
            from django.db import connection, transaction
            cursor = connection.cursor()
            # Data modifying operation - commit required
            cursor.execute("UPDATE issues_issue SET is_default = 0 WHERE is_default = 1 and language = %s", [self.language])
        super(Issue, self).save(force_insert=force_insert, force_update=force_update)

    def get_absolute_url(self):
        return '/issue/' + self.year + '/' + self.month +'/' + self.slug_title

    def __unicode__(self):
            return self.title

