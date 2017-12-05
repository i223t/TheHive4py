from thehive4py.api import TheHiveApi


thehive = TheHiveApi('http://127.0.0.1:9000', 'username', 'password', {'http': '', 'https': ''})
case = thehive.case('AV9HwCaG4umMow4Mjd_n')
case._thehive = thehive
for task in case.tasks:
    print(task.title)