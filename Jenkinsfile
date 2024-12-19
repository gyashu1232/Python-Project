pipeline {
    agent any
    environment {
        IMAGE_NAME = "flask-todo-app"
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}")
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run("-d --name flask-app -p 5000:5000")
                }
            }
        }
        stage('Clean Up') {
            steps {
                script {
                    dockerImage.stop()
                    sh 'docker rm flask-app || true'
                }
            }
        }
    }
    post {
        always {
            sh 'docker rmi ${IMAGE_NAME} || true'
        }
    }
}
