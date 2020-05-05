from django.contrib import admin

from .models import PollQuestions, ShortQuestions


# admin.site.register(PollQuestions)
# admin.site.register(ShortQuestions)
class ShortAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'email', 'create_time', 'is_processed',)
    list_editable = ('is_processed',)


# Register the admin class with the associated model

class PollAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'summ',
                    'amount',
                    'income',
                    'pledge',
                    'property',
                    'city',
                    'email',
                    'registration_city',
                    'name',
                    'phone_number',
                    'create_time',
                    'is_processed',)
    list_editable = ('is_processed',)


admin.site.register(ShortQuestions, ShortAdmin)
admin.site.register(PollQuestions, PollAdmin)

# Register your models here.
