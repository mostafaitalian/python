from django.db import models

# Create your models here.
class Movie(models.Model):
    unrated = 0
    rating_G = 1
    rating_PG = 2
    rating_R = 3
    
    RATING_CHOICES = ((unrated, "not-rated"),
                      (rating_G, "suitable for children"),
                      (rating_PG, "suitable with parental guide"), (rating_R, "Adult only")
                )
    
    director = models.ForeignKey(to='Person', on_delete=models.SET_NULL, related_name='directed',null=True, blank=True)
    writer = models.ManyToManyField(to='Person', related_name='writing_credits', blank=True)
    actor = models.ManyToManyField(to='Person', related_name='acting_credits',through='Role', blank=True)
    title = models.CharField(max_length=200)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=unrated)
    website = models.URLField(blank=True)
    runtime = models.PositiveIntegerField()
    
    class Meta:
        ordering = ('-year', 'title')
    def __str__(self):
        return "{}--({})".format(self.title, self.year)

class Role(models.Model):
    person = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(to='Person', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=140)
    
    def __str__(self):
        return '{}  {}  {}'.format(self.movie, self.person, self.name)
    class Meta:
        unique_together= ('person', 'movie', 'name')
class Person(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    porn = models.DateField()
    died = models.DateField(null = True, blank = True)
    
    def __str__(self):
        if self.died:
            return '{} {}  ({}-{})'.format(
                self.first_name, self.last_name, self.porn, self.died)
        else:
            return '{}  {}  ({})'.format(self.first_name, self.last_name, self.porn)
    class Meta:
        ordering = ('last_name', 'first_name')
        