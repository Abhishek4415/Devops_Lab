
pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {

        stage('Build') {
            steps {
                echo 'Building Application'

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
                echo 'Testing Application'

                bat '''
                    .venv\\Scripts\\python.exe -m pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Application'

                bat '''
                    if not exist deployment mkdir deployment

                    copy /Y app.py deployment\\app.py

                    echo Deployment successful
                '''
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'

            archiveArtifacts artifacts: 'deployment/**',
                             allowEmptyArchive: false
        }

        failure {
            echo 'Build or deployment failed!'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
