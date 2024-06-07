from django.contrib import admin
from .models import Owner, ProjectCategory, Project, Photo, Message
from django.utils.html import format_html

# التحقق مما إذا كان الموديل مسجلاً قبل محاولة إلغاء تسجيله
if admin.site.is_registered(Owner):
    admin.site.unregister(Owner)

# إنشاء OwnerAdmin لعرض عدد المشاريع الخاصة بكل صاحب مشروع
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone', 'date_of_birth', 'get_project_count')

    def get_project_count(self, obj):
        return Project.objects.filter(owner=obj).count()

    get_project_count.short_description = 'عدد المشاريع'

# إعادة تسجيل الموديل Owner مع إعدادات الإدارة الجديدة
admin.site.register(Owner, OwnerAdmin)



# تسجيل الموديلات الأخرى
admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(Photo)

# إنشاء MessageAdmin لعرض المحادثات
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_conversation']
    list_display_links = ['name']

    def display_conversation(self, obj):
        # احصل على جميع رسائل المستخدم مرتبة بترتيب الزمن
        user_messages = Message.objects.filter(name=obj.name, admin_response__isnull=False).order_by('timestamp')
        
        conversation_html = "<div>"  # بداية القالب
        previous_user = None  # متغير لتتبع اسم المستخدم السابق
        for message in user_messages:
            # فقط إذا كان اسم المستخدم الحالي يختلف عن السابق نقوم بإضافته إلى القالب
            if message.name != previous_user:
                conversation_html += f"<div><strong>Name:</strong> {message.name}</div>"
                previous_user = message.name  # تحديث اسم المستخدم السابق ليكون الحالي
            # إضافة كل رسالة ورد للقالب
            conversation_html += f"<div><strong>User:</strong> {message.body}</div>"
            conversation_html += f"<div><strong>Admin:</strong> {message.admin_response}</div><hr>"
        conversation_html += "</div>"  # نهاية القالب
        
        return format_html(conversation_html)

    display_conversation.short_description = "Conversation"  # تعيين عنوان القالب في الإدارة

admin.site.register(Message, MessageAdmin)
