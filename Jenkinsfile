
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing application...'
                sh 'python3 app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'mkdir -p deployment'
                sh 'cp app.py deployment/'
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
