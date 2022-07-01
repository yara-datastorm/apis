pipeline {
    agent any
    environment {
        DOCKER_IMAGE_TAG_NAME = "dss"
        DOCKER_IMAGE_TAG_VERSION = 1.0

        DOCKER_CONTAINER_NAME_TEST = "dss"

        DOCKER_CONTAINER_INTERNAL_PORT = 8080
        DOCKER_CONTAINER_EXTERNAL_PORT = 7997
    }
 

    stages {
            
        stage('Building Image') {
            steps{
                script {
                    sh "docker build -t $DOCKER_IMAGE_TAG_NAME:$DOCKER_IMAGE_TAG_VERSION ."
                }
            }
        }


        stage('Run Unit Test image') {
            steps{
                script {
                    try {
                        sh "docker rm -f $DOCKER_CONTAINER_NAME_TEST"
                        sh "docker run -it -d --name $DOCKER_CONTAINER_NAME_TEST $DOCKER_IMAGE_TAG_NAME:$DOCKER_IMAGE_TAG_VERSION pwd"
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                        sh "docker run -it -d --name $DOCKER_CONTAINER_NAME_TEST $DOCKER_IMAGE_TAG_NAME:$DOCKER_IMAGE_TAG_VERSION pwd"
                    }
                    
                    sh "echo $(pwd)"
                    sh "ls -l $(pwd)"
                    // sh "pytest -v --junitxml='reports/regressor.xml'"
                    // sh "junit /reports/junit/*.xml"
                    
                }



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

