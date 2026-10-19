from django.conf import settings


def site_links(request):
    return {"linkedin_url": settings.LINKEDIN_URL}
