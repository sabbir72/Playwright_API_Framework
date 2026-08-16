# 🗺️ PLAYWRIGHT API FRAMEWORK - PROJECT MAP & COMMAND GUIDE

## 1. PROJECT OVERVIEW

**What is this?**
- A Python-based **API Testing Framework** using Playwright
- Focus: **Authentication API Testing**
- Test Framework: **Pytest**
- Reporting: **Allure Reports**
- Test Data: JSON payloads
- Logging: File + Console logging

**Purpose:**
Test REST APIs with focus on authentication flows (login, user info) and negative scenarios.

---

## 2. PROJECT STRUCTURE

```
Playwright_API_Framework/
│
├── api/                          # API Layer
│   ├── api_client.py            # Core HTTP client (GET, POST, PUT, DELETE)
│   └── auth_api.py              # Authentication endpoints
│
├── test/                         # Test Cases
│   ├── test_auth.py             # Get current user tests
│   ├── test_auth_positive.py    # Successful login tests
│   ├── test_auth_negative.py    # Failed login scenarios
│   └── test_smoke.py            # Smoke tests (Products API)
│
├── utils/                        # Utilities
│   ├── config.py                # Configuration (BASE_URL, timeouts)
│   └── logger.py                # Logging setup
│
├── payloads/                     # Test Data
│   └── login_payload.json       # Login credentials
│
├── conftest.py                   # Pytest fixtures
├── pytest.ini                    # Pytest configuration
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables
└── logs/                         # Generated test logs
```

---

## 3. MAIN MODULES

| Module | Purpose | File |
|--------|---------|------|
| **API Client** | HTTP requests wrapper | `api/api_client.py` |
| **Auth API** | Authentication endpoints | `api/auth_api.py` |
| **Authentication Tests** | Login, user info tests | `test/test_auth*.py` |
| **Configuration** | BASE_URL, timeouts | `utils/config.py` |
| **Logging** | Logs to file & console | `utils/logger.py` |
| **Fixtures** | Pytest test fixtures | `conftest.py` |

---

## 4. MODULE-BY-MODULE WALKTHROUGH

### **MODULE 1: API CLIENT** (`api/api_client.py`)

**Purpose:** Core HTTP communication layer

**View API Client:**
```powershell
Get-Content api\api_client.py
```

**What's inside:**
- Playwright request context initialization
- 4 HTTP methods: GET, POST, PUT, DELETE
- Logging for all requests/responses
- Connection management

**Flow:**
```
APIClient()
    ↓
Playwright Request Context
    ↓
GET / POST / PUT / DELETE
    ↓
Log + Return Response
```

---

### **MODULE 2: AUTHENTICATION API** (`api/auth_api.py`)

**Purpose:** Authentication business logic

**View Auth API:**
```powershell
Get-Content api\auth_api.py
```

**What's inside:**
- `login()` → POST /auth/login
- `get_user_info()` → GET /auth/me

**Flow:**
```
Login Request
    ↓
POST /auth/login with username + password
    ↓
Response: {accessToken, refreshToken, id, username}
    ↓
Get User Info
    ↓
GET /auth/me with Bearer token
    ↓
Response: {id, username}
```

---

### **MODULE 3: CONFIGURATION** (`utils/config.py`)

**Purpose:** Environment configuration

**View Configuration:**
```powershell
Get-Content utils\config.py
```

**What's inside:**
- `BASE_URL` → https://dummyjson.com
- `API_TIMEOUT` → 30000ms

**Where to change settings:**
```powershell
Get-Content .env
```

---

### **MODULE 4: LOGGING** (`utils/logger.py`)

**Purpose:** Test execution logging

**View Logger Setup:**
```powershell
Get-Content utils\logger.py
```

**What it does:** Configure logging to file and console

**Logs are saved to:**
```powershell
Get-Content logs\api_test.log
```

---

### **MODULE 5: TEST FIXTURES** (`conftest.py`)

**Purpose:** Pytest fixtures for all tests

**View Fixtures:**
```powershell
Get-Content conftest.py
```

**Available fixtures:**
- `api_client` → APIClient instance
- `auth_token` → Valid JWT token

