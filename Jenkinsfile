pipeline {
    agent any

    // agent {
    //     docker {
    //         image: 'trivy:latest'
    //         args '--group-add docker'
    //         reuseNode true
    //     }
    // }

    environment {
        IMAGE_TAG_NAME = "dss"
        IMAGE_TAG_VERSION = $BUILD_NUMBER
        IMAGE_VULNERABILITY = "medium"

        CTN_NAME_TEST = "dss"

        CTN_INTERNAL_PORT = 8080
        CTN_EXTERNAL_PORT = 7997
    }
 

    stages {
            
        stage('Build') {
            steps{
                script {
                    sh "docker build -t $IMAGE_TAG_NAME:$IMAGE_TAG_VERSION ."
                }
            }
        }


        stage('Run and Unit Test') {
            steps{
                script {
                    try {
                        sh "docker rm -f $CTN_NAME_TEST"
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }
                    
                    sh "docker run -it -d -p $CTN_EXTERNAL_PORT:$CTN_INTERNAL_PORT --name $CTN_NAME_TEST $IMAGE_TAG_NAME:$IMAGE_TAG_VERSION"
                    
                    sh "docker exec $CTN_NAME_TEST pytest --verbose --junit-xml=reports/results.xml tests/ && ls"
                    
                    sh "docker cp $CTN_NAME_TEST:/usr/src/app/reports \$(pwd)"
                    
                    junit "reports/*.xml"
                }
            }
        }


        stage('Analyze') {
            steps {
                script {
                    // Scan all library vuln levels
                    try {
                        sh 'mkdir \$(pwd)/vuln-scan'
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }
                    sh 'docker run --rm -v "//var/run/docker.sock:/var/run/docker.sock" --mount type=bind,source="\$(pwd)"/vuln-scan,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-ci-report-os-library.html --ignore-unfixed --exit-code 0 --vuln-type os,library  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$IMAGE_TAG_VERSION'
                
                }
            }
        }


        stage('Build image') {
            steps {
                echo 'Starting to build docker image'

                script {
                    // my-image:${env.BUILD_ID}
                    docker.withRegistry('', 'dockerHub-access' ) {
                        def customImage = docker.build("70077007/dss:1.1")
                        customImage.push()
                     }
                }
            }
        }
        
            

        // stage(‘Deploy Image’) {
        //     steps{
        //         script {
        //             docker.withRegistry('', registryCredential ) {
        //                 dockerImage.push()
        //             }
        //         }
        //     }
        // }

        

        // stage('analyze cd') {
        //     steps {
        //         // Scan all library vuln  levels        
        //         docker run --rm -v '//var/run/docker.sock:/var/run/docker.sock' --mount type=bind,source="$(pwd)"/root,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-dc-report-library.html --ignore-unfixed --exit-code 0 --vuln-type library  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$IMAGE_TAG_VERSION
        //         // Scan all os vuln  levels 
        //         docker run --rm -v '//var/run/docker.sock:/var/run/docker.sock' --mount type=bind,source="$(pwd)"/root,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-dc-report-os.html --ignore-unfixed --exit-code 0 --vuln-type os  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$IMAGE_TAG_VERSION
            
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

