# st-persian-datepicker

یک کامپوننت ساده **تقویم جلالی (Persian DatePicker)** برای Streamlit.

## نصب (نسخه محلی)

فایل ZIP را از این گفتگو دانلود و سپس نصب کنید:

```bash
pip install st-persian-datepicker-0.1.0.zip
```

یا در حالت توسعه (داخل پوشه‌ی پروژه):

```bash
pip install -e .
```

## استفاده

```python
import streamlit as st
from st_persian_datepicker import date_picker

st.set_page_config(page_title="نمونه تقویم جلالی", layout="centered")

st.header("انتخاب تاریخ (جلالی)")
d = date_picker(
    label="تاریخ تولد",
    default="1403/07/05",
    format="YYYY/MM/DD",
    time_picker=False,
    key="birthdate",
)

st.write("مقدار انتخاب‌شده:", d)
```

### محدودیت‌ها و نکات

- برای `min_date` و `max_date`، عدد _Unix time (ms)_ بدهید (اختیاری). مثال پایتون:
  ```python
  import datetime as dt
  min_ms = int(dt.datetime(2025, 1, 1).timestamp() * 1000)
  max_ms = int(dt.datetime(2026, 1, 1).timestamp() * 1000)
  date_picker(min_date=min_ms, max_date=max_ms)
  ```
- مقدار بازگشتی یک **رشته‌ی جلالی** طبق `format` است. اگر زمان فعال باشد، زمان در فیلد ورودی نمایش داده می‌شود اما خروجی رشته‌ی تاریخ است (می‌توانید در نسخه‌های بعدی خروجی را گسترش دهید).
- برای توسعه فرانت‌اند پیشرفته‌تر، می‌توانید این HTML را با React/TypeScript جایگزین کنید.

## توسعه

- در `st_persian_datepicker/__init__.py` مقدار `_RELEASE` را `False` کنید و `url` را به dev server خود اشاره دهید.
- در نسخه‌ی فعلی از CDN برای وابستگی‌ها (jQuery, persian-date, persian-datepicker) استفاده شده است.

## مجوز

MIT

## توزیع و انتشار (Publishing)

این پروژه آمادهٔ بسته‌بندی و انتشار روی PyPI است. در این بخش یک مسیر ایمن و مرحله‌به‌مرحله برای ساخت و انتشار بسته روی TestPyPI (یا PyPI اصلی) آمده است.

پیش‌نیازها

- Python 3.8+
- یک virtualenv فعال (پیشنهاد می‌شود)
- بسته‌های `build` و `twine` نصب‌شده در venv

ساخت توزیع‌ها

1. فعال کردن virtualenv و نصب ابزارها (fish shell):

```fish
cd /path/to/st_persian_datepicker
python3 -m venv .venv
. .venv/bin/activate.fish
python3 -m pip install --upgrade pip build twine
```

2. ساخت sdist و wheel:

```fish
cd st_persian_datepicker
python -m build
# یا برای خروجی در پوشهٔ مشخص:
# python -m build --sdist --wheel --outdir dist
```

تست روی TestPyPI

1. ایجاد حساب روی https://test.pypi.org/ و دریافت API token (recommended) یا استفاده از نام‌کاربری/رمز.
2. آپلود به TestPyPI (نکته: استفاده از API token امن‌تر است):

```fish
# اگر از API token استفاده می‌کنید:
export TWINE_USERNAME='__token__'
export TWINE_PASSWORD='pypi-AgENd...'
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# یا با نام‌کاربری و رمز:
# python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

بررسی نصب از TestPyPI

```fish
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps st-persian-datepicker
```

انتشار به PyPI

1. دریافت API token از https://pypi.org/ (Projects -> Your account -> API tokens).
2. آپلود به PyPI:

```fish
export TWINE_USERNAME='__token__'
export TWINE_PASSWORD='pypi-AgENd...'
python -m twine upload dist/*
```

خودکارسازی

برای راحتی تست، یک اسکریپت نمونه برای انتشار به TestPyPI در `scripts/publish_to_testpypi.sh` قرار داده شده است. این اسکریپت از متغیرهای محیطی `TWINE_USERNAME` و `TWINE_PASSWORD` استفاده می‌کند و فایل‌های توزیع را در `dist/` می‌سازد و آپلود می‌کند.

احتیاط امنیتی: هیچ توکنی یا رمز عبوری را در کد منبع ذخیره نکنید؛ از متغیرهای محیطی یا سرویس CI (مثل GitHub Actions Secrets) استفاده کنید.
