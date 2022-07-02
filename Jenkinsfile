pipeline {
    agent any
    environment {
        IMAGE_TAG_NAME = "dss"
        IMAGE_TAG_VERSION = 1.0
        IMAGE_VULNERABILITY = "medium"

        CTN_NAME_TEST = "dss"

        CTN_INTERNAL_PORT = 8080
        CTN_EXTERNAL_PORT = 7997
    }
 

    stages {
            
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


       stage('analyze') {
            steps {
                // sh 'echo "$IMAGE_TAG_NAME:$IMAGE_TAG_VERSION"'
                // sh 'echo "$IMAGE_TAG_NAME:$IMAGE_TAG_VERSION" > anchore_images'
                // anchore name: 'anchore_images'

                writeFile file: 'anchore_images', text: 'dss:1.0'  
                    anchore name: 'anchore_images'
                }
        }
        stage('teardown') {
            steps {
                sh'''
                    for i in `cat anchore_images | awk '{print $1}'`;do docker rmi $i; done
                '''
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

