# Virtual Review #

* Authors: Rui Batista and NVDA Addon Team
* Download [stable version][1]

This Addon allows NVDA users to review a Window content in a text box,
similar to window virtualization of JAWS for Windows.  Note, however, that
this is just a convenience for users and does not replace NVDA's excellent
review modes and object navigation support.

## كيفية الاستخدام ##

قم بالضغط على nvda+control+w لفتح نافذة وهمية لاستعراض محتوى النافذة. ثم قم
ببساطة بالحركة داخل المربع النصي الذي يظهر لك كما تتحرك على أي نص
عادي. يمكنك ضغط مفتاح Escape للخروج من النافذة الوهمية.

## Changes for 2.2

* When windows are minimized or if the foreground window has no title, NVDA
  will record this fact when displaying virtual review window.

## Changes for 2.1

* The title of the screen under virtual review will be included.
* It is now possible to review contents of Universal Windows Platform (UWP)
  apps in Windows 10 and most modern apps in Windows 8.x.
* When obtaining screen contents for modern and universal apps, a beep will
  be heard to indicate when the virtual review window is ready.

## مستجدات الإصدار 2.0

* New name: Virtual Review.
* Due to changes in how content is shown, NVDA 2015.2 or later is required.
* Thanks to new features in 2015.2 and later, you can now find text in
  virtualized windows.
* إصلاح الإضافة مع النوافذ الأخرى غير نوافذ الأوامر النصية.
* حذف الأسطر الفارغة عديمة الفائدة التي كانت توجد أسفل النص عند استخدام
  الإضافة بنوافذ الأوامر النصية.
* بعض التعديلات الطفيفة.
* ترجمة الإضافة لمزيد من اللغات

## مستجدات الإصدار 1.2

* دعم استعراض نوافذ الأوامر النصية

## مستجدات الإصدار 1.1

* تحويل virtual revision إلى إضافة برمجية

## مستجدات الإصدار 1.0

* نسخة أولية

[[!tag dev stable]]

[1]: https://github.com/ruifontes/virtualReview/releases/download/2024.03.24/virtualRevision-2024.03.24.nvda-addon
