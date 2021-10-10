"""
    Token can only be retrieved with existing user's credentials,
    so a small selenium script should be run first to create the first user.
    And then the main test script is run.
"""


import subprocess

if __name__ == "__main__":

    program_list = ['create_first_user.py', 'run_all_tests.py']

    for program in program_list:
        subprocess.call(['python', program], shell=True)
        print("Finished:" + program)
