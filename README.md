# W3-Assignment-Selenium

## Overview
W3-Assignment-Selenium is a project designed to run Selenium test cases efficiently. This guide will help you set up the environment and execute the tests seamlessly.

## Prerequisites
- Python 3.x installed on your system.
- Git installed for cloning the repository.
- Basic knowledge of Python virtual environments.

---

## Setup Instructions

### Step 1: Clone the Repository
Clone the project using the following command:
```bash
git clone https://github.com/Chy-Zaber-Bin-Zahid/W3-Assignment-Selenium.git
```

### Step 2: Navigate to the Project Directory
Change the directory to the project folder:
```bash
cd W3-Assignment-Selenium
```

### Step 3: Create a Virtual Environment
Set up a virtual environment to manage dependencies:
```bash
python3 -m venv env
```

### Step 4: Activate the Virtual Environment
Activate the virtual environment:
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```
- On Windows:
  ```bash
  env\Scripts\activate
  ```

### Step 5: Install Dependencies
Install the required packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## Running the Test Cases
To execute the Selenium test cases, run the following command:
```bash
python main.py
```

---

## Test Reports
The results of the test cases are stored in an Excel report located at:
`/reports/test_report.xlsx`.
This file provides a detailed summary of the test execution.

---

## Notes
- Ensure all necessary drivers (e.g., ChromeDriver) are installed and available in your system's PATH.
- Keep the `requirements.txt` file updated with all dependencies.