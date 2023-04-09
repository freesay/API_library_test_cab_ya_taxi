from common.common import Common
from common.json_methods import load_data


class PutMethods(Common):
    def __init__(self, head_url, token):
        super().__init__(head_url, token)

    def change_draft_order(self, client_id, order_id):
        """
        Метод изменяет черновик заказа.
        """
        file_name = "changed_draft_order.json"
        postfix = f"/1.0/client/{client_id}/order/{order_id}/change"
        data = load_data(self.parent_dir_request, self.put_examples, 'change_draft_order.json')
        change_draft_order = self.put_response(file_name, postfix, data)
        return change_draft_order

    def change_role(self, client_id, role_id):
        """
        Метод изменяет роль.
        """
        file_name = "changed_draft_order.json"
        postfix = f"/1.0/client/{client_id}/role/{role_id}"
        data = load_data(self.parent_dir_request, self.put_examples, 'change_role.json')
        change_role = self.put_response(file_name, postfix, data)
        return change_role

    def change_user(self, client_id, user_id):
        """
        Метод изменяет данные о сотруднике с существующей ролью.
        """
        file_name = "changed_user.json"
        postfix = f"/1.0/client/{client_id}/user/{user_id}"
        data = load_data(self.parent_dir_request, self.put_examples, 'change_user.json')
        change_user = self.put_response(file_name, postfix, data)
        return change_user

    def change_geo_restrictions(self, client_id, geo_id):
        """
        Метод изменяет данные о районе.
        """
        file_name = "changed_geo_restrictions.json"
        postfix = f"/1.0/client/{client_id}/geo_restrictions/{geo_id}"
        data = load_data(self.parent_dir_request, self.put_examples, 'change_geo_restrictions.json')
        change_geo_restrictions = self.put_response(file_name, postfix, data)
        return change_geo_restrictions
