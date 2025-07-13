Sure! Here's the complete and polished README.md file for your kpa_form_backend FastAPI project:


---

📄 README.md

# 🚀 KPA Form Data API

A FastAPI-based backend service to manage and retrieve wheel specification form data, based on the provided Swagger API documentation.

---

## 📦 Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **Server**: Uvicorn (ASGI server)
- **Language**: Python 3.9+

---

## 📁 Project Structure

kpa_form_backend/ ├── app/ │   ├── init.py               # App package initializer │   ├── crud.py                   # DB operations (create, fetch) │   ├── database.py               # DB connection and session │   ├── main.py                   # FastAPI app entrypoint │   ├── models.py                 # SQLAlchemy models │   ├── routes.py                 # API endpoints │   └── schemas.py                # Pydantic models ├── .env                          # (Optional) Environment variables ├── requirements.txt              # Dependencies list └── README.md                     # Setup guide and documentation

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.9+
- PostgreSQL installed and running
- Create a PostgreSQL database named `kpa_db`

### 🔧 Step-by-Step

1. **Clone the repo or unzip the project:**

```bash
git clone https://github.com/yourusername/kpa_form_backend.git
cd kpa_form_backend

2. Install dependencies:



pip install -r requirements.txt

3. Edit the database connection:



In app/database.py, update the DATABASE_URL if your credentials differ:

DATABASE_URL = "postgresql://postgres:yourpassword@localhost:5432/kpa_db"

4. Run the server:



uvicorn app.main:app --reload

5. Access the API docs:



Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc



---

🔌 API Endpoints

✅ POST /api/forms/wheel-specifications

Submit a new wheel specification form.

Request Body Example:

{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
    "bearingSeatDiameter": "130.043 TO 130.068",
    "condemningDia": "825 (800-900)",
    "intermediateWWP": "20 TO 28",
    "lastShopIssueSize": "837 (800-900)",
    "rollerBearingBoreDia": "130 (+0.0/-0.025)",
    "rollerBearingOuterDia": "280 (+0.0/-0.035)",
    "rollerBearingWidth": "93 (+0/-0.250)",
    "treadDiameterNew": "915 (900-1000)",
    "variationSameAxle": "0.5",
    "variationSameBogie": "5",
    "variationSameCoach": "13",
    "wheelDiscWidth": "127 (+4/-0)",
    "wheelGauge": "1600 (+2,-1)",
    "wheelProfile": "29.4 Flange Thickness"
  }
}

Response:

{
  "data": {
    "formNumber": "WHEEL-2025-001",
    "status": "Saved",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03"
  },
  "message": "Wheel specification submitted successfully.",
  "success": true
}


---

🔍 GET /api/forms/wheel-specifications?formNumber=...&submittedBy=...&submittedDate=...

Get submitted forms filtered by form number, submitted by, or date.

Query Example:

/api/forms/wheel-specifications?formNumber=WHEEL-2025-001

Response:

{
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
        ...
        "wheelProfile": "29.4 Flange Thickness"
      }
    }
  ],
  "message": "Filtered wheel specification forms fetched successfully.",
  "success": true
}


---

🧪 Testing

You can use:

Postman

Swagger UI (/docs)

Curl or HTTP clients



---

📌 Notes

Data is stored in a PostgreSQL table wheel_specifications.

You can extend the models for updates, deletions, or authentication later.

Form number must be unique to avoid duplicates.



---

🙋‍♂️ Author

Chibuike Praise Obiora
GitHub
Email


---

Let me know if you'd like me to bundle this README.md with the code again or help create a Postman collection for testing!



