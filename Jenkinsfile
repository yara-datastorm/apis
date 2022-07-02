pipeline {
    agent any

    agent {
        docker {
            image: 'trivy:latest'
            args '--group-add docker'
            reuseNode true
        }
    }

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
        
        // // stage('Evaluate') {
        // //     steps{
        // //         script{
        // //             sh 'docker scan --severity $IMAGE_VULNERABILITY dss:1.0'
        // //         }
        // //     }
        // // }


    //    stage('analyze') {
    //         steps {
    //             // Install trivy
    //             sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin v0.18.3'
    //             sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl > html.tpl'

    //             // Scan all vuln levels
    //             sh 'mkdir -p scan-reports'
    //             sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --format template --template "@html.tpl" -o scan-reports/nodjs-scan.html ./nodejs'
    //             publishHTML target : [
    //                 allowMissing: true,
    //                 alwaysLinkToLastBuild: true,
    //                 keepAll: true,
    //                 reportDir: 'scan-reports',
    //                 reportFiles: 'nodjs-scan.html',
    //                 reportName: 'Trivy Scan',
    //                 reportTitles: 'Trivy Scan'
    //             ]

    //             // Scan again and fail on CRITICAL vulns
    //             sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --exit-code 1 --severity CRITICAL ./nodejs'

    //         }
    //     }
            
            

        // stage(‘Deploy Image’) {
        //     steps{
        //         script {
        //             docker.withRegistry('', registryCredential ) {
        //                 dockerImage.push()
        //             }
        //         }
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

