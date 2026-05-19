pipeline {
    agent any
    environment {
        IMAGE_NAME = 'crud-api'
        CONTAINER_NAME = 'crud-api-container'
        PORT = '5000'
    }
    stages {
        stage('Clone Repository') {
            steps {
                echo '📥 Code clone ho raha hai...'
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                echo '🐳 Docker image build ho rahi hai...'
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }
        stage('Stop Old Container') {
            steps {
                echo '🛑 Purana container band kar raha hoon...'
                sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                '''
            }
        }
        stage('Run New Container') {
            steps {
                echo '🚀 Naya container start ho raha hai...'
                sh '''
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${PORT}:5000 \
                        --restart unless-stopped \
                        ${IMAGE_NAME}:latest
                '''
            }
        }
        stage('Health Check') {
            steps {
                echo '❤️ Health check kar raha hoon...'
                sh 'sleep 3'
                sh 'curl -f http://localhost:${PORT}/health || exit 1'
            }
        }
    }
    post {
        success {
            echo '✅ Pipeline SUCCESS! App deploy ho gayi bhai!'
        }
        failure {
            echo '❌ Pipeline FAILED! Logs check karo.'
        }
    }
}
