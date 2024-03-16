from rolepermissions.roles import AbstractUserRole

class Alunopermission(AbstractUserRole):
    available_permissions = {
        'verNota':True
    }

class Professorpermission(AbstractUserRole):
    available_permissions ={
        'verNota':True,
        'editarNota':True
    }

class Adminpermission(AbstractUserRole):
    available_permissions = {
        'fullAcess':True
    }