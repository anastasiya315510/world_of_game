pipeline {
    agent any

    environment {
        IMAGE_NAME = "315510/world_of_games"
        IMAGE_TAG = "latest"
        DUMMY_SCORES = "dummy_scores.txt"
        CONTAINER_NAME = "world_of_games_test"
        FLASK_PORT = "5001"   // 🔹 Flask server port inside the container
        HOST_PORT = "8777"    // 🔹 external port for Jenkins access
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out repository..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building Docker image..."
                sh """
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Run') {
            steps {
                echo "Running container for testing..."
                sh "echo '0' > ${DUMMY_SCORES}"

                sh """
                    docker run -d \
                    --name ${CONTAINER_NAME} \
                    -p ${HOST_PORT}:${FLASK_PORT} \
                    -v \$(pwd)/${DUMMY_SCORES}:/app/Scores.txt \
                    -e TEST_MODE=True \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                """
                sleep 5
            }
        }

        stage('Setup Python venv') {
            steps {
                echo "Creating Python virtual environment..."
                sh """
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                echo "Running Selenium e2e tests..."
                sh """
                    . venv/bin/activate
                    python tests/e2e.py
                """
            }
        }


        stage('Finalize') {
            steps {
                echo "Stopping and cleaning up container..."
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"

                echo "Pushing image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub_creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS')]) {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

		stage('Deploy Helm Chart') {
            steps {
                sh '''
                export DB_USER=${DB_USER}
                export DB_PASSWORD=${DB_PASSWORD}
                helm upgrade --install world-of-games ./helm/scores \
                    --set mysql.user=$DB_USER \
                    --set mysql.password=$DB_PASSWORD \
                    --set mysql.database=$DB_NAME \
                    --set mysql.host=$DB_HOST
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods'
                sh 'kubectl get svc'
            }
        }
    }



    post {
        always {
            echo "Cleaning up any remaining containers..."
            sh "docker rm -f ${CONTAINER_NAME} || true"
        }
    }
}
