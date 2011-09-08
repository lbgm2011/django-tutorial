from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 4

class PollAdmin(admin.ModelAdmin):
	#fields = ['pub_date','question']
	fieldsets = [
		(None,			{'fields': ['question']}),
		('Date information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	list_display = ('question', 'pub_date', 'was_published_today')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'
	inlines = [ChoiceInline]
		
admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
