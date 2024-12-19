pipeline {
    agent any

    environment {
        REGISTRY = 'docker.io'       // e.g., Docker Hub or ECR
        IMAGE_NAME = 'flask-app'
        KUBE_CONTEXT = 'minikube'     // Kubernetes context for `kubectl`
        HELM_RELEASE = 'flask-app-release'
        HELM_CHART = './helm-chart'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image"
                script {
                    sh 'docker build -t ${REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER} .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker Image to Registry"
                script {
                    sh '''
                    docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
                    docker push ${REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER}
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes using Helm"
                script {
                    sh '''
                    helm upgrade --install ${HELM_RELEASE} ${HELM_CHART} \
                        --set image.repository=${REGISTRY}/${IMAGE_NAME} \
                        --set image.tag=${BUILD_NUMBER} \
                        --kube-context=${KUBE_CONTEXT}
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace"
            cleanWs()
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
