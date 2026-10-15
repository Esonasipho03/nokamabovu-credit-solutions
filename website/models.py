from datetime import timedelta

from django.db import models
from django.utils import timezone


class Vacancy(models.Model):
    """A job post shown on the Careers page. Managed in the Django admin."""

    DEPARTMENTS = [
        ("Debt recovery", "Debt recovery"),
        ("Car insurance", "Car insurance"),
        ("Vehicle tracking", "Vehicle tracking"),
        ("Support", "Support"),
        ("Management", "Management"),
    ]
    JOB_TYPES = [
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Contract", "Contract"),
        ("Internship", "Internship"),
    ]

    title = models.CharField(max_length=150)
    department = models.CharField(max_length=60, choices=DEPARTMENTS)
    location = models.CharField(max_length=100, default="Johannesburg (HQ)")
    job_type = models.CharField("Job type", max_length=30, choices=JOB_TYPES, default="Full-time")
    closing_date = models.DateField(
        null=True, blank=True,
        help_text="Last day to apply. The post hides itself the day after. Leave empty for 'open until filled'.",
    )
    responsibilities = models.TextField(
        help_text="What you'll do. Type one point per line.",
    )
    requirements = models.TextField(
        help_text="What we look for. Type one point per line.",
    )
    is_published = models.BooleanField(
        "Published", default=True,
        help_text="Untick to hide this post from the Careers page without deleting it.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["closing_date", "-created_at"]
        verbose_name_plural = "vacancies"

    def __str__(self):
        return self.title

    @property
    def is_open(self):
        if not self.is_published:
            return False
        return self.closing_date is None or self.closing_date >= timezone.localdate()

    @property
    def badge(self):
        today = timezone.localdate()
        if self.closing_date and 0 <= (self.closing_date - today).days <= 7:
            return "Closing soon"
        if self.created_at and self.created_at >= timezone.now() - timedelta(days=14):
            return "New"
        return ""

    @staticmethod
    def _lines(text):
        return [line.strip(" \t-•") for line in text.splitlines() if line.strip(" \t-•")]

    def responsibilities_list(self):
        return self._lines(self.responsibilities)

    def requirements_list(self):
        return self._lines(self.requirements)
