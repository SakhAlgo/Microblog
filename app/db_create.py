from models import db

db.create_all()
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# db.create_all()
# if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
#     api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
#     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
# else:
#     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

