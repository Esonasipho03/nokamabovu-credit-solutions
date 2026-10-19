from django.core.management.base import BaseCommand

from website.models import Testimonial

MARKER = "[SAMPLE]"

SAMPLES = [
    ("Sample Person One", "Finance Manager", "Sample College",
     "Sample text for layout testing only. A real testimonial would go here, in the client's own words, "
     "describing what working with Nokamabovu was like."),
    ("Sample Person Two", "School Principal", "Sample Academy",
     "Another sample used only to test how a longer testimonial wraps across several lines on desktop and "
     "on a phone, so you can judge spacing before adding real ones."),
    ("Sample Person Three", "Operations Lead", "Sample Insurance Partner",
     "A third sample so you can try the arrows and dots on the slider."),
]


class Command(BaseCommand):
    help = "Add (or remove with --remove) clearly marked SAMPLE testimonials for layout testing."

    def add_arguments(self, parser):
        parser.add_argument("--remove", action="store_true", help="Delete the sample testimonials.")

    def handle(self, *args, **options):
        if options["remove"]:
            deleted, _ = Testimonial.objects.filter(name__startswith=MARKER).delete()
            self.stdout.write(f"Removed {deleted} sample testimonial(s).")
            return
        if Testimonial.objects.filter(name__startswith=MARKER).exists():
            self.stdout.write("Sample testimonials already exist. Use --remove to delete them first.")
            return
        for i, (name, role, org, quote) in enumerate(SAMPLES):
            Testimonial.objects.create(
                name=f"{MARKER} {name}", role=role, organisation=org, quote=quote,
                is_approved=True, display_order=i,
            )
        self.stdout.write(f"Added {len(SAMPLES)} sample testimonials. Remove them before going live:")
        self.stdout.write("  py -3.12 manage.py test_testimonials --remove")
