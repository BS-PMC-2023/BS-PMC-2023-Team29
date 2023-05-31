pipeline {
    agent {
        docker {
            image 'python:3.8.7'
            args '-u root'
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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
        stage('Metrics 1 - Coverage') {
            steps {
                sh 'docker run --rm creativestorage coverage run manage.py test'
                //sh 'docker run --rm creativestorage coverage report'


            }
        }


        stage('Metrics 2 - Radon') {
            steps {
                sh 'docker run --rm creativestorage radon cc --show-complexity --total-average main/tests.py'
            }
        }

        stage('Metrics 3 - Bandit') {
            steps {
                sh 'docker run --rm creativestorage bandit -r manage.py test'
            }
        }

        stage('Metrics 4 - Pylint') {
            steps {
                sh 'docker run --rm creativestorage pylint main/tests.py'
            }
        }
        stage('Post Actions') {
            steps {
                script {
                    try {
                        // Perform post-action steps
                    } catch (Exception e) {
                        // Handle the exception or send notifications
                        echo "Post-action failed: ${e.getMessage()}"
                        // Send email notification, Slack message, etc.
                        // You can use the Jenkins email or Slack plugins for this purpose
                    }
                }
            }
        }
    }
}

