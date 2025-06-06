# API Testing Project with Pytest

This project demonstrates comprehensive API testing using Python, Pytest framework, and integrates with Jenkins for continuous integration.

## Project Structure
```
api-testing/
├── tests/
│   ├── test_get_requests.py
│   ├── test_post_requests.py
│   ├── test_put_requests.py
│   ├── test_delete_requests.py
│   └── conftest.py
├── reports/
├── allure-results/
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests with Allure reporting:
```bash
# Run tests and generate Allure results
pytest tests/ -v --alluredir=allure-results

# Generate and open Allure report
allure serve allure-results
```

4. Run tests with HTML reporting:
```bash
pytest tests/ -v --html=reports/report.html
```

## Test Scenarios

The project includes test cases for:
- GET requests (15 scenarios)
- POST requests (15 scenarios)
- PUT requests (15 scenarios)
- DELETE requests (15 scenarios)

## Jenkins Integration

The project includes a Jenkinsfile for CI/CD pipeline integration. The pipeline:
1. Sets up Python environment
2. Installs dependencies
3. Runs tests
4. Generates and publishes Allure and HTML reports

## Test Reports

The project generates two types of reports:

### Allure Reports
- Interactive and detailed test reports
- Test execution timeline
- Test categories and severity
- Environment information
- Test attachments and logs
- To view locally: `allure serve allure-results`

### HTML Reports
- Basic test execution summary
- Pass/Fail statistics
- Execution time
- Stored in the `reports` directory

## API Endpoints Used

The project uses the following free dummy APIs:
- JSONPlaceholder (https://jsonplaceholder.typicode.com)
- ReqRes (https://reqres.in)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 
