from common.get_methods import GetMethods
from common.post_methods import PostMethods
from common.put_methods import PutMethods
from common.del_methods import DelMethods


HEAD_URL = 'http://corp-client.taxi.tst.yandex.ru/api'
TOKEN = ''

get_req = GetMethods(HEAD_URL, TOKEN)
post_req = PostMethods(HEAD_URL, TOKEN)
put_req = PutMethods(HEAD_URL, TOKEN)
del_req = DelMethods(HEAD_URL, TOKEN)

# Обновить токен
# print(get_req.refresh_token())


# Здесь достаются нужные id
# client_id требуется во множестве запросов. Его лучше оставить раскомментированным.
client_id = get_req.get_auth_info()['client_id']
# user_id = get_req.get_users_list(client_id)["items"][0]["_id"]
# department_id = get_req.get_departments_list_info(client_id)["departments"][0]["_id"]
# order_id = get_req.get_last_orders_info(client_id)["items"][0]["_id"]
# role_id = get_req.get_roles_list_info(client_id)["items"][0]["_id"]
# geo_id = get_req.get_geo_restrictions_info(client_id)["items"][0]["_id"]

# print(get_req.get_class_info())
# print(get_req.get_tariff_list(55.752313, 37.538664))
# print(get_req.get_client_info(client_id))
# print(get_req.get_cost_centers_settings(client_id))
# print(get_req.get_last_orders_info(client_id))
# print(get_req.get_order_info(client_id, order_id))
# print(get_req.get_order_progress_info(client_id, order_id))
# print(get_req.get_roles_list_info(client_id))
# print(get_req.get_role_info(client_id, role_id))
# print(get_req.get_users_list(client_id))
# print(get_req.get_user_info(client_id, user_id))
# print(get_req.get_geo_restrictions_info(client_id))
# print(get_req.get_departments_list_info(client_id))
# print(get_req.get_department_info(client_id, department_id))

# print(post_req.create_cost_center(client_id))
# print(post_req.estimate_info())
# print(post_req.create_draft_order_taxi(client_id))
# print(post_req.create_draft_order_logistic(client_id))
# print(post_req.cancel_order(client_id, order_id))
# print(post_req.processing_draft_order(client_id, order_id))
# print(post_req.create_role(client_id))
# print(post_req.create_user(client_id))
# print(post_req.create_geo_restrictions(client_id))

# print(put_req.change_draft_order(client_id, order_id))
# print(put_req.change_role(client_id, role_id))
# print(put_req.change_employee(client_id, user_id))
# print(put_req.change_geo_restrictions(client_id, geo_id))

# print(del_req.delete_role(client_id, role_id))
# print(del_req.delete_employee(client_id, user_id))
# print(del_req.delete_geo_restrictions(client_id, geo_id))
