import sqlite3

def create_database():
    # اتصال بقاعدة البيانات SQLite (ستتم إنشاء الملف إذا لم يكن موجودًا)
    conn = sqlite3.connect('database.db')

    # إنشاء مؤشر (cursor) لتنفيذ أوامر SQL
    cursor = conn.cursor()

    # إنشاء جدول لتخزين المستخدمين
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            api_worm_gpt_db TEXT NOT NULL,
            pass TEXT NOT NULL
        )
    ''')

    # حفظ التغييرات وإغلاق الاتصال
    conn.commit()
    conn.close()

    print("تم بناء قاعدة البيانات وإنشاء الجدول بنجاح.")

# تشغيل الدالة لإنشاء قاعدة البيانات والجدول
create_database()
