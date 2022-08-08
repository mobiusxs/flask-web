from flask import redirect
from flask import url_for
from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin import expose
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView

from .extensions import db
from .public.models import LogbookModel


class SecureAdminIndexView(AdminIndexView):
    def is_visible(self):
        """Remove duplicate 'Admin Home' link from nav"""

        return False

    @expose('/')
    def index(self):
        """Conditionally grant access to admin interface"""

        # TODO: Implement with your logic here
        conditional = True

        if conditional:
            return self.render(self._template)
        else:
            return redirect(url_for('public.index'))


class PublicSiteLink(MenuLink):
    """Menu link leading to public index."""

    def get_url(self):
        return url_for('public.index')


class SecuredModelView(ModelView):
    def is_accessible(self):
        # TODO: Implement with your logic here
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('public.index'))


class ExampleModelView(SecuredModelView):
    """See flask_admin.model.BaseModelView for permission and customization options"""

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = False
    can_export = False


admin = Admin(index_view=SecureAdminIndexView(name='Admin Home'))
admin.add_link(PublicSiteLink(name='Public Site'))
admin.add_view(ExampleModelView(LogbookModel, session=db.session, name='Logbook', category=None))