**Usage in tests:**
```python
def test_example(api_client, auth_token):
    # api_client and auth_token are auto-injected
```

---

## 5. TEST MODULES

### **TEST FILE 1: test_auth_positive.py** - Successful Scenarios

**View Positive Tests:**
```powershell
Get-Content test\test_auth_positive.py
```

**What it tests:**
- ✅ Login success with valid credentials
- ✅ Response status = 200
- ✅ Username matches payload
- ✅ User ID is valid (> 0)
- ✅ Access Token returned
- ✅ Refresh Token returned

**Run this test:**
```powershell
pytest test\test_auth_positive.py -v
```

---

### **TEST FILE 2: test_auth_negative.py** - Error Scenarios

**View Negative Tests:**
```powershell
Get-Content test\test_auth_negative.py
```

**What it tests:**
- ❌ Wrong password → 400 error
- ❌ Wrong username → 400 error
- ❌ Wrong username + password → 400 error
- ❌ Missing password → 400 error
- ❌ Missing username → 400 error
- ❌ Empty username → 400 error

**Run this test:**
```powershell
pytest test\test_auth_negative.py -v
```

---

### **TEST FILE 3: test_auth.py** - Get Current User

**View Current User Tests:**
```powershell
Get-Content test\test_auth.py
```

**What it tests:**
- ✅ Requires valid token from login
- ✅ GET /auth/me returns user info
- ✅ Username is string and non-empty
- ✅ User ID is integer and > 0

**Run this test:**
```powershell
pytest test\test_auth.py -v
```

---

### **TEST FILE 4: test_smoke.py** - Products API

**View Smoke Tests:**
```powershell
Get-Content test\test_smoke.py
```

**What it tests:**
- ✅ GET /products/1 returns product
- ✅ Product has id, title, description, price

**Run this test:**
```powershell
pytest test\test_smoke.py -v
```

---

## 6. TEST DATA

**View Login Payload:**
```powershell
Get-Content payloads\login_payload.json
```

**What's inside:**
```json
{
    "username": "emilys",
    "password": "emilyspass"
}
```

---

## 7. RUNNING TESTS

### **Run ALL Tests**
```powershell
pytest
```

### **Run ALL Tests with VERBOSE Output**
```powershell
pytest -v
```

### **Run Specific Test File**
```powershell
pytest test\test_auth_positive.py -v
```

### **Run Specific Test Function**
```powershell
pytest test\test_auth_positive.py::test_login_success -v
```

### **Run Tests from Pytest Config**
```powershell
pytest -c pytest.ini
```

### **Run Tests with Allure Report**
```powershell
pytest --alluredir=allure-results
```

### **View Allure Report** (after running tests)
```powershell
allure serve allure-results
```

---

## 8. PROJECT CONFIGURATION

### **View Pytest Config**
```powershell
Get-Content pytest.ini
```

**Settings:**
- Test path: `test/`
- Test file pattern: `test_*.py`
- Test function pattern: `test_*`
- Options: `-v -s` (verbose + print output)

---

### **View Requirements**
```powershell
Get-Content requirements.txt
```

**Dependencies:**
- pytest → Test framework
- playwright → Browser automation
- pytest-playwright → Integration
- allure-pytest → Reporting
- jsonschema → Validation
- python-dotenv → Environment variables

---

### **View Environment File**
```powershell
Get-Content .env
```

**Environment Variables:**
- `BASE_URL` → API base URL
- `API_TIMEOUT` → Request timeout in ms

---

## 9. WHERE IS WHAT?

| Task | Location | File |
|------|----------|------|
| Add new HTTP method | `api/api_client.py` | api_client.py |
| Add new API endpoint | `api/auth_api.py` | auth_api.py |
| Create new test | `test/` | test_*.py |
| Change BASE_URL | `.env` | .env |
| Change timeout | `.env` | .env |
| Create test data | `payloads/` | *.json |
| Configure logging | `utils/logger.py` | logger.py |
| Add test fixture | `conftest.py` | conftest.py |
| View test logs | `logs/` | api_test.log |
| View test reports | `allure-results/` | *.json |

---

## 10. QA QUICK NAVIGATION

