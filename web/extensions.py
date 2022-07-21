from flask import url_for
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

admin = Admin()
db = SQLAlchemy()
migrate = Migrate()


class PublicSiteLink(MenuLink):
    def get_url(self):
        return url_for("index.index")


# Remove duplicitous "Home" link on admin menu
admin._menu.pop()

# Add link on the admin menu leading back to main site
admin.add_link(PublicSiteLink(name="Public Site"))
