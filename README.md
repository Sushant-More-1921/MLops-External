# Python Addition Program — MLOps Integration

An end-to-end MLOps pipeline implementing a Python addition program with **FastAPI**, **Pytest**, **Evidently AI (Data Quality & Monitoring)**, and **Jenkins CI/CD**.

---

## 📁 Project Structure

```text
MLops External/
│
├── app/
│   ├── __init__.py
│   └── main.py                     # FastAPI application & addition logic (POST & GET /add)
│
├── monitoring/
│   ├── __init__.py
│   └── evidently_monitor.py        # Evidently report generation script
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py                # Unit & API tests for FastAPI and addition
│   └── test_evidently.py           # Test suite for Evidently report generation
│
├── reports/
│   ├── data_quality_report.html    # Generated Evidently interactive report
│   └── pytest-results.xml          # JUnit test results XML for Jenkins
│
├── addition_cli.py                 # Standalone console program for two numbers addition
├── Jenkinsfile                     # Declarative CI/CD pipeline (Windows & Linux compatible)
├── pytest.ini                      # Pytest discovery and warning filters
├── requirements.txt                # Python project dependencies
└── README.md                       # Comprehensive documentation & setup guide
```

---

## ⚙️ Prerequisites

1. **Python 3.10+** (Tested on Python 3.13)
2. **Java 17 or 21 LTS** (Required to run Jenkins)
3. **Git** installed and configured on your system

---

## 🚀 Setup & Installation

### 1. Clone or Open the Workspace

Open your terminal or PowerShell in the project directory:

```powershell
cd "e:\MLops External"
```

### 2. Create and Activate Virtual Environment

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# (If using CMD)
# .\.venv\Scripts\activate.bat

# (If on Linux / macOS)
# source .venv/bin/activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

*Contents of `requirements.txt`:*
- `fastapi`
- `uvicorn`
- `pytest`
- `httpx`
- `evidently`
- `pandas`

---

## 🛠️ Step-by-Step Execution Guide

### 1. Run the Standalone Addition Program (CLI)

You can run the program either interactively or by passing numbers directly as command-line arguments:

#### Interactive Mode:
```powershell
python addition_cli.py
```
*Prompt:*
```text
Enter first number : 12.5
Enter second number: 27.5
--------------------------------------------------
Addition Result: 12.5 + 27.5 = 40.0
==================================================
```

#### Argument Mode:
```powershell
python addition_cli.py 15 25
```
*Output:*
```text
First number : 15.0
Second number: 25.0
Addition Result: 40.0
```

---

### 2. Run the FastAPI Application

Start the FastAPI web server using Uvicorn:

```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

The server is available at: `http://127.0.0.1:8000`

#### Supported Endpoints:

| Method | Endpoint | Description | Example |
|---|---|---|---|
| `GET` | `/` | Root health check & welcome | `http://127.0.0.1:8000/` |
| `GET` | `/add` | Browser-friendly GET addition | `http://127.0.0.1:8000/add?num1=10&num2=20` |
| `POST` | `/add` | JSON payload addition | `curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d "{\"num1\": 10, \"num2\": 20}"` |
| `GET` | `/docs` | Interactive Swagger API documentation | `http://127.0.0.1:8000/docs` |

#### Testing via Browser or curl:
- **In your browser URL bar**:
  Navigate to: `http://127.0.0.1:8000/add?num1=100&num2=250`
  *Response:*
  ```json
  {
    "num1": 100.0,
    "num2": 250.0,
    "addition": 350.0
  }
  ```
- **In PowerShell / Terminal using curl**:
  ```powershell
  curl.exe -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"num1": 10, "num2": 20}'
  ```

---

### 3. Run Automated Tests with Pytest

Execute all unit, API, and Evidently pipeline tests:

```powershell
pytest -v
```

Generate standard JUnit XML report for Jenkins:

```powershell
pytest -v --junitxml=reports/pytest-results.xml
```

