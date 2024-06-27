from django.db.models import Manager


class VegManger(Manager):

    def get_most_viewed_10(self):
        return self.order_by('-seen')[:10]
    
    def get_most_liked_10(self):
        return self.order_by('-like')[:10]