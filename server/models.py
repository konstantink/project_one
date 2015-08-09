from django.db import models

class Patch (models.Model):
    name = models.CharField(max_length=255)
    platform = models.IntegerField()
    bild_type = models.IntegerField(null=True, blank=True)
    rivera = models.CharField(max_length=255, null=True, blank=True)
    lint = models.CharField(max_length=255, null=True, blank=True)
    patch = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

class TestGrop(models.Model):
    name = models.CharField(max_length=255)
    libraries = models.CharField(max_length=255)
    parent_group = models.CharField(max_length=255)
    group_type = models.IntegerField(null=True, blank=True)
    rivera = models.CharField(max_length=255, null=True, blank=True)
    lint = models.CharField(max_length=255, null=True, blank=True)
    patch = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=255)
    group = models.ManyToManyField(TestGrop)

    def __unicode__(self):
        return self.name

class TestSuiteType (models.Model):
    PRIORITY_CHOICES = (
    ('0','Idle'),
    ('1','Lowest'),
    ('3','Normal'),
    ('4','Highesth'),
    )
    name = models.CharField(max_length=255)
    priority = platform = models.IntegerField(choices=PRIORITY_CHOICES)

    def __unicode__(self):
        return self.name

class TestSuite(models.Model):
    name = models.CharField(max_length=255)
    suite = models.ForeignKey(TestSuiteType)
    test_group = models.ManyToManyField(TestGrop)

    def __unicode__(self):
        return self.name


class Configuration (models.Model):
    patch_id = models.ForeignKey(Patch)
    suite_id = models.ForeignKey(Test)
    setings = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class TestResult(models.Model):
    test_id = models.ForeignKey(Test)
    test_conf_id = models.ForeignKey(Configuration)
    result = models.TextField()
    time = models.DateField()

    def __unicode__(self):
        return self.name


class Patch (models.Model):
    name = models.CharField(max_length=255)
    platform = models.IntegerField()
    bild_type = models.IntegerField(null=True, blank=True)
    rivera = models.CharField(max_length=255, null=True, blank=True)
    lint = models.CharField(max_length=255, null=True, blank=True)
    patch = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

class History (models.Model):
    test_suite = models.ForeignKey(TestSuite)
    group_id = models.ForeignKey(TestGrop)
    test_id = models.ForeignKey(Test)
    action = models.CharField(max_length=255)
    comment = models.TextField()

    def __unicode__(self):
        return self.name