### **How to Test Login Feature?**

**Step 1: Understand Login Flow**
```powershell
Get-Content api\auth_api.py
```
*See: login() method calls POST /auth/login*

**Step 2: View Test Cases**
```powershell
Get-Content test\test_auth_positive.py
```
*See: Successful login scenarios*

**Step 3: View Negative Cases**
```powershell
Get-Content test\test_auth_negative.py
```
*See: Failed login scenarios*

**Step 4: View Test Data**
```powershell
Get-Content payloads\login_payload.json
```
*See: Login credentials*

**Step 5: Run Login Tests**
```powershell
pytest test\test_auth_positive.py test\test_auth_negative.py -v
```

**Step 6: View Results**
```powershell
Get-Content logs\api_test.log
```

---

### **How to Test Get User Info Feature?**

**Step 1: View Test**
```powershell
Get-Content test\test_auth.py
```

**Step 2: Run Test**
```powershell
pytest test\test_auth.py -v
```

**Step 3: View Logs**
```powershell
Get-Content logs\api_test.log
```

---

## 11. DEVELOPER QUICK NAVIGATION

### **I need to modify API Client (HTTP methods)**
```powershell
Get-Content api\api_client.py
```
Location: `api/api_client.py`

---

### **I need to add a new API endpoint**
```powershell
Get-Content api\auth_api.py
```
Location: `api/auth_api.py`

**Example: Add new method**
```python
def logout(self):
    logger.info("Starting Logout API")
    response = self.api_client.post("/auth/logout")
    return response
```

---

### **I need to create a new test**
```powershell
# Create new file: test\test_new_feature.py
# Use existing test as template
Get-Content test\test_auth_positive.py
```
Location: `test/test_*.py`

---

### **I need to change environment settings**
```powershell
Get-Content .env
```
Location: `.env`

**Options:**
- `BASE_URL` → API endpoint
- `API_TIMEOUT` → Request timeout

---

### **I need to add test data**
```powershell
Get-Content payloads\login_payload.json
```
Location: `payloads/*.json`

---

### **I need to view test logs**
```powershell
Get-Content logs\api_test.log
```
Location: `logs/api_test.log`

---

## 12. API ENDPOINT MAP

### **Authentication Endpoints**

| Method | Endpoint | Purpose | Located In |
|--------|----------|---------|-----------|
| POST | `/auth/login` | Login with credentials | `api/auth_api.py` |
| GET | `/auth/me` | Get current user info | `api/auth_api.py` |
| GET | `/products/1` | Get product info | `test/test_smoke.py` |

---

## 13. FEATURE FLOW - LOGIN FEATURE

```
LOGIN FEATURE FLOW
│
├─ UI Test → Not in this project (API only)
│
├─ API Test → test_auth_positive.py
│   │
│   └─ Call API → AuthAPI.login()
│       │
│       └─ HTTP Layer → APIClient.post()
│           │
│           └─ Base URL → https://dummyjson.com
│               │
│               └─ Endpoint → /auth/login
│                   │
│                   └─ Response → {accessToken, refreshToken, id, username}
│
├─ Validation → Pytest assertions
│   │
│   ├─ Status 200? ✓
│   ├─ Has accessToken? ✓
│   ├─ Has refreshToken? ✓
│   └─ Username matches? ✓
│
└─ Reporting → Allure report + logs/api_test.log
```

---

## 14. FEATURE FLOW - GET USER INFO

```
GET USER INFO FLOW
│
├─ Prerequisites → Valid auth token from login
│
├─ API Test → test_auth.py
│   │
│   └─ Call API → AuthAPI.get_user_info(token)
│       │
│       └─ HTTP Layer → APIClient.get()
│           │
│           ├─ Endpoint → /auth/me
│           ├─ Header → Authorization: Bearer {token}
│           │
│           └─ Response → {id, username}
│
├─ Validation → Pytest assertions
│   │
│   ├─ Status 200? ✓
│   ├─ Username is string? ✓
│   └─ ID > 0? ✓
│
└─ Reporting → Allure report + logs
```

---

## 15. COMMANDS CHEAT SHEET

### **Setup & Installation**
```powershell
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

---

### **Running Tests**
```powershell
# Run all tests
pytest

