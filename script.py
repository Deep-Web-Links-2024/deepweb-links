import os
import subprocess
import time

def update_timeline():
    # Modify the timeline.txt file
    with open('timeline.txt', 'a') as file:
        file.write('Update at ' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

    # Commit the changes
    subprocess.run(['git', 'add', 'timeline.txt'])
    subprocess.run(['git', 'commit', '-m', 'Automatic update'])
    
    # Push changes to remote repository
    subprocess.run(['git', 'push'])

if __name__ == "__main__":
    while True:
        update_timeline()
        time.sleep(60)  # Wait for 60 seconds before running again
