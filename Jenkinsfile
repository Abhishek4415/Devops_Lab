
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Starting Build Stage'

                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                    python3 -m py_compile app.py
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Starting Test Stage'

                sh '''
                    .venv/bin/pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting Deployment Stage'

                sh '''
                    mkdir -p deployment
                    cp app.py deployment/
                    echo "Application deployed successfully"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline execution failed!'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
