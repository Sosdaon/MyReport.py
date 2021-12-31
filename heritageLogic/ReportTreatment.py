class Passport:
    def __init__(self, objects_list=[], pasport_num=0, obj_name='ім\'я', invent_num='інвентарний номер',
                 execute_restorer='Ім\'я виконавця реставрації', time='час створення', material='матеріал'):
        self.__objects_list = objects_list
        self.__pasport_num = pasport_num
        self.__obj_name = obj_name
        self.__invent_num = invent_num
        self.__execute_restorer = execute_restorer
        self.__time = time
        self.__material = material

    def set_name(self, obj_name):
        self.__obj_name = obj_name
        self.__objects_list.append(obj_name)
        self.__pasport_num = len(self.__objects_list)

    def set_invent_num(self, invent_num):
        self.__invent_num = invent_num

    def set_execute_restorer(self, execute_restorer):
        self.__execute_restorer = execute_restorer

    def set_time(self, time):
        self.__time = time

    def set_material(self, material):
        self.__material = material

    def get_name(self):
        return self.__obj_name

    def get_invent_num(self):
        return self.__invent_num

    def get_execute_restorer(self):
        return self.__execute_restorer

    def get_time(self):
        return self.__time

    def get_material(self):
        return self.__material

    def get_mylist(self):
        return self.__objects_list

    def get_pasport_num(self):
        return self.__pasport_num