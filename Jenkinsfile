
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -3.10 -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install pytest pandas==2.2.3 evidently==0.7.23'
            }
        }

        stage('Run Application') {
            steps {
                bat '.venv\\Scripts\\python.exe hello.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '.venv\\Scripts\\python.exe monitor.py'
            }
        }
    }
}
