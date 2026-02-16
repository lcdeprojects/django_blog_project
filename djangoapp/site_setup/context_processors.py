from .models import SiteSetup


def extra_context(request):
    return {
        'example': 'Contexto Extra',
    }

def site_setup(request):
    site_setup = SiteSetup.objects.first()
    return {
        'site_setup': site_setup,
    }