
pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {

        stage('Build') {
            steps {
                echo 'Starting Build Stage'

                bat '''
                    echo Checking Python version

                    "C:\\Users\\Abhishek\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" --version

                    echo Creating virtual environment

                    "C:\\Users\\Abhishek\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv .venv

                    echo Installing dependencies

                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt

                    echo Checking application syntax

                    .venv\\Scripts\\python.exe -m py_compile app.py
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Starting Test Stage'

                bat '''
                    .venv\\Scripts\\python.exe -m pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting Deployment Stage'

                bat '''
                    if not exist deployment mkdir deployment

                    copy app.py deployment\\app.py

                    echo Application deployed successfully
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'

            archiveArtifacts artifacts: 'deployment/**',
                             allowEmptyArchive: false
        }

        failure {
            echo 'Pipeline execution failed!'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
