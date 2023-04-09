from common.common import Common


class GetMethods(Common):
    def __init__(self, head_url, token):
        super().__init__(head_url, token)

    def get_class_info(self):
        """
        Получение информации о машинах
        """
        file_name = "class_info.json"
        postfix = '/1.0/class'
        class_info = self.get_response(file_name, postfix)
        return class_info

    def get_tariff_list(self, x, y):
        """
        Получение информации о доступных тарифах по конкретным координатам.
        """
        file_name = "tariff_list_info.json"
        postfix = f"/1.0/class?lat={x}&lon={y}"
        tariff_list_info = self.get_response(file_name, postfix)
        return tariff_list_info

    def get_client_info(self, client_id):
        """
        Метод получает детальную информацию о клиенте.
        """
        file_name = "client_info.json"
        postfix = f"/1.0/client/{client_id}"
        client_info = self.get_response(file_name, postfix)
        return client_info

    def get_cost_centers_settings(self, client_id):
        """
        Метод получает информацию о центрах затрат.
        """
        file_name = "cost_centers_info.json"
        postfix = f"/1.0/client/{client_id}/cost_centers"
        cost_centers_info = self.get_response(file_name, postfix)
        return cost_centers_info

    def get_last_orders_info(self, client_id):
        """
        Метод получает информацию о последних заказах.
        """
        file_name = "last_orders_info.json"
        postfix = f"/1.0/client/{client_id}/order"
        last_orders_info = self.get_response(file_name, postfix)
        return last_orders_info

    def get_order_info(self, client_id, order_id):
        """
        Метод получает информацию о конкретной поездке.
        """
        file_name = "order_info.json"
        postfix = f"/1.0/client/{client_id}/order/{order_id}"
        order_info = self.get_response(file_name, postfix)
        return order_info

    def get_order_progress_info(self, client_id, order_id):
        """
        Получение информации о прогрессе заказа (выполнен, отменен и т.д.).
        """
        file_name = "order_progress_info.json"
        postfix = f"/1.0/client/{client_id}/order/{order_id}/progress"
        order_progress_info = self.get_response(file_name, postfix)
        return order_progress_info

    def get_roles_list_info(self, client_id):
        """
        Так и не въехал, что такое РОЛЬ (проверить).
        """
        file_name = "roles_list_info.json"
        postfix = f"/1.0/client/{client_id}/role"
        roles_list_info = self.get_response(file_name, postfix)
        return roles_list_info

    def get_role_info(self, client_id, role_id):
        """
        Получение информации о конкретной роли.
        """
        file_name = "role_info.json"
        postfix = f"/1.0/client/{client_id}/role/{role_id}"
        role_info = self.get_response(file_name, postfix)
        return role_info

    def get_users_list(self, client_id):
        """
        Метод получает список сотрудников клиента.
        """
        file_name = "users_list_info.json"
        postfix = f"/1.0/client/{client_id}/user"
        users = self.get_response(file_name, postfix)
        return users

    def get_user_info(self, client_id, user_id):
        """
        Метод получает детальную информацию о сотруднике.
        """
        file_name = "user_info.json"
        postfix = f"/1.0/client/{client_id}/user/{user_id}"
        user_info = self.get_response(file_name, postfix)
        return user_info

    def get_geo_restrictions_info(self, client_id):
        """
        Метод получает информацию обо всех доступных районах поездок клиента.
        """
        file_name = "geo_restrictions_info.json"
        postfix = f"/1.0/client/{client_id}/geo_restrictions"
        geo_restrictions_info = self.get_response(file_name, postfix)
        return geo_restrictions_info

    def get_departments_list_info(self, client_id):
        """
        Метод получает информацию о подразделениях.
        """
        file_name = "departments_list_info.json"
        postfix = f"/1.0/client/{client_id}/department"
        departments_info = self.get_response(file_name, postfix)
        return departments_info

    def get_department_info(self, client_id, department_id):
        """
        Метод получает информацию о конкретном подразделении.
        """
        file_name = "department_info.json"
        postfix = f"/1.0/client/{client_id}/department/{department_id}"
        department_info = self.get_response(file_name, postfix)
        return department_info
