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
        IMAGE_TAG_VERSION = 1.0
        IMAGE_VULNERABILITY = "medium"

        CTN_NAME_TEST = "dss"

        CTN_INTERNAL_PORT = 8080
        CTN_EXTERNAL_PORT = 7997
    }
 

    stages {

        stage('Build') {
            steps{
                echo "Holla"
            }
        }
            
        // stage('Build') {
        //     steps{
        //         script {
        //             sh "docker build -t $IMAGE_TAG_NAME:$IMAGE_TAG_VERSION ."
        //         }
        //     }
        // }


        // stage('Run and Unit Test') {
        //     steps{
        //         script {
        //             try {
        //                 sh "docker rm -f $CTN_NAME_TEST"
        //             } catch (Exception e) {
        //                 echo 'Exception occurred: ' + e.toString()
        //             }
                    
        //             sh "docker run -it -d -p $CTN_EXTERNAL_PORT:$CTN_INTERNAL_PORT --name $CTN_NAME_TEST $IMAGE_TAG_NAME:$IMAGE_TAG_VERSION"
                    
        //             sh "docker exec $CTN_NAME_TEST pytest --verbose --junit-xml=reports/results.xml tests/ && ls"
                    
        //             sh "docker cp $CTN_NAME_TEST:/usr/src/app/reports \$(pwd)"
                    
        //             junit "reports/*.xml"
        //         }

        //         // pytest --verbose --junit-xml=test-reports/results.xml test_api.py
        //     }
        // }


        stage('analyzeee') {
            steps {
                script {
                    // Scan all library vuln levels      
                    sh "ls -la"
                    sh 'mkdir \$(pwd)/vuln-scan'
                    sh 'ls -la'
                    sh 'docker run --rm -v "//var/run/docker.sock:/var/run/docker.sock" --mount type=bind,source="\$(pwd)"/vuln-scan,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-ci-report-library.html --ignore-unfixed --exit-code 1 --vuln-type library python:3.10-slim'
                
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

        

        // stage('analyze') {
        //     steps {
        //         // Scan all library vuln  levels        
        //         docker run --rm -v '//var/run/docker.sock:/var/run/docker.sock' --mount type=bind,source="$(pwd)"/root,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-dc-report-library.html --ignore-unfixed --exit-code 1 --vuln-type library python:3.10-slim
        //         // Scan all os vuln  levels 
        //         docker run --rm -v '//var/run/docker.sock:/var/run/docker.sock' --mount type=bind,source="$(pwd)"/root,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-dc-report-os.html --ignore-unfixed --exit-code 1 --vuln-type os python:3.10-slim
            
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

