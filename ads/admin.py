from django.contrib import admin

from ads.models import Categories, Location, Author, Announcement

admin.site.register(Categories)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Announcement)
