from tests.users_test import *
import json

# Reading Users JSON file
with open('./resources/test_users.json') as json_file:
    data = json.load(json_file)

"""
    Perform all API testing for all users from JSON file in following order:
        1. Add new user
        2. Show specific user's information
        3. Update specific user's information
        4. Show updated user's information
        5. Show all existing users
"""

for user, info in data.items():
    test_new_user_can_be_added(info[0])
    test_show_user_info(user)
    test_user_can_be_updated(info[1])
    test_show_user_info(user)
    test_list_all_users()