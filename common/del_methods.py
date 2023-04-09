from common.common import Common


class DelMethods(Common):
    def __init__(self, head_url, token):
        super().__init__(head_url, token)

    def delete_role(self, client_id, role_id):
        """
        Метод удаляет роль.
        """
        file_name = "deleted_role.json"
        postfix = f"/1.0/client/{client_id}/role/{role_id}"
        delete_role = self.del_response(file_name, postfix)
        return delete_role

    def delete_user(self, client_id, user_id):
        """
        Метод удаляет сотрудника.
        """
        file_name = "deleted_user.json"
        postfix = f"/1.0/client/{client_id}/user/{user_id}"
        delete_user = self.del_response(file_name, postfix)
        return delete_user

    def delete_geo_restrictions(self, client_id, geo_id):
        """
        Метод удаляет район.
        """
        file_name = "deleted_geo_restrictions.json"
        postfix = f"/1.0/client/{client_id}/geo_restrictions/{geo_id}"
        delete_geo_restrictions = self.del_response(file_name, postfix)
        return delete_geo_restrictions
