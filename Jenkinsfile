pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from your repository
                git 'https://github.com/your/repository.git'
            }
        }
        
        stage('Build') {
            steps {
                // Set up the virtual environment (assuming you're using venv)
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                
                // Install dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Unit Test') {
            steps {
                // Run unit tests
                sh 'python -m unittest discover -s tests -p "*_test.py"'
            }
        }
    }
    
    post {
        always {
            // Clean up the virtual environment
            sh 'deactivate'
            sh 'rm -rf venv'
        }
    }
}