All 7 tests verify:
- Addition of positive, negative, and decimal numbers
- `GET /` welcome message
- `POST /add` JSON API request/response
- `GET /add` query parameter API request/response
- Evidently monitoring pipeline execution and report output

---

### 4. Run Evidently Tool (Data Quality & Monitoring)

Execute the Evidently monitoring script to generate interactive HTML reports:

```powershell
python -m monitoring.evidently_monitor
```

- Report saved to: `reports/data_quality_report.html`
- Open the report in your browser:
  ```powershell
  Start-Process "reports/data_quality_report.html"
  ```
The report shows data summaries, missing value checks, distributions, and data quality metrics for `num1`, `num2`, and `result`.

---

## 🏗️ Jenkins Setup & Pipeline Configuration

### Step 1: Start Jenkins

Since `jenkins.war` is available at `D:\jenkins.war` and Java 21 is installed:

Open a new PowerShell terminal and run:

```powershell
java -jar D:\jenkins.war --httpPort=8080
```

> **Note:** If Jenkins is already running as a Windows service on port `8080`, simply open your browser and go to `http://localhost:8080`.

### Step 2: Unlock and Initial Setup
1. Open [http://localhost:8080](http://localhost:8080) in your web browser.
2. If this is the initial launch, copy the administrator password from the terminal or from:
   `C:\Users\<username>\.jenkins\secrets\initialAdminPassword`
3. Click **"Install suggested plugins"** and create your admin account.

### Step 3: Install Required Plugins
Ensure the following plugins are installed (via **Manage Jenkins** → **Plugins** → **Available Plugins**):
- **Pipeline**
- **JUnit Plugin** (to parse and display `pytest-results.xml`)
- **HTML Publisher Plugin** (optional, to view Evidently HTML reports directly in Jenkins)
- **Git**

### Step 4: Create the Pipeline Job
1. In Jenkins dashboard, click **"New Item"**.
2. Enter item name: `Addition-API-Pipeline`.
3. Select **"Pipeline"** and click **OK**.
4. Scroll to the **Pipeline** section:
   - **Definition**: Choose **"Pipeline script from SCM"** (if pushed to Git repository), OR choose **"Pipeline script"** and paste the contents of `Jenkinsfile`.
   - If using local workspace / SCM, specify the branch (e.g., `*/main`).
5. Click **Save**.

### Step 5: Trigger the Build
1. Click **"Build Now"** on the left menu.
2. Observe the pipeline stages execute:
   - `Checkout`
   - `Install Dependencies`
   - `Run Pytest`
   - `Evidently Monitoring`
   - `Build Completed`
3. Check the **Test Result** trend graph and downloaded HTML artifacts under **Build Artifacts** (`reports/data_quality_report.html`).

---

## 🔍 Errors Resolved

1. **`{"detail": "Method Not Allowed"}` on `/add`**:
   - **Issue**: Navigating to `http://127.0.0.1:8000/add` in a browser sends an HTTP `GET` request, while previously only `POST /add` was configured.
   - **Resolution**: Implemented `@app.get("/add")` supporting query parameters `?num1=X&num2=Y` and descriptive fallbacks, while preserving `@app.post("/add")`.

2. **`ModuleNotFoundError: No module named 'pandas'` / `evidently` in `.venv`**:
   - **Issue**: The virtual environment `.venv` was created with `include-system-site-packages = false`, isolating it from installed system packages.
   - **Resolution**: Updated `pyvenv.cfg` to `include-system-site-packages = true` and added a `system_packages.pth` link.

3. **`pandas.errors.ParserError: Expected 3 fields, saw 4`**:
   - **Issue**: Column header and row field count mismatch between logged API calls and Evidently dataset reads.
   - **Resolution**: Standardized data columns across monitoring and API modules to `num1, num2, result`.

4. **Jenkins Windows Execution (`sh: command not found`)**:
   - **Issue**: Jenkins running natively on Windows fails if standard UNIX shell commands (`sh`) are invoked.
   - **Resolution**: Updated `Jenkinsfile` with cross-platform conditional checks (`isUnix()` using `sh` on Linux and `bat` on Windows).

