from django.db import models


class MadLib(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name


# e.g. noun, verb, adverb, etc
class MadLibWordType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MadLibWord(models.Model):
    madlib = models.ForeignKey(MadLib, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.ForeignKey(MadLibWordType, on_delete=models.PROTECT)

    def pretty_name(self):
        return self.name.title()

    def __str__(self):
        return self.madlib.name + ' - ' + self.name

