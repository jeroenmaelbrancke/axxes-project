pipeline {
    agent { 
        docker { 
            image 'python:latest'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'sudo pip install -r requirements.txt'
            }
        }

        stage('unit tests'){
            steps {
                sh 'python -m unittest test_volume_cuboid.py'
            }
        }
    }
}
