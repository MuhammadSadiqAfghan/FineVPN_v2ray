<p align="center">
  <img src="assets/github-banner.gif" alt="FineVPN_v2ray — Secure, Fast, Global" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FineVPN_v2ray-v1.0.0-6d5dfc?style=for-the-badge&logo=shieldsdotio&logoColor=white" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11">
  <img src="https://img.shields.io/badge/Interface-FA%20%7C%20EN-06b6d4?style=for-the-badge" alt="Persian and English interface">
</p>

# ⚡ FineVPN_v2ray

<p align="center">
  <strong>پنل مدرن مدیریت کانفیگ‌های VLESS</strong><br>
  ساخت کانفیگ، مدیریت اشتراک و کنترل منابع سرور در یک محیط یکپارچه
</p>

<p align="center">
  <a href="https://github.com/MuhammadSadiqAfghan/FineVPN-v2ray">مخزن GitHub</a>
  · <a href="INSTALL.md">راهنمای نصب</a>
  · <a href="https://t.me/sadiq_AFG1">پشتیبانی</a>
</p>

**نسخه:** `1.0.0` · **زبان:** فارسی / English · **انتقال‌ها:** WebSocket / XHTTP

**وب‌سایت:** [finevpnv-2ray.hostless.app](https://finevpnv-2ray.hostless.app) · **ورود:** [/login](https://finevpnv-2ray.hostless.app/login) · **سلامت سرویس:** [/health](https://finevpnv-2ray.hostless.app/health)

> **مالکیت و نام تجاری:** نام، لوگو و بخش‌های اصیل پروژه متعلق به صاحب اثر مربوطه هستند. جعل نسخهٔ رسمی یا استفادهٔ گمراه‌کننده از هویت FineVPN مجاز نیست، مگر در مواردی که قانون یا مجوز مربوط اجازه دهد. اطلاعات تکمیلی در [`COPYRIGHT.md`](COPYRIGHT.md) قرار دارد.

## 🪐 بنر متحرک مخزن

بنر متحرک مخزن از فایل [`assets/github-banner.gif`](assets/github-banner.gif) بارگذاری می‌شود؛ نسخهٔ ثابت نیز در [`assets/github-banner.png`](assets/github-banner.png) قرار دارد. برای نمایش درست و حرکت GIF، `README.md` و پوشهٔ `assets/` را همراه بقیهٔ فایل‌ها مستقیماً در ریشهٔ مخزن GitHub قرار دهید؛ آپلود ZIP به‌تنهایی به‌جای فایل‌های پروژه کافی نیست.

## 🌐 معرفی پروژه

FineVPN_v2ray یک پنل مدیریتی برای ساخت و مدیریت کانفیگ‌های VLESS با انتقال‌های WebSocket و XHTTP است. این پروژه برای ساده‌ترکردن مدیریت گروه‌های اشتراک، کنترل سهمیه و محدودیت‌ها و دسترسی سریع به اطلاعات مدیریتی طراحی شده است.

> مدیریت ساده‌تر؛ کنترل بیشتر؛ تجربه‌ای حرفه‌ای‌تر.

**سازنده:** محمدصادق افغان  
**پشتیبانی:** [@sadiq_AFG1](https://t.me/sadiq_AFG1)

## ✨ امکانات اصلی

### ⚙️ ساخت و مدیریت کانفیگ

- ساخت کانفیگ‌های VLESS با انتقال WebSocket و XHTTP.
- پشتیبانی از حالت‌های `packet-up` و `stream-up`.
- ساخت سریع ۲۴ کانفیگ برای هر گروه با ترکیب ۳ حالت انتقال، ۲ fingerprint و ۴ گزینهٔ ALPN.
- فعال‌سازی و غیرفعال‌سازی کانفیگ‌ها.
- انتخاب و حذف گروهی همراه با تأیید عملیات حساس.

### 👥 مدیریت اشتراک و گروه‌ها

- ایجاد و مدیریت گروه‌های اشتراک.
- ارائهٔ لینک اشتراک و صفحهٔ عمومی.
- تنظیم سهمیه و انقضای ترافیک.
- اعمال محدودیت سرعت و تعداد IP.
- حذف گروه همراه با کانفیگ‌های متعلق به همان گروه، بدون حذف کانفیگ‌های سایر گروه‌ها.

### 📊 آمار و کنترل

- مشاهدهٔ اتصال‌های ثبت‌شده.
- نمایش آمار آپلود و دانلود بر اساس شمارنده‌های ثبت‌شده در سمت سرور.
- به‌روزرسانی خودکار اطلاعات صفحهٔ اشتراک بدون رفرش کامل صفحه، به‌همراه دکمهٔ تازه‌سازی دستی.
- ارسال فرادادهٔ حجم، مصرف و انقضا در هدر اشتراک برای کلاینت‌های سازگار؛ پشتیبانی از نمایش این اطلاعات به برنامهٔ کلاینت وابسته است.
- کپی سریع لینک‌ها و دسترسی به کد QR.
- نمایش سرعت بر اساس اختلاف شمارنده‌های ثبت‌شده بین درخواست‌های متوالی.

### 🎨 تجربهٔ کاربری

- رابط کاربری فارسی و انگلیسی.
- پس‌زمینهٔ فضایی متحرک، افکت‌های شیشه‌ای و کارت‌های واکنش‌گرا.
- بخش مستقل «ظاهر پنل» زیر داشبورد، با تم‌های آبی، بنفش، زمردی و طلایی و رنگ‌های سفارشی.
- تنظیم ظاهر جداگانه در پنل اشتراک؛ تنظیمات ظاهری هر دو بخش در مرورگر ذخیره می‌شوند.
- بخش دانلود برنامه‌های سازگار با لینک‌های رسمی.
- رابط مناسب برای استفاده در رایانه و موبایل.

### 🔐 ابزارهای مدیریتی

- ثبت رخدادهای مدیریتی.
- محدودکردن تلاش‌های ورود.
- پشتیبان‌گیری و بازیابی اطلاعات.
- امکان پیکربندی ذخیره‌سازی پایدار.

> **توجه:** آمار اتصال و ترافیک به داده‌هایی وابسته است که سرور واقعاً ثبت می‌کند. صفر بودن آمار در نبود ترافیک می‌تواند طبیعی باشد.

## 🧩 پیش‌نیازها

- Python 3.11 برای اجرای محلی و تصویر Docker
- فایل‌های پروژه و `requirements.txt`

## 🚀 نصب و اجرای محلی

### ۱. ساخت محیط مجازی

```bash
python -m venv .venv
```

### ۲. فعال‌سازی محیط

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### ۳. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

### ۴. تنظیم اطلاعات مدیریتی

**Linux / macOS**

```bash
export ADMIN_USERNAME='your-admin-name'
export ADMIN_PASSWORD='your-strong-password'
export SECRET_KEY='your-long-random-secret'
```

**Windows PowerShell**

```powershell
$env:ADMIN_USERNAME='your-admin-name'
$env:ADMIN_PASSWORD='your-strong-password'
$env:SECRET_KEY='your-long-random-secret'
```

برای `SECRET_KEY` از یک مقدار تصادفی و طولانی استفاده کنید. رمز و کلید واقعی را در GitHub قرار ندهید.

### ۵. اجرای برنامه

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

صفحهٔ ورود محلی: <http://127.0.0.1:8000/login>

## ☁️ استقرار روی Hostless

این نسخه یک `Dockerfile` و فایل `hostless.yaml` دارد تا Hostless به‌جای مسیر Railpack/Mise از ساخت مبتنی بر Docker و Python 3.11 استفاده کند. این مسیر برای دورزدن خطایی آماده شده که در مرحلهٔ نصب Python رخ می‌داد؛ استقرار واقعی همچنان باید در Hostless آزمایش شود.

1. فایل‌های پروژه، از جمله `Dockerfile` و `hostless.yaml`، را در ریشهٔ مخزن قرار دهید.
2. از مخزن درست استفاده کنید: [FineVPN_v2ray](https://github.com/MuhammadSadiqAfghan/FineVPN-v2ray).
3. مطمئن شوید تنظیمات Hostless از ریشهٔ مخزن استفاده می‌کند و بخش Build System روی Docker تنظیم شده است. فایل `hostless.yaml` این تنظیم را تعریف می‌کند.
4. در **Environment variables** مقادیر محرمانهٔ `ADMIN_USERNAME`، `ADMIN_PASSWORD` و `SECRET_KEY` را تنظیم کنید. آن‌ها را داخل فایل‌های مخزن نگذارید.
5. نسخهٔ جدید را Deploy کنید و لاگ Build را بررسی کنید.
6. پس از شروع برنامه، مسیر `/health` باید پاسخ موفق بدهد و سپس `/login` را آزمایش کنید.

اگر Hostless پیکربندی داخل `hostless.yaml` را خودکار اعمال نکرد، در تنظیمات برنامه Build System را روی **Docker** قرار دهید و مسیر Dockerfile را `./Dockerfile` تنظیم کنید. این فایل‌ها مشکل کد برنامه را اثبات یا تضمین نمی‌کنند؛ اگر Build با Docker هم شکست خورد، خطای جدید را بررسی کنید.

## 🚄 استقرار روی Railway

1. مخزن [FineVPN_v2ray در GitHub](https://github.com/MuhammadSadiqAfghan/FineVPN-v2ray) را به پروژهٔ Railway متصل کنید.
2. در بخش Variables متغیرهای `ADMIN_USERNAME`، `ADMIN_PASSWORD` و `SECRET_KEY` را تنظیم کنید.
3. یک Volume پایدار به مسیر `/data` متصل کنید.
4. دستور اجرا را در `Procfile` یا تنظیمات سرویس بررسی کنید:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

5. یک دامنهٔ عمومی ایجاد و سپس `/health` و `/login` را آزمایش کنید.

> تعریف `DATA_DIR=/data` به‌تنهایی فضای پایدار ایجاد نمی‌کند؛ Volume باید واقعاً متصل باشد و برنامه نیز از مسیر درست استفاده کند.

راهنمای تکمیلی نصب و عیب‌یابی در [`INSTALL.md`](INSTALL.md) قرار دارد.

## 🛡️ امنیت و نگهداری اطلاعات

- اطلاعات محرمانه را داخل کد یا مخزن عمومی قرار ندهید.
- رمزها و کلیدهای امنیتی را از متغیرهای محیطی تنظیم کنید.
- برای حفظ اطلاعات بین Deployها، فضای ذخیره‌سازی پایدار را به‌درستی پیکربندی کنید.
- اگر از پشتیبان GitHub استفاده می‌کنید، `GH_PERSIST_TOKEN` و `GH_PERSIST_REPO` را در تنظیمات محرمانهٔ سرویس قرار دهید.
- برای توکن دسترسی، حداقل سطح دسترسی موردنیاز را انتخاب کنید.
- فایل‌های پشتیبان را عمومی منتشر نکنید؛ ممکن است حاوی UUID، لینک اشتراک یا اطلاعات مدیریتی باشند.
- پیش از انتشار نسخهٔ جدید، پشتیبان تهیه کنید و ورود، ساخت کانفیگ و مدیریت گروه‌ها را آزمایش کنید.

## 📱 برنامه‌های سازگار

| پلتفرم | برنامه | لینک دریافت |
|---|---|---|
| Android | V2Box | [Google Play](https://play.google.com/store/apps/details?id=dev.hexasoftware.v2box) |
| Android | Hiddify | [Google Play](https://play.google.com/store/apps/details?id=app.hiddify.com) |
| iPhone | V2Box | [App Store](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) |
| Windows | Hiddify | [انتشارهای رسمی](https://github.com/hiddify/hiddify-app/releases/latest) |

دسترس‌پذیری برنامه‌ها ممکن است بسته به کشور، دستگاه و فروشگاه متفاوت باشد.

## 🎁 حمایت اختیاری

اگر FineVPN_v2ray برایتان مفید بوده است، می‌توانید به‌صورت کاملاً اختیاری از سازنده حمایت کنید. نوع و مقدار هدیه به انتخاب شماست.

برای هماهنگی: [@sadiq_AFG1](https://t.me/sadiq_AFG1)

استفاده از پروژه نیازمند پرداخت یا هدیه نیست. در این مخزن سیستم فروش یا پرداخت خودکار فعال نشده است.

## 🐛 گزارش مشکل و مشارکت

برای گزارش مشکل، در صورت امکان این موارد را ارائه دهید:

- نسخهٔ Python و محیط اجرا
- شرح مشکل و مراحل بازتولید آن
- پیام خطای غیرمحرمانه

رمز عبور، توکن، UUID و لینک اشتراک واقعی را در Issue عمومی منتشر نکنید.

---

<p align="center">
  <strong>FineVPN_v2ray</strong><br>
  <sub>مدیریت ساده‌تر؛ کنترل بیشتر؛ تجربه‌ای بهتر</sub><br><br>
  <a href="https://github.com/MuhammadSadiqAfghan/FineVPN-v2ray">مشاهدهٔ پروژه در GitHub</a>
  · <a href="https://t.me/sadiq_AFG1">تماس با سازنده</a>
</p>
