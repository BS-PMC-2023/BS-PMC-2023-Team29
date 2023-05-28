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
//
//
// pipeline {
//     agent {
//         docker {
//             image 'python:3.8.7'
//             args '-u root'
//         }
//     }
//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//         stage('Install dependencies') {
//             steps {
//                 sh 'pip install -r requirements.txt'
//             }
//         }
//         stage('Run tests') {
//             steps {
//                 sh 'python -m unittest discover -s tests'
//             }
//         }
//         stage('Post Actions') {
//             steps {
//                 script {
//                     try {
//                         // Perform post-action steps
//                     } catch (Exception e) {
//                         // Handle the exception or send notifications
//                         echo "Post-action failed: ${e.getMessage()}"
//                         // Send email notification, Slack message, etc.
//                         // You can use the Jenkins email or Slack plugins for this purpose
//                     }
//                 }
//             }
//         }
//     }
// }
//
pipeline {
    agent {
        docker {
            image 'python:3.8.7'
            args '-u root'
        }
    }

    stages {
        stage('Connect to Database') {
            steps {
                script {
                    def mysqlHost = 'localhost'
                    def mysqlPort = 3306
                    def mysqlDatabase = 'supply solutions'
                    def mysqlUser = 'root'
                    def mysqlPassword = 'aalleexx'

                    try {
                        // Import necessary libraries
                        @GrabConfig(systemClassLoader = true)
                        @Grab('mysql:mysql-connector-java:8.0.26')
                        import com.mysql.jdbc.Driver

                        // Connect to the MySQL database
                        def connection = null
                        try {
                            def connectionString = "jdbc:mysql://${mysqlHost}:${mysqlPort}/${mysqlDatabase}"
                            connection = DriverManager.getConnection(connectionString, mysqlUser, mysqlPassword)

                            echo "Connected to the MySQL database successfully!"
                            // Perform additional operations if needed
                        } finally {
                            if (connection != null) {
                                connection.close()
                            }
                        }
                    } catch (Exception e) {
                        error "Failed to connect to the MySQL database: ${e.message}"
                    }
                }
            }
        }
    }
}
