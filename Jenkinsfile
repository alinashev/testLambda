pipeline {
    agent any
    stages {
        stage('Delete Stack') {
            steps {
                withCredentials([aws(accessKeyVariable:'AWS_ACCESS_KEY_ID', credentialsId:'aws-cresds1', secretKeyVariable:'AWS_SECRET_ACCESS_KEY')])
                {
                sh '''
                    aws cloudformation create-stack \
                      --stack-name a-testLambda2 \
                      --template-body file://template.yml --region 'us-east-2' \
                      --capabilities CAPABILITY_NAMED_IAM \
                      --parameters ParameterKey=FunctionName,ParameterValue=A-test-env \
                      ParameterKey=LambdaEnvBucket,ParameterValue=bucket_pipeline
                    '''
                }
              }
             }
            stage('Stack create complete'){
            steps{
                withCredentials([aws(accessKeyVariable:'AWS_ACCESS_KEY_ID', credentialsId:'aws-cresds1', secretKeyVariable:'AWS_SECRET_ACCESS_KEY')])
                    {
                    sh '''
                        aws cloudformation wait stack-create-complete \
                            --stack-name a-testLambda2  \
                            --region 'us-east-2'
                        '''
                    }
                }
            }

           }
         }