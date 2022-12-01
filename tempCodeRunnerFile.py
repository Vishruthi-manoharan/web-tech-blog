
from werkzeug.utils import secure_filename
import uuid as uuid
import os


# Create a Flask Instance
app = Flask(__name__)
# Add CKEditor
#ckeditor = CKEditor(app)
# Add Database
# Old SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fvmdxyjigwbmiu:d31d36c7613e08f7ad37a6e40007189d7f2f44fbc99234b339994780a122d870@ec2-3-214-190-189.compute-1.amazonaws.com:5432/d17b5scj97ckqe'
# New MySQL DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/our_users'
# Secret Key!
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"
# Initialize The Database

UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask_Login Stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
	return Users.query.get(int(user_id))

# Pass Stuff To Navbar