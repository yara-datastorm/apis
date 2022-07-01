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
            
        stage('Build') {
            steps{
                script {
                    sh "docker build -t $DOCKER_IMAGE_TAG_NAME:$DOCKER_IMAGE_TAG_VERSION ."
                }
            }
        }


        stage('Run and Unit Test') {
            steps{
                script {
                    try {
                        sh "docker rm -f $DOCKER_CONTAINER_NAME_TEST"
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }
                    
                    sh "docker run -it -d -p $DOCKER_CONTAINER_EXTERNAL_PORT:$DOCKER_CONTAINER_INTERNAL_PORT --name $DOCKER_CONTAINER_NAME_TEST $DOCKER_IMAGE_TAG_NAME:$DOCKER_IMAGE_TAG_VERSION"
                    
                    sh "docker exec $DOCKER_CONTAINER_NAME_TEST pytest --verbose --junit-xml=reports/results.xml tests/ && ls"
                    
                    sh "docker cp $DOCKER_CONTAINER_NAME_TEST:/usr/src/app/reports \$(pwd)"
                    
                    // sh "cd \$(pwd)"
                    // sh "ls -l"

                    junit "reports/*.xml"

                }

            // pytest --verbose --junit-xml=test-reports/results.xml test_api.py


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

