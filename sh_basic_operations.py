import os

def sh_file(operation,first,second):

    nameTail = f'Opt_{operation}_First{first}_Second{second}'

    f = open(f"al3x_{nameTail}.sh", 'w+')#INSTEAD OF al3x WRITE YOUR USERNAME
    f.write('#!/bin/bash\n')
   
    f.write('#SBATCH --account=def-ravh011\n') #RODRIGOS'S ACC IF YOU ARE IN THE GRAHAM SERVER YOU CAN USE account=rrg-ravh011 OTHERWISE YOU NEED TO USE --account=def-ravh011 
    #f.write(f'#SBATCH --account=rrg-ravh011\n')
    f.write(f'#SBATCH --job-name={nameTail}\n')
    f.write('#SBATCH --time=00:10:00\n') # time of computation
    f.write(f'#SBATCH --output=out_{nameTail}.log\n')
    f.write(f'#SBATCH --mem-per-cpu=10G\n')
    #f.write(f'#SBATCH --gpus-per-node=v100:1\n') #IF YOU NEED GPUS AND YOUR CODE IS COMPATIBLE 
    f.write(f'#SBATCH --cpus-per-task=2\n\n') 


    f.write('module load python/3.9.6 \n') 
    f.write('source /home/al3x/envs/test/bin/activate\n') # load your environment YOU CAN USE THE COMAND pwd TO FIND OUT THE PATH TO YOUR ENVIRONMENT 
    f.write('module load scipy-stack \n')
    #############################################################################i
    ## WRITE SCRIPT EXECUTION

    f.write(f'python basic_operations.py --op {operation} --fst {first} --sec {second}\n') ## ADD VARIABLES HERE IT NEEDS TO HAVE THE SAME EXACT NAME AS THE FILES IN THE ARGPARSER ON YOUR MAIN FILE !!!!!

    f.write('\n\n')
    f.close()




    #############################################################################
    ## SUBMIT JOB TO COMPUTE CANADA

    if os.path.isfile(f"al3x_{nameTail}.sh"): #WRITE YOUR OWN USEERNAME
        print(f"Submitting al3x_{nameTail}.sh")
        os.system(f"sbatch al3x_{nameTail}.sh")


if __name__== "__main__":
    
    op = ['times']
    first = [1,2,3,4]
    second = [10.]

    for _op in op:
        for _first in first:
            for _second in second:
                sh_file(_op,_first,_second) 
