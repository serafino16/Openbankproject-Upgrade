import subprocess
import boto3

def kubectl_apply(kubeconfig_file, manifest_files):
    try:
        
        print(f"Setting KUBECONFIG to {kubeconfig_file}...")
        apply_command = f"kubectl --kubeconfig={kubeconfig_file} apply -f {manifest_files}"
        apply_process = subprocess.Popen(apply_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = apply_process.communicate()

        if apply_process.returncode != 0:
            raise Exception(f"Error during kubectl apply: {stderr.decode('utf-8')}")
        
        print(f"Successfully applied manifests: {manifest_files}")
    except Exception as e:
        print(f"Error: {str(e)}")
