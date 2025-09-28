import os
import typing as _t
import streamlit.components.v1 as components

__all__ = ["date_picker"]

_COMPONENT_NAME = "st_persian_datepicker"
_RELEASE = True

if _RELEASE:
    _parent = os.path.dirname(os.path.abspath(__file__))
    _build_dir = os.path.join(_parent, "frontend")
    _component_func = components.declare_component(_COMPONENT_NAME, path=_build_dir)
else:
    _component_func = components.declare_component(_COMPONENT_NAME, url="http://localhost:3001")

def date_picker(
    label: str = "انتخاب تاریخ",
    default: _t.Optional[str] = None,
    min_date: _t.Optional[int] = None,
    max_date: _t.Optional[int] = None,
    format: str = "YYYY/MM/DD",
    time_picker: bool = False,
    rtl: bool = True,
    disabled: bool = False,
    key: _t.Optional[str] = None,
) -> _t.Optional[str]:
    """Persian (Jalali) date picker for Streamlit.

    Parameters
    ----------
    label : str
        متن برچسب نمایش داده‌شده در کنار ورودی تاریخ.
    default : Optional[str]
        مقدار اولیه به‌صورت رشته‌ی جلالی مطابق با `format`، مثلاً ``"1403/07/05"``.
    min_date : Optional[int]
        حداقل تاریخ مجاز به‌صورت *Unix time milliseconds* (اختیاری).
    max_date : Optional[int]
        حداکثر تاریخ مجاز به‌صورت *Unix time milliseconds* (اختیاری).
    format : str
        الگوی نمایش/بازگشت تاریخ در جلالی. پیش‌فرض ``"YYYY/MM/DD"``.
    time_picker : bool
        فعال‌سازی انتخاب زمان (ساعت/دقیقه). ثانیه غیرفعال است.
    rtl : bool
        چیدمان راست‌به‌چپ.
    disabled : bool
        غیرفعال کردن ورودی.
    key : Optional[str]
        کلید یکتای کامپوننت در استریم‌لیت.

    Returns
    -------
    Optional[str]
        تاریخ انتخاب‌شده به‌صورت رشته‌ی جلالی طبق `format`.
        اگر کاربر هنوز انتخاب نکرده باشد، ``None`` برمی‌گردد.
    """
    value = _component_func(
        label=label,
        default=default,
        min_date=min_date,
        max_date=max_date,
        format=format,
        time_picker=time_picker,
        rtl=rtl,
        disabled=disabled,
        key=key,
    )
    return value