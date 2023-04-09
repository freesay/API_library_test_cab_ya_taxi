from common.common import Common
from common.json_methods import load_data


class PostMethods(Common):
    def __init__(self, head_url, token):
        super().__init__(head_url, token)

    def create_cost_center(self, client_id):
        """
        Метод создает центр затрат. Так же можно редактировать подразделение.
        """
        file_name = "created_cost_center.json"
        postfix = f"/1.0/client/{client_id}/cost_centers"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_cost_center.json')
        created_cost_center = self.post_response(file_name, postfix, data)
        return created_cost_center

    def estimate_info(self):
        """
        Метод получает информацию о предстоящей поездке.
        """
        file_name = "produced_estimate_info.json"
        postfix = f"/1.0/estimate"
        data = load_data(self.parent_dir_request, self.post_examples, 'estimate_info.json')
        produced_estimate_info = self.post_response(file_name, postfix, data)
        return produced_estimate_info

    def create_draft_order_taxi(self, client_id):
        """
        Метод создает черновик заказа такси.
        """
        file_name = "created_draft_order_taxi.json"
        postfix = f"/1.0/client/{client_id}/order"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_draft_order_taxi.json')
        created_draft_order_taxi = self.post_response(file_name, postfix, data)
        return created_draft_order_taxi

    def create_draft_order_logistic(self, client_id):
        """
        Метод создает черновик заказа доставки.
        """
        file_name = "created_draft_order_logistic.json"
        postfix = f"/1.0/client/{client_id}/order"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_draft_order_logistic.json')
        created_draft_order_logistic = self.post_response(file_name, postfix, data)
        return created_draft_order_logistic

    def cancel_order(self, client_id, order_id):
        """
        Отменить заказ.
        """
        file_name = "canceled_order.json"
        postfix = f"/1.0/client/{client_id}/order/{order_id}/cancel"
        data = load_data(self.parent_dir_request, self.post_examples, 'cancel_order.json')
        canceled_order = self.post_response(file_name, postfix, data)
        return canceled_order

    def processing_draft_order(self, client_id, order_id):
        """
        Метод запускает обработку черновика заказа.
        """
        file_name = "processed_draft_order.json"
        postfix = f"/1.0/client/{client_id}/order/{order_id}/processing"
        processed_draft_order = self.post_response(file_name, postfix)
        return processed_draft_order

    def create_role(self, client_id):
        """
        Метод создает роль.
        """
        file_name = "created_role.json"
        postfix = f"/1.0/client/{client_id}/role"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_role.json')
        created_role = self.post_response(file_name, postfix, data)
        return created_role

    def create_user(self, client_id):
        """
        Метод создает сотрудника.
        """
        file_name = "created_user.json"
        postfix = f"/1.0/client/{client_id}/user"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_user.json')
        created_user = self.post_response(file_name, postfix, data)
        return created_user

    def create_geo_restrictions(self, client_id):
        """
        Метод создает район.
        """
        file_name = "created_geo_restriction.json"
        postfix = f"/1.0/client/{client_id}/geo_restrictions"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_geo_restrictions.json')
        created_geo_restrictions = self.post_response(file_name, postfix, data)
        return created_geo_restrictions

    def create_department(self, client_id):
        """
        Метод создает подразделение.
        """
        file_name = "created_department.json"
        postfix = f"/1.0/client/{client_id}/department"
        data = load_data(self.parent_dir_request, self.post_examples, 'create_department.json')
        created_department = self.post_response(file_name, postfix, data)
        return created_department
