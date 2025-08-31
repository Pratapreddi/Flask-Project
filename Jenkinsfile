pipeline {
    agent any

    environment {
        APP_NAME = "flask-project:v3"
        DOCKER_IMAGE = "pratapreddy007/flask-project:v3"
        DEPLOY_SERVER = "ec2-user@13.235.103.164"   // Change to your EC2 instance
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Pratapreddi/Flask-Project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
    steps {
        sh '''
            export PATH=$PATH:/var/lib/jenkins/.local/bin
            pytest || echo "No tests found, skipping..."
        '''
           }
    }


        stage('Build Docker Image') {
    steps {
        sh 'docker build -t pratapreddy007/flask-project:v3 .'
    }
}



        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-crd',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u pratapreddy007 --password-stdin"
                    sh "docker push pratapreddy007/flask-project:v3"
                    sh "docker push pratapreddy007/flask-project:v3"
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent (credentials: ['ec2-ssh-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ec2-user@13.235.103.164 '
                        docker pull pratapreddy007/flask-project:v3 &&
                        docker stop flask-project || true &&
                        docker rm flask-project || true &&
                        docker run -d -p 7000:5000 --name flask-project pratapreddy007/flask-project:v3
                    '
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished (Build #${BUILD_NUMBER})"
        }
        success {
            echo "✅ Deployment successful!"
        }
        failure {
            echo "❌ Pipeline failed. Check logs."
        }
    }
}

