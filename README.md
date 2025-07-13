# SkinDx – Deep Learning Based Skin Disease Diagnosis

SkinDx is a web-based application designed to detect and identify common skin diseases using deep learning models. Users can upload images of their skin, and the system will provide a predicted diagnosis with confidence. Built with Django and integrated with Google OAuth for secure authentication.

---

## 🔧 Features

- 🌐 Google Login (OAuth2)
- 🧠 Deep Learning Integration (CNN-based)
- 📁 Image Upload and Prediction System
- 📊 Free Trial Logic (3 free tests per user)
- 💸 Payment Gateway Placeholder (for extended access)
- 🖼️ Background Blur with Glass UI Effect
- 🎨 Responsive and Stylish UI (based on Figma design)

---

## ⚙️ Tech Stack

- **Backend:** Django 5.x
- **Frontend:** HTML5, CSS3
- **Auth:** Google OAuth (django-allauth)
- **ML:** TensorFlow / PyTorch (Planned)
- **Database:** MySQL (via XAMPP)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AbhishekKaisar/SkinDx-DeepLearning-Diagnosis.git
cd SkinDx-DeepLearning-Diagnosis
````

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL in `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'skindx_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Make sure your MySQL service is running via **XAMPP** and the database `skindx_db` is created.

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start Development Server

```bash
python manage.py runserver
```

---

## 🧪 Testing Skin Analysis

After logging in with Google:

* Navigate to **Try Free Now**
* Upload a skin image (under 1MB, square size recommended)
* Get AI-generated prediction
* After 3 tests, a payment page will appear

---

## 📁 Folder Structure

```
├── core/
│   ├── templates/
│   ├── static/
│   ├── views.py
├── skindx/
│   ├── settings.py
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📌 Notes

* Favicon and logo are located in `core/static/images/`
* Background image is fixed and blurred only in hero section
* Model integration code is placeholder-ready