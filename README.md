# فروشگاه کتاب آنلاین

پروژه فروشگاه کتاب آنلاین با استفاده از Django توسعه داده شده است. این پروژه امکاناتی مانند ثبت‌نام کاربران، مدیریت پروفایل، مشاهده و مدیریت کتاب‌ها، افزودن و مدیریت نظرات را ارائه می‌دهد.

## 🚀 راه‌اندازی پروژه در محیط محلی

### پیش‌نیازها

- Python 3.10 یا بالاتر
- pipenv
- MySQL (نصب و راه‌اندازی شده)
- ایجاد دیتابیس MySQL با نام دلخواه (مثلاً `bookstore_db`)

### مراحل نصب و راه‌اندازی

1. **کلون کردن پروژه:**

   ```bash
   git clone git@github.com:VahidRajabi-2000-5/Store-Project.git
   cd Store-Project
   ```

2. **نصب وابستگی‌ها و ساخت محیط مجازی با pipenv:**

   ```bash
   pipenv install
   ```

3. **فعال‌سازی محیط مجازی:**

   ```bash
   pipenv shell
   ```

4. **نصب پکیج mysqlclient (ممکن است به نصب libmysqlclient-dev نیاز باشد):**

   ```bash
   pipenv install mysqlclient
   ```

5. **تنظیمات دیتابیس:**

   در فایل `store_project/settings.py`، بخش `DATABASES` را به صورت زیر تنظیم کنید:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'bookstore_db',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. **اجرای مهاجرت‌ها:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **ساخت ادمین (اختیاری):**

   ```bash
   python manage.py createsuperuser
   ```

8. **اجرای سرور:**

   ```bash
   python manage.py runserver
   ```

حالا پروژه در آدرس [http://127.0.0.1:8000/](http://127.0.0.1:8000/) در دسترس است.

## ساختار پروژه

```
store_project/
├── accounts/            # اپلیکیشن مدیریت کاربران
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py        # فرم‌های ثبت‌نام و ویرایش پروفایل
│   ├── models.py      # مدل‌های سفارشی‌شده کاربران
│   ├── tests.py
│   └── views.py      # ویوهای مربوط به مدیریت کاربران
├── books/              # اپلیکیشن مدیریت کتاب‌ها
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py        # فرم‌های مربوط به کتاب‌ها و نظرات
│   ├── models.py      # مدل‌های Book و Comment
│   ├── tests.py
│   └── views.py      # ویوهای مربوط به نمایش و مدیریت کتاب‌ها
├── store_project/      # تنظیمات اصلی پروژه Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py    # تنظیمات کلی پروژه
│   ├── urls.py       # آدرس‌دهی‌های اصلی پروژه
│   └── wsgi.py
├── manage.py
├── Pipfile
├── Pipfile.lock
└── ...
```

## تکنولوژی‌های استفاده‌شده

- Django
- MySQL
- pipenv برای مدیریت محیط مجازی و وابستگی‌ها
- Git & GitHub برای کنترل نسخه

## API Endpoints

برخی از مسیرهای مهم API:

| Endpoint                               | Method | توضیحات                                 |
|----------------------------------------|--------|------------------------------------------|
| `/signup/`                             | GET, POST | صفحه ثبت‌نام و ثبت اطلاعات کاربر جدید |
| `/profile/edit/`                       | GET, POST | صفحه ویرایش پروفایل کاربر               |
| `/books/`                              | GET    | لیست کتاب‌ها                             |
| `/books/<int:pk>/`                      | GET    | جزئیات یک کتاب خاص                       |
| `/books/create/`                       | GET, POST | صفحه افزودن کتاب جدید                   |
| `/books/<int:pk>/update/`              | GET, POST | صفحه ویرایش اطلاعات کتاب               |
| `/books/<int:pk>/delete/`              | GET, POST | صفحه حذف کتاب                            |
| `/books/<int:pk>/profile/`              | GET    | پروفایل کاربر مرتبط با کتاب               |

لطفاً توجه داشته باشید که برای استفاده از برخی از این مسیرها، نیاز به ورود به سیستم (لاگین) دارید.


📌 نکات مهم:

در بخش تنظیمات دیتابیس، نام کاربری و رمز عبور MySQL خود را وارد کنید.

اگر از محیط‌های توسعه مختلف استفاده می‌کنید، مطمئن شوید که تنظیمات دیتابیس و سایر وابستگی‌ها به درستی پیکربندی شده‌اند.​


## توسعه‌دهندگان

- **وحید رجبی**
  - GitHub: [VahidRajabi-2000-5](https://github.com/VahidRajabi-2000-5)

## لایسنس

این پروژه به صورت آموزشی ساخته شده و استفاده از آن آزاد است.
