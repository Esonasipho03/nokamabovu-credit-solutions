from django.contrib import admin

from .models import Testimonial, Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "location", "job_type", "closing_date", "is_published", "live")
    list_editable = ("is_published",)
    list_filter = ("is_published", "department", "job_type")
    search_fields = ("title", "location")
    date_hierarchy = "closing_date"
    actions = ["publish", "unpublish"]

    @admin.display(boolean=True, description="Showing on site")
    def live(self, obj):
        return obj.is_open

    @admin.action(description="Publish selected vacancies")
    def publish(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description="Hide selected vacancies")
    def unpublish(self, request, queryset):
        queryset.update(is_published=False)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "organisation", "role", "is_approved", "display_order")
    list_editable = ("is_approved", "display_order")
    list_filter = ("is_approved",)
    search_fields = ("name", "organisation", "quote")
