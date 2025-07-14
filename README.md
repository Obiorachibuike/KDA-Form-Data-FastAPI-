# 🚂 KPA Form Data API Backend

A backend project developed with **FastAPI** and **PostgreSQL** to implement two production-ready APIs for railway wheel specification data, based on the official [KPA Form Data Swagger API Documentation](https://app.swaggerhub.com/apis/sarvasuvidhaen/kpa-form_data/1.0.0).

---

## 📌 Project Objective

To demonstrate backend development skills by building two fully functional and well-documented APIs based on a provided Postman collection and Swagger docs, with features like:

- Data validation and persistence
- Query-based filtering
- Modular, production-grade FastAPI structure
- PostgreSQL integration

---

## ✅ Implemented APIs

### 1. **Submit Wheel Specification**
- **Endpoint**: `POST /api/forms/wheel-specifications`
- **Description**: Accepts wheel specification data and saves it to the database.
- **Request Format**:
```json
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
```

- **Success Response (201)**:
```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "status": "Saved"
  }
}
```

### 2. **Get Filtered Wheel Specifications**
- **Endpoint**: `GET /api/forms/wheel-specifications`
- **Description**: Returns a list of forms filtered by `formNumber`, `submittedBy`, or `submittedDate`.
- **Example Request**:
```
GET /api/forms/wheel-specifications?submittedBy=user_id_123
```
- **Success Response (200)**:
```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": { ... }
    }
  ]
}
```

---

## 🛠️ Tech Stack

| Technology       | Purpose                      |
|------------------|------------------------------|
| FastAPI          | Backend framework            |
| PostgreSQL       | Database                     |
| SQLAlchemy       | ORM                          |
| Pydantic         | Request & Response validation |
| Uvicorn          | ASGI server                  |
| python-dotenv    | Environment configuration     |

---

## 📁 Project Structure

```
kpa_form_backend/
├── app/
│   ├── __init__.py
│   ├── crud.py           # DB logic
│   ├── database.py       # DB connection
│   ├── main.py           # FastAPI app entrypoint
│   ├── models.py         # SQLAlchemy models
│   ├── routes.py         # Endpoints
│   └── schemas.py        # Pydantic models
├── .env                  # Environment variables
├── requirements.txt      # Dependencies
└── README.md             # Project description
```

---

## 🚀 Setup & Running Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/kpa_form_backend.git
   cd kpa_form_backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**: Create a `.env` file:
   ```
   DATABASE_URL=postgresql://kpa_db_o5em_user:RonszX8To0qDCWd3b6AfsPNjthIUeZAh@dpg-d1pmm7k9c44c738pdmfg-a.oregon-postgres.render.com:5432/kpa_db_o5em
   ```

5. **Run the app**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Visit Docs**
   - Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## ✅ Features Summary

- Two endpoints implemented as per Swagger spec.
- Input validation with Pydantic.
- PostgreSQL integration via SQLAlchemy ORM.
- Modular FastAPI codebase.
- `.env` support for secure config.
- Swagger UI for live API testing.
- Optional Render deployment ready.

---

## 📤 Submission Assets

| Item                     | Link (example)                                   |
|--------------------------|--------------------------------------------------|
| 🔗 Source Code (zip)     | https://drive.com/yourname_api_assignment.zip    |
| 🧪 Postman Collection     | https://drive.com/yourname_postman_collection.json|
| 📘 README (txt)          | https://drive.com/yourname_readme.txt            |

---

## 👤 Author

Your Name  
📧 [obiorachibuike22@gmail.com]  
📝 Submitted to: [contact@suvidhaen.com]

---

## 🏁 Final Note

This project meets all requirements from the assignment brief. If needed, the API can be extended to support authentication, file uploads, or additional forms as per future use cases.

---
