from datetime import date

from django.db import migrations


def add_samples(apps, schema_editor):
    Vacancy = apps.get_model("website", "Vacancy")
    if Vacancy.objects.exists():
        return
    # The three sample roles that were on the Careers page. Edit or delete them in the admin.
    Vacancy.objects.create(
        title="Debt Recovery Agent", department="Debt recovery", location="Johannesburg (HQ)",
        job_type="Full-time", closing_date=date(2026, 11, 16),
        responsibilities="Contact customers by phone to agree affordable repayment arrangements\n"
                         "Record every conversation accurately on our system\n"
                         "Treat every customer with respect and follow our compliance standards",
        requirements="Matric certificate\n"
                     "Clear, confident phone manner in English and one other local language\n"
                     "Comfortable working to daily targets",
    )
    Vacancy.objects.create(
        title="Car Insurance Sales Consultant", department="Car insurance", location="Johannesburg (HQ)",
        job_type="Full-time", closing_date=date(2026, 11, 30),
        responsibilities="Speak to customers about our car insurance solutions and answer their questions\n"
                         "Prepare clear, no-obligation quotes and follow up on enquiries\n"
                         "Meet monthly sales targets",
        requirements="Matric certificate; sales experience is an advantage\n"
                     "Strong listening and communication skills\n"
                     "Willing to complete the required product training",
    )
    Vacancy.objects.create(
        title="Call Centre Team Leader", department="Debt recovery", location="Durban",
        job_type="Full-time", closing_date=date(2026, 12, 13),
        responsibilities="Coach and support a team of agents day to day\n"
                         "Track team performance and report on results\n"
                         "Handle escalated customer queries",
        requirements="Previous call centre or collections experience\n"
                     "Experience leading or mentoring others\n"
                     "Good reporting and organising skills",
    )


class Migration(migrations.Migration):
    dependencies = [("website", "0001_initial")]
    operations = [migrations.RunPython(add_samples, migrations.RunPython.noop)]
