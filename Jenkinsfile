pipeline {
    agent any

    environment {
        IMAGE_NAME = "315510/world_of_games"
        IMAGE_TAG = "latest"
        DUMMY_SCORES = "dummy_scores.txt"
        CONTAINER_NAME = "world_of_games_test"
        VENV_PATH = "${WORKSPACE}/venv"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out repository..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh """
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

     stage('Run Container') {
    steps {
        echo "Running container for testing..."
        sh "echo '0' > ${DUMMY_SCORES}"
        sh """
            docker run -d \
                --name ${CONTAINER_NAME} \
                -p 5000:5000 \
                -v \$(pwd)/${DUMMY_SCORES}:/app/Scores.txt \
                -e TEST_MODE=True \
                ${IMAGE_NAME}:${IMAGE_TAG}

            # Wait for Flask server, retry up to 10 times
            for i in \$(seq 1 10); do
                if curl -s http://127.0.0.1:5000 > /dev/null; then
                    echo "Server is up!"
                    break
                else
                    echo "Waiting for server... Attempt \$i/10"
                    sleep 3
                fi
                if [ \$i -eq 10 ]; then
                    echo "Server did not start after 10 attempts."
                    exit 1
                fi
            done
        """
    }
}



        stage('Setup Python venv') {
            steps {
                echo "Creating Python virtual environment and installing dependencies..."
                sh """
                    python3 -m venv ${VENV_PATH}
                    ${VENV_PATH}/bin/pip install --upgrade pip
                    ${VENV_PATH}/bin/pip install -r requirements.txt
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo "Running Selenium e2e tests..."
                sh """
                    ${VENV_PATH}/bin/python tests/e2e.py
                """
            }
        }

        stage('Finalize') {
            steps {
                echo "Stopping test container..."
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"

                echo "Pushing Docker image..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub_creds',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
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
