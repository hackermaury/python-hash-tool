import subprocess
print("Wi-Fi Password Viewer")
profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], shell=True,text=True)
names = []
for line in profiles.split('\n'):
    if "All User Profile" in line:
        name = line.split(":")[1].strip()
        names.append(name)
for i, name in enumerate(names):
            print(f"{i}. {name}")

choice = int(input("Enter the number of the Wi-Fi profile to view the password: "))
wifi = names[choice - 1]
result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear'], shell=True, text=True)
for line in result.split('\n'):
    if "Key Content" in line:
        print(f"The password for Wi-Fi profile {wifi} is: {line.split(':')[1].strip()}")
        