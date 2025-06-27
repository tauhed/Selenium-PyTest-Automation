# Selenium PyTest Automation Framework 🚗

A robust web automation framework built with **Selenium**, **PyTest**, and **Allure Report**, following the **Page Object Model** design pattern.

## 🔧 Features
- Page Object Model (POM)
- Cross-browser support (Chrome, Firefox)
- Pytest integration with Allure and HTML reporting
- CI integration with GitHub Actions
- Modular folder structure for scalability

## 📂 Project Structure
```
project_root/
├── pages/             # Page classes
├── tests/             # Test cases
├── data/              # Test data
├── utils/             # Helpers and utilities
├── conftest.py        # Global fixtures
├── run_tests.py       # Script to run tests
├── pytest.ini         # Pytest configuration
├── requirements.txt   # Dependencies
├── .github/workflows/ # CI configuration
└── README.md
```

## 🚀 How to Run Tests

### 📦 Install Requirements
```bash
pip install -r requirements.txt
```

### ▶ Run Tests with Allure + HTML Report
```bash
python run_tests.py
```

### 🧪 Run Tests Manually
```bash
pytest --browser chrome --alluredir=allure-results --html=reports/report.html --self-contained-html
```

## 📊 View Allure Report
```bash
allure serve allure-results
```

## ⚙️ GitHub Actions CI
This framework includes a GitHub Actions workflow that runs tests automatically on every push and pull request to the `main` branch.

## 🧑‍💻 Author
**M. Tauhedul Amin Mazumder**  
QA Manager | SQA Trainer | Automation Enthusiast  
[GitHub: Tauhed](https://github.com/Tauhed)