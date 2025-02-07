import subprocess
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if not is_admin():

    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()




def activate_windows_kms():
    try:
        #Set-the-KMS server
        kms_server = "kms8.msguides.com"
        subprocess.run(f"slmgr /skms {kms_server}", shell=True, check=True)

        #Activate-Windows
        subprocess.run("slmgr /ato", shell=True, check=True)

        print("Windows activation successful!")
    except subprocess.CalledProcessError as e:
        print(f"Activation failed: {e}")


if __name__ == "__main__":
    activate_windows_kms()