# Run all tests (verbose)
pytest -v

# Run specific file
pytest test\test_auth_positive.py -v

# Run specific test
pytest test\test_auth_positive.py::test_login_success -v

# Run with Allure reporting
pytest --alluredir=allure-results
```

---

### **Viewing Results**
```powershell
# View test logs
Get-Content logs\api_test.log

# View Allure report (after running tests)
allure serve allure-results

# View test files
Get-ChildItem test\

# View API files
Get-ChildItem api\
```

---

### **Configuration**
```powershell
# View environment variables
Get-Content .env

# View pytest settings
Get-Content pytest.ini

# View dependencies
Get-Content requirements.txt
```

---

## 16. DIRECTORY STRUCTURE VISUALIZATION

### **Command to see full tree:**
```powershell
# Windows built-in tree command
tree /F
```

**Output:**
```
Playwright_API_Framework/
│
├── api/
│   ├── api_client.py
│   ├── auth_api.py
│   └── __pycache__/
│
├── test/
│   ├── test_auth.py
│   ├── test_auth_positive.py
│   ├── test_auth_negative.py
│   ├── test_smoke.py
│   └── __pycache__/
│
├── utils/
│   ├── config.py
│   ├── logger.py
│   └── __pycache__/
│
├── payloads/
│   └── login_payload.json
│
├── logs/
│   └── api_test.log
│
├── allure-results/
│   └── [test reports]
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env
└── README.md
```

---

## 17. TEST EXECUTION EXAMPLE

### **Run and See Output:**

```powershell
# Navigate to project
cd f:\Playwright_API_Framework

# Run login tests
pytest test\test_auth_positive.py -v -s
```

**Expected Output:**
```
test\test_auth_positive.py::test_login_success PASSED

GET CURRENT USER RESPONSE
==================================================

Status Code   : 200
Username      : emilys
User ID       : 70
Access Token  : eyJhbGciOi...
Refresh Token : eyJhbGciOi...

==================================================
```

---

## 18. NEXT STEPS FOR YOU

### **For QA - START HERE:**
```powershell
# Step 1: Understand project structure
tree /F

# Step 2: See test files
Get-ChildItem test\

# Step 3: Run all tests
pytest -v

# Step 4: View logs
Get-Content logs\api_test.log

# Step 5: View Allure report
allure serve allure-results
```

---

### **For Developer - START HERE:**
```powershell
# Step 1: Understand current code
Get-Content api\api_client.py
Get-Content api\auth_api.py

# Step 2: Understand tests
Get-Content test\test_auth_positive.py

# Step 3: Understand fixtures
Get-Content conftest.py

# Step 4: Run tests to verify setup
pytest test\test_auth_positive.py -v
```

---

## 19. SUMMARY TABLE - "WHAT SHOULD I READ?"

| Role | Read First | Then | Then |
|------|-----------|------|------|
| **QA** | `test/test_auth_positive.py` | `payloads/login_payload.json` | `logs/api_test.log` |
| **Developer** | `api/api_client.py` | `api/auth_api.py` | `conftest.py` |
| **DevOps** | `.env` | `pytest.ini` | `requirements.txt` |
| **Manager** | This README | Run: `pytest -v` | View report |

---

## 20. IMPORTANT FILES AT A GLANCE

| File | Lines | Purpose |
|------|-------|---------|
| `api/api_client.py` | ~60 | HTTP client (GET/POST/PUT/DELETE) |
| `api/auth_api.py` | ~30 | Login + Get User endpoints |
| `test/test_auth_positive.py` | ~50 | Successful login tests |
| `test/test_auth_negative.py` | ~100 | Failed login scenarios |
| `test/test_auth.py` | ~50 | Get user info tests |
| `conftest.py` | ~20 | Test fixtures |
| `utils/config.py` | ~10 | Environment config |
| `utils/logger.py` | ~30 | Logging setup |

---

## 📝 QUICK START

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run all tests
pytest -v

# 3. View logs
Get-Content logs\api_test.log

# 4. Generate Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

---

**This is your complete project map & command guide. Start with: `pytest -v` to run all tests!** 🚀
