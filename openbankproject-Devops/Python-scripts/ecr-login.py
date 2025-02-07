import subprocess
import os
import boto3

def ecr_login(region, docker_registry):
    try:
        
        login_command = f"aws ecr get-login-password --region {region}"
        login_process = subprocess.Popen(login_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = login_process.communicate()

        if login_process.returncode != 0:
            raise Exception(f"Error during AWS ECR login: {stderr.decode('utf-8')}")

        
        docker_login_command = f"docker login --username AWS --password-stdin {docker_registry}"
        docker_process = subprocess.Popen(docker_login_command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        docker_process.stdin.write(stdout)  
        docker_process.stdin.close()
        docker_stdout, docker_stderr = docker_process.communicate()

        if docker_process.returncode != 0:
            raise Exception(f"Error during Docker login: {docker_stderr.decode('utf-8')}")

        print("Successfully logged in to AWS ECR and Docker.")
    except Exception as e:
        print(f"Error: {str(e)}")
