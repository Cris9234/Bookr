from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn__exact', 'publisher__name')


def initialled_name(obj):
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)


class ReviewAdmin(admin.ModelAdmin):
    exclude = 'date_edited'


admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
