from src.entities.user import User, UserSchema#,db
from src import db
from flask_jwt_extended import (
	create_access_token, create_refresh_token, get_jwt_identity,
	verify_jwt_in_request, jwt_required, current_user)

def authenticate_user(user):
	user.is_authenticated = True
	db.session.commit()
	return create_access_token(identity=user), create_refresh_token(identity=user)

@jwt_required()
def get_authenticated_user(username):
	identity = get_jwt_identity()
	# user = db.query(User).filter_by(username=username).first()
	if identity and current_user.username == username:
		return current_user
	return False


