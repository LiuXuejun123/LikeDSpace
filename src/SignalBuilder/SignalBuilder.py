class Signal:
    def __init__(self):
        self.SignalName = ""
        self.MessageName = ""
        self.SignalCycle = 0.01
        self.SignalUnit = ""
        self.SignalRange = (0,100)
        self.SignalCoding = []
    def display(self):
        print("SignalName:",self.SignalName)
        print("MessageName:",self.MessageName)
class SignalRowConfig:
    def __init__(self):
        self.MessageName = 8
        self.SignalName = 9
        self.SignalCycle = 10
        self.SignalUnit = 11
        self.Codingdefine = 12
def GetVeh2FuncSignal(sheet,sheet_row_config:SignalRowConfig):
    Veh2FuncSiganlDict = []
    max_row = sheet.max_row
    for i in range(2,max_row+1):
        MessageName =  str(sheet.cell(i, sheet_row_config.MessageName).value)# 报文名称
        SignalName = str(sheet.cell(i, sheet_row_config.SignalName).value) # 信号名称
        SignalCycle = str(sheet.cell(i, sheet_row_config.SignalCycle).value)#cycle
        SignalUnit = str(sheet.cell(i, sheet_row_config.SignalUnit).value)# unit
        signalCodingDefine =  str(sheet.cell(i, sheet_row_config.Codingdefine).value)
        print(SignalName)
        print(signalCodingDefine)













