import subprocess
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def run_command(cmd):
    result = subprocess.run(cmd,capture_output=True, shell=True)
    if result.returncode == 0:
        logging.info(f"Command: {cmd} finished successfully, stdout: {result.stdout}")
    else:
        logging.error(f"Command: {cmd} failed with exit code: {result.returncode} and error message: {result.stderr}")


run_command("dir")