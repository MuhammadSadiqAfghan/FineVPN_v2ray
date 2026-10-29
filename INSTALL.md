<div dir="rtl">

# راهنمای نصب و اجرا — FineVPN_v2ray

این راهنما اجرای محلی و استقرار روی Railway و Hostless را توضیح می‌دهد. قبل از انتشار عمومی، رمزهای پیش‌فرض را تغییر دهید و پایداری ذخیره‌سازی را واقعاً آزمایش کنید.

## ۱. دریافت پروژه از GitHub

### دانلود ZIP

1. صفحهٔ مخزن [FineVPN_v2ray](https://github.com/MuhammadSadiqAfghan/FineVPN-v2ray) را باز کنید.
2. دکمهٔ **Code** را بزنید.
3. **Download ZIP** را انتخاب کنید.
4. فایل ZIP را از حالت فشرده خارج کنید و ترمینال را در پوشه‌ای باز کنید که `main.py` و `requirements.txt` داخل آن قرار دارند.

### دریافت با Git

```bash
git clone https://github.com/MuhammadSadiqAfghan/FineVPN-v2ray.git
cd FineVPN_v2ray
```

اگر مخزن خصوصی است، باید حساب شما مجوز دسترسی داشته باشد.

## ۲. اجرای محلی در Linux/macOS

پیشنهاد می‌شود از Python 3.11 یا نسخهٔ سازگار جدیدتر استفاده کنید.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
export ADMIN_USERNAME='your-admin-name'
export ADMIN_PASSWORD='replace-with-a-long-unique-password'
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
uvicorn main:app --host 0.0.0.0 --port 8000
```

سپس باز کنید: `http://127.0.0.1:8000/login`

## ۳. اجرای محلی در Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
$env:ADMIN_USERNAME='your-admin-name'
$env:ADMIN_PASSWORD='replace-with-a-long-unique-password'
$env:SECRET_KEY=(python -c "import secrets; print(secrets.token_urlsafe(48))")
uvicorn main:app --host 0.0.0.0 --port 8000
```

اگر PowerShell اجرای اسکریپت فعال‌سازی را مسدود کرد، می‌توانید از Command Prompt و فایل `.venv\Scripts\activate.bat` استفاده کنید. این تغییر به تنظیمات دائمی امنیت ویندوز نیاز ندارد.

## ۴. استقرار روی Railway از طریق GitHub

### مرحلهٔ اول: اتصال مخزن

1. وارد [Railway](https://railway.com/) شوید.
2. از داشبورد، پروژهٔ جدید بسازید و گزینهٔ Deploy from GitHub Repo (یا گزینهٔ مشابه در داشبورد فعلی) را انتخاب کنید.
3. حساب GitHub را متصل کرده و مخزن `FineVPN_v2ray` را انتخاب کنید.
4. صبر کنید Build و Deploy تمام شود. در صورت شکست، به Deployment → Build Logs و Deploy Logs بروید و اولین خطای واقعی را پیدا کنید.

### مرحلهٔ دوم: تنظیم متغیرهای محرمانه

در تنظیمات سرویس Railway، بخش Variables را باز کنید و متغیرهای زیر را اضافه کنید:

| متغیر | مقدار | توضیح |
|---|---|---|
| `ADMIN_USERNAME` | نام کاربری قوی و غیرقابل حدس | نام ورود مدیر |
| `ADMIN_PASSWORD` | رمز قوی و منحصربه‌فرد | رمز ورود مدیر؛ در چت یا GitHub قرار ندهید |
| `SECRET_KEY` | مقدار تصادفی طولانی | برای پایداری کلید، آن را بین Deployها ثابت نگه دارید |
| `VPN_COUNTRY_CODE` | `FI` | فقط پرچم و برچسب نام کلاینت را تعیین می‌کند؛ خروجی کشور را تغییر نمی‌دهد |
| `DATA_DIR` | `/data` (اختیاری) | مسیر داده؛ بدون Volume پایدار تضمین ماندگاری نیست |

برای تولید `SECRET_KEY` در محیط خود می‌توانید از Python استفاده کنید:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

این مقدار را به‌عنوان Variable محرمانه ثبت کنید؛ آن را در فایل‌های مخزن Commit نکنید. بعد از اضافه‌کردن متغیرها، سرویس را دوباره Deploy کنید.

### مرحلهٔ سوم: اتصال Volume پایدار

1. در داشبورد Railway به سرویس مربوطه بروید.
2. بخش **Settings → Volumes** یا مدیریت Volume در داشبورد فعلی را باز کنید.
3. یک Volume جدید بسازید.
4. **Mount Path** را دقیقاً `/data` تنظیم کنید.
5. صبر کنید استقرار مجدد تمام شود.
6. بعد از Deploy به `/health` بروید و بررسی کنید که مسیر داده و وضعیت Volume معقول باشد. از برنامه نیز یک بکاپ دستی بگیرید.

**مهم:** نوشتنی‌بودن `/data` به معنی ذخیره‌سازی پایدار نیست. Volume باید از طریق تنظیمات پلتفرم واقعاً متصل شده باشد. فایل‌های تنظیم استقرار این پروژه ممکن است در پلتفرم یا نسخهٔ جدید داشبورد، همهٔ مراحل اتصال Volume را خودکار ایجاد نکنند؛ وضعیت را در داشبورد بررسی کنید.

### مرحلهٔ چهارم: دستور اجرا و دامنه

دستور اجرای پروژه:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

در صورت نیاز همین دستور را در تنظیمات Start Command سرویس وارد کنید. Health check path باید `/health` باشد. سپس از بخش Networking دامنهٔ عمومی بسازید (Generate Domain یا گزینهٔ متناظر). بعد از استقرار این آدرس‌ها را بررسی کنید:

- `/health` — وضعیت سلامت سرور
- `/login` — صفحهٔ ورود مدیر
- `/` — هدایت به صفحهٔ ورود (`/login`)

اگر دامنهٔ سفارشی دارید، TLS/DNS آن را در تنظیمات پلتفرم تکمیل کنید. لینک اشتراک باید از دامنهٔ عمومی صحیح تولید شود.

### مرحلهٔ پنجم: ذخیره‌سازی جایگزین با GitHub (اختیاری)

در پروژه، پشتیبان‌گیری روی مخزن GitHub هم از طریق متغیرها قابل تنظیم است. این گزینه جایگزین ایده‌آل Volume نیست و باید با دقت استفاده شود، چون ذخیرهٔ وضعیت می‌تواند اطلاعات حساس کاربران/اشتراک‌ها را در مخزن بنویسد.

- `GH_PERSIST_TOKEN`: توکن دارای حداقل دسترسی لازم به مخزن هدف.
- `GH_PERSIST_REPO`: نام مخزن به شکل `owner/repository`.
- `GH_PERSIST_PATH`: مسیر فایل وضعیت؛ پیش‌فرض `state/panel_state.json`.
- `GH_PERSIST_BRANCH`: شاخهٔ وضعیت؛ پیش‌فرض `state`.

این متغیرها را فقط در بخش Secrets/Variables سرویس نگه دارید. قبل از استفاده، مخزن هدف را خصوصی کنید، scope توکن را بررسی کنید و بعد از تست مطمئن شوید فایل وضعیت هرگز در مخزن عمومی ذخیره نمی‌شود.

## استقرار روی Hostless با Docker

این نسخه شامل `Dockerfile` و `hostless.yaml` است تا ساخت برنامه به‌جای Railpack/Mise از Docker و Python 3.11 استفاده کند.

1. تمام محتوای پروژه، از جمله `README.md`، پوشهٔ `assets/`، `Dockerfile`، `.dockerignore` و `hostless.yaml` را در ریشهٔ مخزن قرار دهید؛ این کار باعث می‌شود بنر GIF در بالای صفحهٔ README در GitHub نمایش داده شود.
2. در Hostless بررسی کنید که مخزن و شاخه درست هستند و Working Directory روی ریشهٔ مخزن قرار دارد.
3. مطمئن شوید Build System روی **Docker** است. اگر تنظیمات فایل `hostless.yaml` به‌صورت خودکار اعمال نشده، آن را در تنظیمات Hostless انتخاب کنید و مسیر Dockerfile را `./Dockerfile` بگذارید.
4. در **Environment variables**، مقادیر `ADMIN_USERNAME`، `ADMIN_PASSWORD` و `SECRET_KEY` را نگه دارید یا تنظیم کنید. مقادیر محرمانه را در `hostless.yaml` وارد نکنید.
5. Deploy را اجرا و Build Logs را بررسی کنید. پس از اجرا، `/health` باید پاسخ موفق بدهد.

اگر Build با Docker هم شکست خورد، لاگ جدید را بررسی کنید؛ خطای قبلی `secret SECRET: not found` در مرحلهٔ نصب Python در Railpack رخ داده بود و با تست محلی برنامه قابل بازتولید نبود.

## ۵. اولین ورود و امن‌سازی

1. در `/login` با `ADMIN_USERNAME` و `ADMIN_PASSWORD` تعریف‌شده وارد شوید.
2. رمز را در جای امن نگه دارید و با دیگران به اشتراک نگذارید.
3. نسخهٔ پشتیبان را دانلود و به‌شکل خصوصی نگهداری کنید.
4. بررسی کنید که صفحهٔ اشتراک در V2Box/Hiddify وارد می‌شود. نام و پرچم کانفیگ به برچسب کشور تنظیم‌شده بستگی دارند و خودشان سرور خروجی را عوض نمی‌کنند.
5. IP خروجی را از داخل یک کلاینت VPN متصل بررسی کنید تا پرچم با کشور واقعی هماهنگ باشد.

## ۶. رفع خطاهای رایج

### Build شکست می‌خورد

- در Build Logs اولین خطای Python یا `pip` را بررسی کنید.
- مطمئن شوید `requirements.txt` و `main.py` در ریشهٔ مخزن هستند.
- پس از اصلاح وابستگی، Build را دوباره اجرا کنید.

### سرویس Deploy نمی‌شود یا PORT مشکل دارد

- Start Command باید `$PORT` را بخواند و روی `0.0.0.0` گوش کند.
- از اجرای `python main.py` به‌جای Uvicorn در Start Command خودداری کنید مگر اینکه دلیل مشخصی داشته باشید.
- Deploy Logs را برای خطای Import، پورت یا crash بررسی کنید.

### صفحه باز نمی‌شود

- دامنه در بخش Networking ساخته شده باشد.
- `/health` را باز کنید و Logs را بررسی کنید.
- چند لحظه بعد از Deploy دوباره بررسی کنید؛ اگر سرویس crash می‌کند، پیام خطای اول را نگه دارید.

### رمز مدیر پذیرفته نمی‌شود

- متغیرهای `ADMIN_USERNAME` و `ADMIN_PASSWORD` را در سرویس درست بررسی کنید.
- در این پروژه ممکن است اعتبارنامهٔ ذخیره‌شده در فایل وضعیت، مقدارهای محیطی را تحت‌الشعاع قرار دهد؛ قبل از استفادهٔ عمومی، روش ورود/بازیابی را در یک نسخهٔ آزمایشی بررسی کنید.
- فایل دیتابیس یا کلید محرمانه را به شکل تصادفی حذف نکنید، چون ممکن است نشست‌ها یا اطلاعات از دست بروند.

### داده‌ها پس از Deploy ناپدید می‌شوند

- بررسی کنید Volume واقعی به `/data` mount شده باشد.
- پیش از هر تغییر ذخیره‌سازی بکاپ بگیرید.
- به `DATA_DIR=/data` به‌تنهایی به‌عنوان تضمین ماندگاری تکیه نکنید.

### سرعت آپلود/دانلود صفر است

- سرعت از افزایش شمارنده‌های واقعی ترافیک محاسبه می‌شود؛ در بارگذاری اول یا بدون استفاده، مقدار صفر طبیعی است.
- کانفیگ واقعاً متصل باشد و از آن ترافیک عبور کند.
- نمایش هدر `announce` و برچسب‌های subscription در همهٔ کلاینت‌ها تضمین نیست و به پشتیبانی هر کلاینت بستگی دارد.

### اتصال VPN برقرار نمی‌شود

- آدرس دامنهٔ عمومی، TLS/SNI، پورت و پروتکل انتخابی را بررسی کنید.
- از URL واقعی کانفیگ و IP خروجی یک کلاینت متصل استفاده کنید.
- Logs را بدون افشای UUID یا لینک اشتراک عمومی ارسال کنید.

## ۷. مواردی که هرگز نباید عمومی شوند

`ADMIN_PASSWORD`، `SECRET_KEY`، توکن GitHub، فایل‌های بکاپ، لینک اشتراک زنده و UUIDها. اگر یکی از این موارد افشا شد، آن را باطل یا تعویض کنید.

## پیوندهای رسمی

- [مخزن پروژه در GitHub](https://github.com/MuhammadSadiqAfghan/FineVPN-v2ray)
- [Railway Quick Start](https://docs.railway.com/quick-start)
- [Railway Volumes](https://docs.railway.com/volumes)
- [Railway Domains](https://docs.railway.com/networking/domains/working-with-domains)
- [V2Box Android](https://play.google.com/store/apps/details?id=dev.hexasoftware.v2box)
- [V2Box iPhone](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690)
- [Hiddify Android](https://play.google.com/store/apps/details?id=app.hiddify.com)
- [Hiddify Windows/official releases](https://github.com/hiddify/hiddify-app/releases/latest)

</div>
