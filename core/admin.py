from django.contrib import admin
from .models import Course, Lesson, Hotel

admin.site.site_header = "Custom Admin Project"
admin.site.site_title = "Custom Admin"

class LessonInline(admin.StackedInline):
    model = Lesson
    max_num = 5
    extra = 1
    # exclude = ('video_url',)
    # can_delete = False
    verbose_name_plural = "Sample Title"
    classes = ('collapse',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'price', 'full_title', 'status')
    list_display_links = ('title', 'publish_date')
    list_editable = ('price', 'status')
    list_filter = ('status', 'publish_date')
    search_fields = ('title',)
    list_per_page = 3
    readonly_fields = ('status', )
    inlines = (LessonInline,)
    # ordering = ('-title',)
    # search_fields = ('title__startswith', 'price__gte')
    # exclude = ('title', 'price')
    # fields = (('title', 'price'), 'publish_date', 'status', 'author')
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'publish_date', 'price')
    #     }), 
    #     ('Extra Info', {
    #         'classes': ('collapse', 'wide'),
    #         'fields': ('author', 'status'),
    #         'description': "This is a new group"
    #     }))
    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('title',)
        else:
            return ('-price',)
   
    @admin.display(description="New Name")
    def full_title(self, obj):
        return f"{obj.title}-{obj.price}"
    # full_title.short_description = "CompleteName"
    
# admin.site.register(Lesson)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('course__status',)
    search_fields = ('course__price__gte',)
    # autocomplete_fields = ('course',)
    raw_id_fields = ('course',)
admin.site.register(Course, CourseAdmin)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    readonly_fields = ("image_privew",)
    list_display = ("name", "admin_image_privew")

