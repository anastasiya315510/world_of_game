pipeline {
    agent any

    environment {
        IMAGE_NAME = "315510/world_of_games"
        IMAGE_TAG = "latest"
        DUMMY_SCORES = "dummy_scores.txt"
        CONTAINER_NAME = "world_of_games_test"
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
                // Create dummy Scores.txt if it doesn't exist
                sh "echo '0' > ${DUMMY_SCORES}"

                sh """
                    docker run -d \
                    --name ${CONTAINER_NAME} \
                    -p 8777:5000 \
                    -v \$(pwd)/${DUMMY_SCORES}:/app/Scores.txt \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                """
                // Wait a few seconds for Flask server to start
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
            pip install selenium
        """
    }
}

       stage('Test') {
    steps {
        echo "Running Selenium e2e tests in venv..."
        sh """
            . venv/bin/activate
            python tests/e2e.py
        """
    }
}

        stage('Finalize') {
            steps {
                echo "Stopping test container..."
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
    }

    post {
        always {
            echo "Cleaning up any remaining containers..."
            sh "docker rm -f ${CONTAINER_NAME} || true"
        }
    }
}
