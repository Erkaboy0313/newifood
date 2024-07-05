from django.db.models import Manager


class MealManger(Manager):

    def get_most_viewed_10(self):
        return self.filter(status = 'published',confirmed = True).order_by('-seen')[:10]
    
    def get_most_liked_10(self):
        return self.filter(status = 'published',confirmed = True).order_by('-like')[:10]