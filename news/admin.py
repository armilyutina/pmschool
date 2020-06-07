from django.contrib import admin
from news.models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class NewsAdmin(SummernoteModelAdmin):
	summer_note_fields = ('text')

#class PostAdmin(admin.ModelAdmin):
#	list_display = ('title', 'date')	
		
admin.site.register(Post,NewsAdmin)

#admin.site.register(Post, PostAdmin, NewsAdmin)

#Если отключить комментирование строк 9-10 и 14, то поле пост в админке 
#будет иметь список постов с названиями, датой и слагом
#просто прикольная фича в Django