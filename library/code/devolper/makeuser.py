import sqlite3

def insert_user(api_worm_gpt_db, pass_input):
    # اتصال بقاعدة البيانات SQLite
    conn = sqlite3.connect('database.db')

    # إنشاء مؤشر (cursor) لتنفيذ أوامر SQL
    cursor = conn.cursor()

    # إضافة بيانات المستخدم إلى الجدول
    cursor.execute("INSERT INTO table_name (api_worm_gpt_db, pass) VALUES (?, ?)", (api_worm_gpt_db, pass_input))

    # حفظ التغييرات وإغلاق الاتصال
    conn.commit()
    conn.close()

    print(f"تمت إضافة المستخدم '{api_worm_gpt_db}' إلى قاعدة البيانات.")

# قم بتعيين بيانات المستخدم الذي ترغب في إضافته
api_worm_gpt_db = 'admin'
pass_input = 'admin_pass'

# قم بإضافة المستخدم إلى قاعدة البيانات
insert_user(api_worm_gpt_db, pass_input)
