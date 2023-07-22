import pyautogui as gu
import time
import subprocess

# Open CMD
cmd_process = subprocess.Popen("cmd", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

time.sleep(5)

# creating virtual environment named env
gu.typewrite('python -m venv env')
gu.hotkey('enter')

time.sleep(2)
# activate virtual environment
gu.typewrite('cd env/scripts')
gu.hotkey('enter')
gu.typewrite('activate')
gu.hotkey('enter')

# installing django
gu.typewrite('pip install django')
gu.hotkey('enter')

time.sleep(3)
# getting back to root directory
gu.typewrite('cd ..')
gu.hotkey('enter')
gu.typewrite('cd ..')
gu.hotkey('enter')

# creating a directory to put our django files in
gu.typewrite('mkdir mysite')
gu.hotkey('enter')
gu.typewrite('cd mysite')
gu.hotkey('enter')

# starting django-admin config
gu.typewrite('django-admin startproject config .')
gu.hotkey('enter')

time.sleep(2)
# migrating 
gu.typewrite('python manage.py migrate')
gu.hotkey('enter')

# running 
gu.typewrite('python manage.py runserver')
gu.hotkey('enter')

