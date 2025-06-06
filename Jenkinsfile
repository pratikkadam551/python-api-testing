pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'
        VENV_NAME = 'venv'
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    python${PYTHON_VERSION} -m venv ${VENV_NAME}
                    . ${VENV_NAME}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV_NAME}/bin/activate
                    pytest tests/ -v --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']]
            ])
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'HTML Test Report'
            ])
        }
        success {
            echo 'Test execution completed successfully!'
        }
        failure {
            echo 'Test execution failed!'
        }
    }
} 