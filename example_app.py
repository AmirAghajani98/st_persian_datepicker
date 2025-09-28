import streamlit as st
from st_persian_datepicker import date_picker
import datetime as dt

st.set_page_config(page_title="نمونه تقویم جلالی", layout="centered")
st.title("📅 استریم‌لیت - تقویم جلالی")

st.caption("نمونه ساده استفاده از پکیج st-persian-datepicker")

min_ms = int(dt.datetime(2024, 1, 1).timestamp() * 1000)
max_ms = int(dt.datetime(2026, 12, 31).timestamp() * 1000)

val = date_picker(
    label="تاریخ رویداد",
    default="1403/07/06",
    min_date=min_ms,
    max_date=max_ms,
    time_picker=False,
    key="event_date",
)

st.write("نتیجه:", val)