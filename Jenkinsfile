pipeline {
    agent any
    environment {
        DOCKER_IMAGE_TAG_NAME = "datastorm"
        DOCKER_IMAGE_TAG_VERSION = 1.0

        DOCKER_CONTAINER_INTERNAL_PORT = 8080
        DOCKER_CONTAINER_EXTERNAL_PORT = 7997
    }
    def app 
    
    stages {
            
        stage('Build Docker Image') {
            steps {
                // sh 'ls -l'
                // sh 'pwd'
                // // echo '${env.DOCKER_IMAGE_TAG_NAME}:${env.DOCKER_IMAGE_TAG_VERSION}'
                // sh 'docker build -t $env.DOCKER_IMAGE_TAG_NAME:$env.DOCKER_IMAGE_TAG_VERSION .'

                app = docker.build("yara/ds")
                

            }
        }

        // stage('Run Docker Container') {
        //     steps {
        //         echo 'docker run --name ds -d -p ${env.DOCKER_CONTAINER_EXTERNAL_PORT}:${env.DOCKER_CONTAINER_INTERNAL_PORT} ${env.DOCKER_IMAGE_TAG_NAME}:${env.DOCKER_IMAGE_TAG_VERSION}'
        //         sh 'docker run --name ds -d -p ${env.DOCKER_CONTAINER_EXTERNAL_PORT}:${env.DOCKER_CONTAINER_INTERNAL_PORT} ${env.DOCKER_IMAGE_TAG_NAME}:${env.DOCKER_IMAGE_TAG_VERSION}'
        //     }
        // }
            
        // stage('Build') {
        //     // parallel {
        //     //     stage('Build Docker Image') {
        //     //         steps {
        //     //             sh 'ls -l'
        //     //             sh 'pwd'
        //     //             // echo '${env.DOCKER_IMAGE_TAG_NAME}:${env.DOCKER_IMAGE_TAG_VERSION}'
        //     //             sh 'docker build -t $env.DOCKER_IMAGE_TAG_NAME:$env.DOCKER_IMAGE_TAG_VERSION .'
        //     //         }
        //     //     }
        //     //     stage('Run Docker Container') {
        //     //         steps {
        //     //             echo 'docker run --name ds -d -p ${env.DOCKER_CONTAINER_EXTERNAL_PORT}:${env.DOCKER_CONTAINER_INTERNAL_PORT} ${env.DOCKER_IMAGE_TAG_NAME}:${env.DOCKER_IMAGE_TAG_VERSION}'
        //     //             sh 'docker run --name ds -d -p ${env.DOCKER_CONTAINER_EXTERNAL_PORT}:${env.DOCKER_CONTAINER_INTERNAL_PORT} ${env.DOCKER_IMAGE_TAG_NAME}:${env.DOCKER_IMAGE_TAG_VERSION}'
        //     //         }
        //     //     }
        //     // }
        // }

        stage('Test image') {
            app.inside {
                sh 'echo "Tests passed"'
            }
        }

        // stage('Deploy') {
        //     steps {
        //         echo "deploying the application"
        //         sh "sudo nohup python3 app.py > log.txt 2>&1 &"
        //     }
        // }

    }

    // post {
	// 	always {
	// 		echo 'The pipeline completed'
	// 		junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
	// 	}
	// 	success {				
	// 		echo "Flask Application Up and running!!"
	// 	}
	// 	failure {
	// 		echo 'Build stage failed'
	// 		error('Stopping early…')
	// 	}
	// }   
}

