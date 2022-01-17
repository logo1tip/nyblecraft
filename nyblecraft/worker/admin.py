from django.contrib import admin
from worker.models import Department, Position, Worker


class WorkerAdmin(admin.ModelAdmin):
    list_display = ["id", "last_name", "first_name", "current_department", "current_position"]
    list_display_links = ("id", "last_name")
    ordering = ("last_name",)


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Worker, WorkerAdmin)
