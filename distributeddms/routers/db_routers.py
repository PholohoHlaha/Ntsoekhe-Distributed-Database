class Primary_Health_CenterRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'auth', 'contenttypes', 'admin', 'sessions'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to Primary_Health_CenterDB.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'Primary_Health_CenterDB'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to Primary_Health_CenterDB.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'Primary_Health_CenterDB'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'Primary_Health_CenterDB' database.
        """
        if app_label in self.route_app_labels:
            return db == 'Primary_Health_CenterDB'
        return None
    

class Hospital_CenterRouter:

    route_app_labels = {'hospital_center'}

    def db_for_read(self, model, **hints):
 
        if model._meta.app_label in self.route_app_labels:
            return 'Hospital_CenterDB'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'Hospital_CenterDB'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == 'Hospital_CenterDB'
        return None
    


class Tertiary_CenterRouter:

    route_app_labels = {'Tertiary_center'}

    def db_for_read(self, model, **hints):
 
        if model._meta.app_label in self.route_app_labels:
            return 'Tertiary_CenterDB'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'Tertiary_CenterDB'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == 'Tertiary_CenterDB'
        return None

class NorthernRecordsRouter:

    route_app_labels = {'Northern_records'}

    def db_for_read(self, model, **hints):
 
        if model._meta.app_label in self.route_app_labels:
            return 'Northern_PatientsRecordDB'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'Northern_PatientsRecordDB'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label in self.route_app_labels:
            return db == 'Northern_PatientsRecordDB'
        return None