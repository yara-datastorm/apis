pipeline {
    agent any 


    environment {
        IMAGE_TAG_NAME = "dss"
        // BUILD_NUMBER = $BUILD_NUMBER
        IMAGE_VULNERABILITY = "medium"

        // IMAGE_TAG_NAME = "dss"

        CTN_INTERNAL_PORT = 8080
        CTN_EXTERNAL_PORT = 7997
    }


    stages {
            
        stage('Build') {
            steps{
                script {
                    sh "docker build -t $IMAGE_TAG_NAME:$BUILD_NUMBER ."
                }
            }
        }


        stage('Run and Unit Test') {
            steps{
                script {
                    try {
                        sh "docker rm -f $IMAGE_TAG_NAME"
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }
                    
                    sh "docker run -it -d -p $CTN_EXTERNAL_PORT:$CTN_INTERNAL_PORT --name $IMAGE_TAG_NAME $IMAGE_TAG_NAME:$BUILD_NUMBER"
                    
                    sh "docker exec $IMAGE_TAG_NAME pytest --verbose --junit-xml=reports/results.xml tests/ && ls"
                    
                    sh "docker cp $IMAGE_TAG_NAME:/usr/src/app/reports \$(pwd)"
                    
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
                    sh 'docker run --rm -v "//var/run/docker.sock:/var/run/docker.sock" --mount type=bind,source="\$(pwd)"/vuln-scan,target=/home aquasec/trivy:0.18.3 image --cache-dir \$(pwd)/vuln-scan/ --format template --template @contrib/html.tpl -o ./home/trivy-ci-report-os-library$BUILD_NUMBER.html --ignore-unfixed --exit-code 0 --vuln-type os,library  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$BUILD_NUMBER'
                
                }
            }
        }


        stage('Build image') {
            steps {
                echo 'Starting to build docker image'

                script {
                    // my-image:${env.BUILD_ID}
                    sh 'echo "70077007/$IMAGE_TAG_NAME:$BUILD_NUMBER"'
                    docker.withRegistry('', 'dockerHub-access' ) {
                        def customImage = docker.build("70077007/$IMAGE_TAG_NAME:$BUILD_NUMBER")
                        customImage.push()
                     }
                }
            }
        }
        
            
        // stage('Verify') {
        //     steps{
        //         script {
        //             docker.withRegistry('', registryCredential ) {
        //                 dockerImage.push()
        //             }
        //         }
        //     }
        // }
            

        stage('Deploy') {
            steps{
                script {
                    sh 'my_image=${IMAGE_TAG_NAME}:${BUILD_NUMBER} envsubst < k8s/deploy.yml.tmpl > k8s/mydeploy.yaml'
                    sh 'kubectl apply -f k8s/ --recursive'
                }
            }
        }

        

        // stage('analyze code') {
        //     steps {
        //         // Scan all library vuln  levels        
        //         docker run --rm -v '//var/run/docker.sock:/var/run/docker.sock' --mount type=bind,source="$(pwd)"/root,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-dc-report-library.html --ignore-unfixed --exit-code 0 --vuln-type library  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$BUILD_NUMBER
        //         // Scan all os vuln  levels 
        //         docker run --rm -v '//var/run/docker.sock:/var/run/docker.sock' --mount type=bind,source="$(pwd)"/root,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-dc-report-os.html --ignore-unfixed --exit-code 0 --vuln-type os  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$BUILD_NUMBER
            
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

