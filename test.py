# -*- coding: utf-8 -*-

#    File Name：       test
#    Description :
#    Author :          LvYang
#    date：            2019/4/1
#    Change Activity:  2019/4/1:
# a = [{u'en_name': u'user', u'name': u'\u6d4b\u8bd5', u'created_time_ts': 1500618901, u'platform_id': 0, u'func_list': [{u'sort': u'1', u'en_name': u'', u'name': u'\u4efb\u52a1\u7ba1\u7406', u'created_time_ts': u'1514355246', u'parent_id': u'0', u'path': u'', u'project_id': u'471', u'type': 0, u'id': u'1200', u'updated_time_ts': u'0', u'desc': u''}, {u'sort': 0, u'en_name': u'', u'name': u'\u5de5\u4f5c\u6d41\u7a0b-\u521b\u5efa\u4efb\u52a1', u'created_time_ts': u'1514355422', u'parent_id': u'1200', u'path': u'/taskmanagetasklist/', u'project_id': u'471', u'type': 1, u'id': u'1206', u'updated_time_ts': u'0', u'desc': u''}, {u'sort': u'1', u'en_name': u'', u'name': u'\u5de5\u4f5c\u6d41\u7a0b-\u65e5\u5fd7\u5217\u8868', u'created_time_ts': u'1514355467', u'parent_id': u'1200', u'path': u'/taskmanageloglist/', u'project_id': u'471', u'type': 1, u'id': u'1208', u'updated_time_ts': u'0', u'desc': u''}], u'game_id': 47, u'project_id': 471, u'id': 306, u'updated_time_ts': 1553769647, u'desc': u''}, {u'en_name': u'operating', u'name': u'\u8fd0\u8425', u'created_time_ts': 1500618901, u'platform_id': 0, u'func_list': [{u'sort': u'2', u'en_name': u'', u'name': u'\u4efb\u52a1\u5ba1\u6838', u'created_time_ts': u'1514355279', u'parent_id': u'0', u'path': u'', u'project_id': u'471', u'type': 0, u'id': u'1201', u'updated_time_ts': u'0', u'desc': u''}, {u'sort': u'1', u'en_name': u'', u'name': u'\u4efb\u52a1\u7ba1\u7406', u'created_time_ts': u'1514355246', u'parent_id': u'0', u'path': u'', u'project_id': u'471', u'type': 0, u'id': u'1200', u'updated_time_ts': u'0', u'desc': u''}, {u'sort': 0, u'en_name': u'', u'name': u'\u5de5\u4f5c\u6d41\u7a0b-\u521b\u5efa\u4efb\u52a1', u'created_time_ts': u'1514355422', u'parent_id': u'1200', u'path': u'/taskmanagetasklist/', u'project_id': u'471', u'type': 1, u'id': u'1206', u'updated_time_ts': u'0', u'desc': u''}, {u'sort': u'1', u'en_name': u'', u'name': u'\u5de5\u4f5c\u6d41\u7a0b-\u65e5\u5fd7\u5217\u8868', u'created_time_ts': u'1514355467', u'parent_id': u'1200', u'path': u'/taskmanageloglist/', u'project_id': u'471', u'type': 1, u'id': u'1208', u'updated_time_ts': u'0', u'desc': u''}, {u'sort': 0, u'en_name': u'', u'name': u'\u5ba1\u6838\u5217\u8868', u'created_time_ts': u'1514355490', u'parent_id': u'1201', u'path': u'/workflowlogworkflowlog/', u'project_id': u'471', u'type': 1, u'id': u'1209', u'updated_time_ts': u'0', u'desc': u''}], u'game_id': 47, u'project_id': 471, u'id': 307, u'updated_time_ts': 1500618901, u'desc': u'\u5929\u68af\u8fd0\u8425\u89d2\u8272'}]
#
# print(type(a))
# def get_role(a):
#     # manager
#     role_list = []
#     for i in a:
#         print(i.get('en_name'))
#         role_list.append(i.get('en_name'))
#
#     if 'manager' in role_list:
#         return 'manager'
#     elif 'operating' in role_list:
#         return 'operating'
#     elif 'user' in role_list:
#         return 'user'
#
#
# print(get_role(a))

import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

objgraph.show_refs([a])