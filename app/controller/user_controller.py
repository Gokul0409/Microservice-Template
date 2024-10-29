from app.config.config import Session
from app.model.user_model import UserModel
from sanic.response import json
from sanic import Blueprint


def list_all_user():

    """
    list_all_user : Return all User List

    Returns:
        user (list) : list of all row of table
    """
    db = Session()
    users = db.query(UserModel).all()
    return users


def add_user(data: UserModel):

    """
    add_user : Used to add new user

    Args:
        data (UserModel): Logic to add new user to DB

    Raises:
        Exception: Raise if UserModel parameter is invalid
    """

    db = Session()

    if isinstance(data, UserModel):
        db.add(instance=data)
        db.commit()
        db.close()
    else:
        raise Exception("Invalid Data Found")


user_print = Blueprint("user_print")


@user_print.route("/user", methods=["GET"])
async def list_all_users(request):
    users = list_all_user()
    return json([{"SN": user.sn, "Name": user.name} for user in users])


@user_print.route("/create_user", methods=["POST"])
async def create_user(request: json):

    """
    create_user: Used to create New User

    Args:
        request (json): Input Json with User Data

    Returns:
        json : Acknowledgement message after creating New User

    """

    data = UserModel(**request.json)
    add_user(data)
    return json({"UserCreation": "Added User Successfully"}, status=200)
