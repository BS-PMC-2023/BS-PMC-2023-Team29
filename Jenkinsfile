pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                // Install required dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                // Run your Python unit tests
                sh 'python -m unittest discover'
            }
        }

    }
}
