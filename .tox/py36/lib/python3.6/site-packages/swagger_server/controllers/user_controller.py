import connexion
import six
import json

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util
from swagger_server.models import User


def create_user(body):  # noqa: E501
    """Create user

    This can only be done by the logged in user. # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        u = User(body["username"], body["first_name"], body["last_name"],
                 body["email"], body["password"])
        util.add_user(u)
    return 'User added successfully', 201


def delete_user(username):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param username: The name that needs to be deleted
    :type username: str

    :rtype: None
    """
    u = User.query.filter(User._username == username).first()
    util.delete_user(u)
    return 'do some magic!'


def get_user_by_name(username):  # noqa: E501
    """Get user by user name

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing.
    :type username: str

    :rtype: User
    """
    if not username:
        return "Ivalid username", 400
    u = User.query.filter(User._username == username).first()
    if u:
        return u.to_dict(),200
    return "User not found", 404


def update_user(username, body):  # noqa: E501
    """Updated user

    This can only be done by the logged in user. # noqa: E501

    :param username: name that need to be updated
    :type username: str
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
        u = User.query.filter(User._username == username)
        util.update_user(u, body)
    return 'do some magic!'
