import subprocess

ArchKeywords = ['arch wiki', 'archwiki', 'arch linux wiki', 'arch linux']

print("runner.py has been called")
with open('command.txt') as f:
    text = f.read()
if 'discord' in text.lower():
    subprocess.Popen('discord', shell=True)
if 'steam' in text.lower():
    subprocess.Popen('steam', shell=True)
if 'pc' in text.lower():
    subprocess.Popen('xdg-open https://pcpartpicker.com', shell=True)
if any(keyword in text.lower() for keyword in ArchKeywords):
    subprocess.Popen('xdg-open https://wiki.archlinux.org/title/Main_page', shell=True)
if 'youtube' in text.lower():
    subprocess.Popen('xdg-open https://youtube.com', shell=True)
if 'emails' in text.lower():
    subprocess.Popen('betterbird', shell=True)
    subprocess.Popen('/home/comrade/Applications/tutanota-desktop-linux_c6863df2e348e96ec9b3ea20494ce2f5.AppImage', shell=True)
if 'who is in charge' in text.lower():
    subprocess.Popen('espeak-ng "Mavi"', shell=True)
    print("Mavi is in charge")
