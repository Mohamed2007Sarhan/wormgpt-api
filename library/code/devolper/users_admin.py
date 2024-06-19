import sqlite3

def add_user(username, password):
    # اتصال بقاعدة البيانات SQLite
    conn = sqlite3.connect('../database.db')

    # إنشاء مؤشر (cursor) لتنفيذ أوامر SQL
    cursor = conn.cursor()

    # إضافة بيانات المستخدم إلى الجدول
    cursor.execute("INSERT INTO table_name (api_worm_gpt_db, pass) VALUES (?, ?)", (username, password))

    # حفظ التغييرات وإغلاق الاتصال
    conn.commit()
    conn.close()

    print(f"تمت إضافة المستخدم '{username}' إلى قاعدة البيانات.")

# قم بتعيين بيانات المستخدم الذي ترغب في إضافته

