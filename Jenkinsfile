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
                    def mysqlDatabase = 'your_database_name'
                    def mysqlUsername = 'your_username'
                    def mysqlPassword = 'your_password'

                    try {
                        def sql = new groovy.sql.Sql(
                            groovy.sql.Sql.newInstance(
                                "jdbc:mysql://${mysqlHost}:${mysqlPort}/${mysqlDatabase}",
                                mysqlUsername,
                                mysqlPassword,
                                'com.mysql.cj.jdbc.Driver'
                            )
                        )
                        echo "Connected to the local MySQL database successfully!"
                        sql.close()
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
