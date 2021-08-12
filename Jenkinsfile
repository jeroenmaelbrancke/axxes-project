pipeline {
    environment {
        MY_NAME = 'Jeroen'
    }

    agent { 
        docker { 
            image "python:latest"
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                echo "Hello, my name is ${MY_NAME}"
            }
        }
    }
    post {
        always {
            echo 'This will always run'
            echo "Hello, my name is ${MY_NAME}"
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
