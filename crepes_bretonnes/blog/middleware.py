from django.db.models import F
from .models import Page

class CompteurMiddleware(object):

    def process_response(self, request, response):

        try:
            page = Page.objects.get(url=request.path)
            page.nb_visit = F('nb_visit') + 1
            page.save()
        except Page.DoesNotExist:
            page = Page.objects.create(url=request.path)

        # Reload it after request complet, without it nothing change
        page.refresh_from_db()

        response.content += str.encode("Page vue {0} fois".format(page.nb_visit))

        return response
