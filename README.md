# 🎯 Tutorial Ninja Playwright Project

[![Build Status](https://img.shields.io/github/actions/workflow/status/Fulcrum-S/Tutorial-ninja-playwright-project/playwright.yml?style=for-the-badge)](https://github.com/Fulcrum-S/Tutorial-ninja-playwright-project/actions)
[![Test Coverage](https://img.shields.io/badge/Test-Coverage-success?style=for-the-badge)](#test-coverage)
[![Allure Report](https://img.shields.io/badge/Allure-Report-blueviolet?style=for-the-badge)](http://127.0.0.1:50122/)

🚀 A professional Playwright for Python test automation framework for the Tutorial Ninja demo application, built with scalability, clarity, and CI integration in mind.

## 📖 Overview

This project is a comprehensive end-to-end UI test automation framework built using Playwright for Python.  
It demonstrates modern QA automation best practices including Page Object Model (POM) design, Pytest-based execution, centralized INI configuration, CI pipelines, and rich Allure reporting.  
The framework is designed to be maintainable, scalable, and suitable for real-world automation scenarios.

## 🎯 Project Goals

- Deliver a clean and maintainable Playwright automation framework  
- Demonstrate professional QA automation standards  
- Validate critical user journeys of the Tutorial Ninja application  
- Provide clear test reporting and visibility  
- Serve as a portfolio-quality automation project  

## 🧰 Technologies Used

- 🐍 Python 3.14  
- 🎭 Playwright for Python  
- 🧪 Pytest  
- 📊 Allure Reports  
- ⚙️ INI-based configuration  
- 🤖 GitHub Actions (CI/CD)  

## ✨ Key Features

- Page Object Model (POM) architecture  
- Pytest-driven test execution  
- Centralized configuration using .ini files  
- Allure HTML reporting for detailed insights  
- Continuous Integration with GitHub Actions  
- Clean, readable, and scalable codebase  

## 🛠 Prerequisites

- Python 3.14 or higher  
- pip  
- Git  

## 📥 Installation

1. Clone the repository  
   git clone https://github.com/Fulcrum-S/playwright-project.git

2. Navigate to the project directory  
   cd playwright-project

3. Install dependencies  
   pip install -r requirements.txt

4. Install Playwright browsers  
   playwright install

## 📊 Allure Test Reports

1. Run tests and collect Allure results:  
pytest --alluredir=allure-results

2. Generate the Allure report:  
allure generate allure-results -o allure-report --clean

Allure Report URL: https://fulcrum-s.github.io/playwright-project/



## 📈 Test Coverage

This project supports test coverage tracking to ensure that key application flows are properly validated.  
Coverage analysis helps identify gaps and improve overall test quality.  
(Test coverage can be enabled using tools such as pytest-cov.)

## 📂 Project Structure

📦 playwright-project  
 ┣ 📂 Pages               → Page object clasess   
 ┣ 📂 Tests               → Test specifications  
 ┣ 📜 config.ini          → Environment & application configuration  
 ┣ 📜 pytest.ini          → Pytest configuration  
 ┣ 📜 requirements.txt   → Python dependencies  
   

## 🔄 Continuous Integration

This project uses GitHub Actions to automatically run Playwright tests on push and pull requests, ensuring code quality and test stability.

CI configuration location:  
.github/workflows/playwright.yml

## 👤 Author

Roma Asailov  
LinkedIn: https://www.linkedin.com/in/roma-asailov-a8b49b29a/

## 📜 License

License not specified

⭐ If you find this project useful, feel free to give it a star and connect on LinkedIn.  
Happy testing with Playwright 🎭
