from clients.users_client import UserClient

client = UserClient()


def test_list_all_users():

    """
        Test on API showing all existing users
    """

    print("TEST: LIST ALL EXISTING USERS")
    print("")
    response = client.show_all_users()
    assert response.status_code == 200, "Error: There are not any users."
    user_count = len(response.as_dict["payload"])
    if user_count > 1:
        print("Result: SUCCESS", "\n")
        print("There are " + str(user_count) + " users.")
    else:
        print("Result: SUCCESS", "\n")
        print("There is " + str(user_count) + " user.")

    print(response.as_dict["payload"])
    print(2 * "\n")


def test_show_user_info(username):

    """
        Test on showing user's information
    """

    print("TEST: SHOW USER'S INFO")
    print("")

    response = client.get_user_info(username)
    assert bool(response), "Error: This user does not exists."

    print("Result: SUCCESS", "\n")
    print("User's information: " + str(response))
    print(2 * "\n")


def test_user_can_be_updated(new_info):

    """
        Test on updating user's information
    """

    print("TEST: UPDATE USER'S INFO")
    print("")

    response = client.update_user(new_info)
    assert response.status_code == 201, "Error: User can't be updated"

    print("Result: SUCCESS", "\n")
    print("User is updated with " + str(new_info))
    print(2 * "\n")


def test_new_user_can_be_added(new_user):

    """
        Test on creating new user
    """

    print("TEST: ADD NEW USER")
    print("")

    response = client.create_user(new_user)
    assert response.status_code == 201, "Error: This user can't be added"

    print("Result: SUCCESS", "\n")
    print("New user " + new_user["username"] + " is added.")
    print(2 * "\n")
