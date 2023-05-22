// pipeline {
//
//     agent {
//             docker {
//                 image 'python:3.8.7' // Specify the Python version or any other base image you need
//                 args '-u root' // Run Docker container as root user
//             }
//         }
//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//         stage('Install dependencies') {
//             steps {
//                 // Install required dependencies
//                 sh 'pip install -r requirements.txt'
//             }
//         }
//
//         stage('Run tests') {
//             steps {
//                 // Run your Python unit tests
//                 sh 'python -m unittest discover -s tests'
//             }
//         }
//
//     }
// }
pipeline {
    agent any

    stages {
        stage('Connect to Local Database') {
            steps {
                script {
                    def mysqlHost = 'localhost'
                    def mysqlPort = 3306
                    def mysqlDatabase = 'supply solutions'
                    def mysqlUsername = 'root'
                    def mysqlPassword = 'aalleexx'
                    def jdbcDriver = 'com.mysql.cj.jdbc.Driver'
                    def connectionString = "jdbc:mysql://${mysqlHost}:${mysqlPort}/${mysqlDatabase}?useSSL=false"

                    // Load the JDBC driver
                    Class.forName(jdbcDriver)

                    try {
                        def connection = DriverManager.getConnection(connectionString, mysqlUsername, mysqlPassword)
                        echo "Connected to the local MySQL database successfully!"
                        connection.close()
                    } catch (Exception e) {
                        echo "Failed to connect to the local MySQL database: ${e.message}"
                        error("Database connection failed")
                    }
                }
            }
        }

        // ... Other stages in your pipeline ...
    }
}

