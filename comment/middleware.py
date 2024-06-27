from django.utils import timezone
from .models import SiteVisit

class SiteVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if user has already visited today
        if not request.path.startswith('/admin'):
            visit,created = SiteVisit.objects.get_or_create(date=timezone.now().date())

            if 'visited_today' in request.session:
                if request.session.get('visited_today') != timezone.now().strftime('%Y-%m-%d'):
                    request.session['visited_today'] = timezone.now().strftime('%Y-%m-%d')
                    visit.unique_visits += 1
            else:
                request.session['visited_today'] = timezone.now().strftime('%Y-%m-%d')
                visit.unique_visits += 1

            visit.total_visits += 1
            visit.save()

        response = self.get_response(request)
        return response
