import subprocess

def make_a_call(phonenumber):
        adb_path = 'adb'
        command = f"{adb_path} shell am start -a android.intent.action.CALL -d tel:{phonenumber}"
    
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Calling {phonenumber}...")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

def call(query):
    if "sahil" in query:
        phonenumber = "9607118530"
        make_a_call(phonenumber)
    elif "siddharth" in query:
        phonenumber= "9834647612"
        make_a_call(phonenumber)
    elif "laukik" in query:
         phonenumber = "8767364403"
         make_a_call(phonenumber)
    elif "parth" in query:
         phonenumber = "7721904123"
         make_a_call(phonenumber)

