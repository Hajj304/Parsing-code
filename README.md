تمام، سأجهز لك **ملف كامل** بصيغة `README.md` يحتوي على شرح الأكواد الثلاثة التي عملنا عليها في Google Colab:

1. **Parsing Code بسيط** (قراءة نص واستخراج كلمات/أرقام).
2. **Parsing HTML من رابط موقع** (باستخدام BeautifulSoup).
3. **Parsing في Workflow n8n** (فكرة عن التعامل مع JSON وبيانات API داخل n8n).

سأكتب الملف جاهز للعرض في GitHub، منظم بالعناوين والكود مع الشرح.

---

````markdown
# 📌 أمثلة على Parsing Code في Python و n8n

هذا المشروع يحتوي على ثلاثة أمثلة عملية لشرح مفهوم **Parsing** في البرمجة باستخدام Python وبيئة **n8n**.

---

## 📝 1. مثال بسيط على Parsing نصوص (Python)

في هذا المثال سنقوم بقراءة نص ثم استخراج الكلمات والأرقام منه.

```python
# استيراد المكتبات
import re

# نص تجريبي
text = "مرحباً، هذا مثال Parsing! الرقم هو 1234"

# استخراج الكلمات
words = re.findall(r'\w+', text)

# استخراج الأرقام
numbers = re.findall(r'\d+', text)

print("📄 الكلمات:", words)
print("🔢 الأرقام:", numbers)
````

**الشرح:**

* نستخدم `re.findall` لاستخراج الأنماط.
* `\w+` تعني أي كلمة.
* `\d+` تعني أي رقم.

---

## 🌐 2. استخراج معلومات من موقع ويب (Web Scraping)

سنقوم بتحميل صفحة ويب واستخراج العنوان الرئيسي `<title>`.

```python
# استيراد المكتبات
import requests
from bs4 import BeautifulSoup

# رابط الموقع
url = "https://example.com"

# جلب محتوى الصفحة
response = requests.get(url)

# تحويل HTML إلى كائن يمكن تحليله
soup = BeautifulSoup(response.text, "html.parser")

# استخراج عنوان الصفحة
page_title = soup.title.string

print("📌 عنوان الصفحة:", page_title)
```

**الشرح:**

* `requests` لجلب محتوى الموقع.
* `BeautifulSoup` لتحليل الـ HTML.
* `soup.title.string` للوصول لعنوان الصفحة.

---

## ⚙️ 3. مثال Parsing في Workflow n8n

في **n8n** يمكننا استخدام عقدة **Function** لمعالجة بيانات JSON قادمة من API.

📌 **كود عقدة Function**:

```javascript
// قراءة البيانات القادمة من العقدة السابقة
const data = items[0].json;

// استخراج حقل محدد
const name = data.name;
const email = data.email;

// إعادة النتيجة
return [{
  json: {
    fullName: name,
    contactEmail: email
  }
}];
```

**الشرح:**

* `items[0].json` تمثل أول عنصر JSON في سير العمل.
* نستخرج القيم المطلوبة (`name` و `email`).
* نعيد البيانات بشكل JSON جديد.

---

## 📂 تشغيل الأكواد في Google Colab

يمكنك نسخ الأكواد الأولى والثانية وتشغيلها مباشرة على Google Colab، أما الكود الثالث فهو مخصص لبيئة n8n.

---

## 📜 المتطلبات

لتشغيل الأمثلة على Python:

```bash
pip install requests beautifulsoup4
```

---

✍️ **المؤلف:** Mawardi
📅 **التاريخ:** 2025-08-07

```

---

أنا أقترح بعد هذا أن أعمل لك أيضًا **ملف Colab Notebook** يحوي الأكواد الثلاثة جاهزة للتشغيل مع التعليقات.  
هل تريد أن أجهزه الآن ليكون جاهز للرفع مع الـ README على GitHub؟
```
