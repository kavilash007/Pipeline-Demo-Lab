pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'nginx-reverse-proxy'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code repository
                git branch: 'main', url: 'https://github.com/kavilash007/Pipeline-Demo-Lab.git'
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    // Build the Docker images
                    sh 'docker compose build'
                }
            }
        }
        stage('Push Docker Images to Docker Hub') {
            steps {
                script {
                    // Use Jenkins credentials to login to Docker Hub securely
                    withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_TOKEN')]) {
                        sh "docker login -u kavilash -p ${DOCKER_TOKEN}"
                    }
                    sh 'docker compose push'
                }
            }
        }
        stage('Deploy Docker Containers') {
            steps {
                script {
                    // Start the containers using Docker Compose
                    sh 'docker compose up -d'
                }
            }
        }
    }
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
