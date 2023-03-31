from common.common import Common


class GetMethods(Common):
    def __init__(self, head_url, token):
        super().__init__(head_url, token)

    def get_alerts_info(self):
        """
        Получение информации об уведомлениях (проверить)
        """
        file_name = "alerts_info.json"
        postfix = '/1.0/alerts'
        alerts_info = self.get_response(file_name, postfix)
        return alerts_info

    def get_announcements_info(self):
        """
        Получение информации об уведомлениях (проверить)
        """
        file_name = "announcements_info.json"
        postfix = f'/1.0/client/{self.client_id}/announcements'
        announcements_info = self.get_response(file_name, postfix)
        return announcements_info

    def get_vehicles_info(self):
        """
        Получение информации о машинах (проверить)
        """
        file_name = "vehicles_info.json"
        postfix = '/1.0/vehicles/search'
        vehicles_info = self.get_response(file_name, postfix)
        return vehicles_info

    def get_class_info(self):
        """
        Получение информации о машинах (проверить)
        """
        file_name = "class_info.json"
        postfix = '/1.0/class'
        class_info = self.get_response(file_name, postfix)
        return class_info

    def get_client_info(self):
        """
        Метод получает детальную информацию о клиенте.
        """
        file_name = "client_info.json"
        postfix = f"/1.0/client/{self.client_id}"
        client_info = self.get_response(file_name, postfix)
        return client_info

    def get_employees_list(self):
        """
        Метод получает список сотрудников клиента.
        """
        file_name = "employees_list_info.json"
        postfix = f"/1.0/client/{self.client_id}/user"
        employees = self.get_response(file_name, postfix)
        return employees

    def get_contracts_info(self):
        """
        Метод получает информацию о договорах (НЕТ В ДОКУМЕНТАЦИИ).
        """
        file_name = "contracts_info.json"
        postfix = f"/1.0/client/{self.client_id}/contracts"
        contracts_info = self.get_response(file_name, postfix)
        return contracts_info

    def get_documents_list_info(self, contract_id):
        """
        Метод получает информацию о договоре (НЕТ В ДОКУМЕНТАЦИИ).
        """
        file_name = "documents_list_info.json"
        postfix = f"/1.0/client/{self.client_id}/documents?contract_id={contract_id}"
        documents_info = self.get_response(file_name, postfix)
        return documents_info

    def get_services_info(self):
        """
        Получение информации о сервисах (НЕТ В ДОКУМЕНТАЦИИ)
        """
        file_name = "services_info.json"
        postfix = f"/1.0/client/{self.client_id}/services"
        services_info = self.get_response(file_name, postfix)
        return services_info

    def get_last_orders_info(self):
        """
        Метод получает информацию о последних заказах.
        """
        file_name = "last_orders_info.json"
        postfix = f"/1.0/client/{self.client_id}/order"
        last_orders_info = self.get_response(file_name, postfix)
        return last_orders_info

    def get_roles_list_info(self):
        """
        Метод получает информацию о ролях.
        """
        file_name = "roles_list_info.json"
        postfix = f"/1.0/client/{self.client_id}/role"
        roles_list_info = self.get_response(file_name, postfix)
        return roles_list_info

    def get_cost_centers_settings(self):
        """
        Метод получает информацию о центрах затрат.
        """
        file_name = "cost_centers_info.json"
        postfix = f"/1.0/client/{self.client_id}/cost_centers"
        cost_centers_info = self.get_response(file_name, postfix)
        return cost_centers_info

    def get_geo_restrictions_info(self):
        """
        Метод получает информацию обо всех доступных районах поездок клиента.
        """
        file_name = "geo_restrictions_info.json"
        postfix = f"/1.0/client/{self.client_id}/geo_restrictions"
        geo_restrictions_info = self.get_response(file_name, postfix)
        return geo_restrictions_info

    def get_departments_list_info(self):
        """
        Метод получает информацию о подразделениях.
        """
        file_name = "departments_list_info.json"
        postfix = f"/1.0/client/{self.client_id}/department"
        departments_info = self.get_response(file_name, postfix)
        return departments_info

    def get_department_info(self, department_id):
        """
        Метод получает информацию о конкретном подразделении.
        """
        file_name = "department_info.json"
        postfix = f"/1.0/client/{self.client_id}/department/{department_id}"
        department_info = self.get_response(file_name, postfix)
        return department_info

    def get_employee_info(self, employee_id):
        """
        Метод получает детальную информацию о сотруднике.
        """
        file_name = "employee_info.json"
        postfix = f"/1.0/client/{self.client_id}/user/{employee_id}"
        employee_info = self.get_response(file_name, postfix)
        return employee_info

    def get_order_info(self, order_id):
        """
        Метод получает информацию о конкретной поездке.
        """
        file_name = "order_info.json"
        postfix = f"/1.0/client/{self.client_id}/order/{order_id}"
        order_info = self.get_response(file_name, postfix)
        return order_info

    def get_order_progress_info(self, order_id):
        """
        Получение информации о прогрессе заказа (выполнен, отменен и т.д.).
        """
        file_name = "order_progress_info.json"
        postfix = f"/1.0/client/{self.client_id}/order/{order_id}/progress"
        order_progress_info = self.get_response(file_name, postfix)
        return order_progress_info

    def get_role_info(self, role_id):
        """
        Получение информации о конкретной роли.
        """
        file_name = "role_info.json"
        postfix = f"/1.0/client/{self.client_id}/role/{role_id}"
        role_info = self.get_response(file_name, postfix)
        return role_info

    def get_department_children_info(self, department_id):
        """
        Метод получает информацию о дочерних подразделениях (группах).
        """
        file_name = "department_children_info.json"
        postfix = f"/1.0/client/{self.client_id}/department/{department_id}/children"
        department_info = self.get_response(file_name, postfix)
        return department_info

    def get_tariff_list(self, y, x):
        """
        Получение информации о доступных тарифах по конкретным координатам. Я.Карты отдают координаты y и x.
        Метод ставит координаты на свои места x и y.
        """
        file_name = "tariff_list_info.json"
        postfix = f"/1.0/class?lat={x}&lon={y}"
        tariff_list_info = self.get_response(file_name, postfix)
        return tariff_list_info

    def get_fuel_types_info(self):
        """
        Получение информации о типах заправок.
        """
        file_name = "fuel_types_info.json"
        postfix = f"/1.0/client/{self.client_id}/fuel-types"
        fuel_types_info = self.get_response(file_name, postfix)
        return fuel_types_info

    def get_pay(self, contract_id, value):
        """
        FIXIT получение пдф файла для пополнения счета.
        """
        file_name = "pay.json"
        postfix = f"/1.0/client/{self.client_id}/invoice_pdf?value={value}&contract_id={contract_id}"
        pay_info = self.get_response(file_name, postfix)
        return pay_info
