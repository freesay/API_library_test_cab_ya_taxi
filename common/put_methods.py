from common.common import Common
from common.json_methods import load_data


class PutMethods(Common):
    def __init__(self, head_url, token):
        super().__init__(head_url, token)

    def change_draft_order(self, order_id):
        """
        Метод изменяет черновик заказа.
        """
        file_name = "changed_draft_order.json"
        postfix = f"/1.0/client/{self.client_id}/order/{order_id}/change"
        data = load_data(self.put_examples, 'change_draft_order.json')
        change_draft_order = self.put_response(file_name, postfix, data)
        return change_draft_order

    def change_role(self, role_id):
        """
        Метод изменяет роль.
        """
        file_name = "changed_draft_order.json"
        postfix = f"/1.0/client/{self.client_id}/role/{role_id}"
        data = load_data(self.put_examples, 'change_role.json')
        change_role = self.put_response(file_name, postfix, data)
        return change_role

    def change_employee_with_role(self, employee_id):
        """
        Метод изменяет данные о сотруднике с существующей ролью.
        """
        file_name = "changed_employee_with_role.json"
        postfix = f"/1.0/client/{self.client_id}/user/{employee_id}"
        data = load_data(self.put_examples, 'change_employee_with_role.json')
        change_employee_with_role = self.put_response(file_name, postfix, data)
        return change_employee_with_role

    def restore_employee_with_role(self, employee_id):
        """
        Метод восстанавливает сотрудника с существующей ролью.
        """
        file_name = "restored_employee_with_role.json"
        postfix = f"/1.0/client/{self.client_id}/user/{employee_id}/restore"
        data = load_data(self.put_examples, 'restore_employee_with_role.json')
        restore_employee_with_role = self.put_response(file_name, postfix, data)
        return restore_employee_with_role

    def change_geo_restrictions(self, geo_id):
        """
        Метод изменяет данные о районе.
        """
        file_name = "changed_geo_restrictions.json"
        postfix = f"/1.0/client/{self.client_id}/geo_restrictions/{geo_id}"
        data = load_data(self.put_examples, 'change_geo_restrictions.json')
        change_geo_restrictions = self.put_response(file_name, postfix, data)
        return change_geo_restrictions
