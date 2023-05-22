pipeline {

    agent {
            docker {
                image 'python:3.8.7' // Specify the Python version or any other base image you need
                args '-u root' // Run Docker container as root user
            }
        }
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
                sh 'python -m unittest discover -s tests'
            }
        }

    }
}
