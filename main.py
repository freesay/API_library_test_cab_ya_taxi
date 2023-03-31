from common.get_methods import GetMethods
from common.post_methods import PostMethods
from common.put_methods import PutMethods
from common.del_methods import DelMethods

HEAD_URL = 'http://corp-client.taxi.tst.yandex.ru/api'
TOKEN = 'TOKEN'

get_req = GetMethods(HEAD_URL, TOKEN)
post_req = PostMethods(HEAD_URL, TOKEN)
put_req = PutMethods(HEAD_URL, TOKEN)
del_req = DelMethods(HEAD_URL, TOKEN)

# contract_id = get_req.get_contracts_info()["contracts"][0]["contract_id"]
# employee_id = get_req.get_employees_list()["items"][0]["_id"]
# department_id = get_req.get_departments_list_info()["departments"][0]["_id"]
# order_id = get_req.get_last_orders_info()["items"][0]["_id"]
# role_id = get_req.get_roles_list_info()["items"][0]["_id"]
# geo_id = get_req.get_geo_restrictions_info()["items"][0]["_id"]


# print(get_req.refresh_token())
# print(get_req.get_client_info())
# print(get_req.get_departments_list_info())
# print(get_req.get_contracts_info())
# print(get_req.get_employees_list())
# print(get_req.get_services_info())
# print(get_req.get_last_orders_info())
# print(get_req.get_roles_list_info())
# print(get_req.get_cost_centers_settings())
# print(get_req.get_geo_restrictions_info())
# print(get_req.get_documents_list_info(contract_id))
# print(get_req.get_employee_info(employee_id))
# print(get_req.get_department_info(department_id))
# print(get_req.get_department_children_info(department_id))
# print(get_req.get_order_info(order_id))
# print(post_req.get_order_cargo_info())
# print(get_req.get_order_progress_info(order_id))
# print(get_req.get_role_info(role_id))
# print(get_req.get_tariff_list(y_coord, x_coord))
# print(get_req.get_fuel_types_info())
# print(get_req.get_alerts_info())
# print(get_req.get_alerts_info())
# print(get_req.get_fuel_types_info())
# print(get_req.get_pay(contract_id, 1234))
# print(get_req.get_announcements_info())
# print(get_req.get_class_info())

# print(post_req.create_cost_center())
# print(post_req.edit_cost_center())
# print(post_req.create_draft_order_taxi())
# print(post_req.create_draft_order_logistic())
# print(post_req.processing_draft_order(order_id))
# print(post_req.cancel_order(order_id))
# print(post_req.create_role())
# print(post_req.create_employee())
# print(post_req.create_employee())
# print(post_req.get_estimate_info())
# print(post_req.create_geo_restrictions())
# print(post_req.wtf())

# print(put_req.change_draft_order(order_id))
# print(put_req.change_role(role_id))
# print(put_req.change_employee_with_role(employee_id))
# print(put_req.change_employee_without_role())
# print(put_req.restore_employee_with_role(employee_id))
# print(put_req.restore_employee_without_role())
# print(put_req.change_geo_restrictions(geo_id))
# print(put_req.change_employee_with_role(employee_id))
# print(put_req.restore_employee_with_role(employee_id))
# print(put_req.change_geo_restrictions(geo_id))

# print(del_req.delete_role(role_id))
# print(del_req.delete_employee(user_id))
# print(del_req.delete_geo_restrictions(geo_id))
