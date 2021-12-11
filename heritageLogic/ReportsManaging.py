from ReportTreatment import Passport


class RegisterBook(Passport):
    def __init__(self, mylist=[], pasport_num=0, obj_name='ім\'я', invent_num='інвентарний номер',
                 execute_restorer='Ім\'я виконавця реставрації', time='час створення', material='матеріал',
                 outputReportNum='empty', outputReportDate='date'):
        Passport.__init__(self, mylist, pasport_num, obj_name, invent_num,
                          execute_restorer, time, material)
        self.__outputReportNum = outputReportNum
        self.__outputReportDate = outputReportDate

    def set_outputReport(self, outputReportNum, outputReportDate):
        self.__outputReportNum = outputReportNum
        self.__outputReportDate = outputReportDate

    def get_outputReport(self):
        return self.__outputReportNum, self.__outputReportDate

