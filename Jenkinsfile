pipeline{
  agent any
  stages {
    stage('Build application'){
      steps{
	    script{
            if (env.BRANCH_NAME == 'dev'||env.BRANCH_NAME == 'realease'||env.BRANCH_NAME == 'text'){
            bat 'docker build -t data-eng-proj2 .'
			}
          }
        }
      }  
    
    stage('Run image'){
      steps{
	    script{
	        if (env.BRANCH_NAME == 'dev'||env.BRANCH_NAME == 'realease'||env.BRANCH_NAME == 'text'){
            bat 'docker run -d -p 5000:5000 -it --name tweet-app data-eng-proj2'
			}
		}
      }
    }
    stage('Unittest'){
      steps{
        script{
		  if (env.BRANCH_NAME == 'test'){
	    bat 'python webapp.py '
            bat 'python test.py '
            }
        }
      }
	}
	
	stage('Stresstest'){
      steps{
        script{
		  if (env.BRANCH_NAME == 'dev'){
			 bat 'pip install requests' 
                         bat 'python stress_test.py '
            }
        }
      }
	}
	
    
    stage('User acceptance'){
      steps{
        script{
          if (env.BRANCH_NAME == 'realease' ) {
            input 'Do you want to push?'
          }
        }
      }
    }
	
	
    stage('Merger'){
      steps{
        script{
          if (env.BRANCH_NAME == 'realease') {
            echo 'Merge'
          }
        }
      }
    }
    
    stage('Docker images down'){
      steps{
        script{
          if (env.BRANCH_NAME == 'dev' || env.BRANCH_NAME == 'realease' ) {
        
	    bat 'docker stop -t=10 tweet-app'	  
            bat 'docker rm -f tweet-app'
	    
          }
        }
      }
    }
	
	
	}

  }
