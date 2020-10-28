import subprocess

if __name__ == '__main__':
    subprocess.call(['gunicorn', 'routing_manager:app', '--reload'])
