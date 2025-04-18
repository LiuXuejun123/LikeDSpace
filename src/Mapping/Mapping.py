class MappingRowConfig:
    def __init__(self):
        self.MessageName = 15
        self.SignalName = 16
        self.Basetype = 11
class Signal:
    def __init__(self):
        self.SignalName = ""
        self.MessageName = ""
        self.BaseType = ""
    def display(self):
        print("==============================")
        print("SignalName:",self.SignalName)
        print("MessageName:",self.MessageName)
        print("BaseType",self.BaseType)
def GetMappingSignal(sheet,RowConfig:MappingRowConfig):
    max_row = sheet.max_row
    MappingSignalDict = []
    for i in range(2, max_row + 1):
        MessageName = str(sheet.cell(i, RowConfig.MessageName).value)# 报文名称
        SignalName = str(sheet.cell(i, RowConfig.SignalName).value)  # 信号名称
        SignalBaseType = str(sheet.cell(i, RowConfig.Basetype).value)  # datatype
        if MessageName != 'None' and SignalName != 'None' and SignalBaseType != 'None':
            TempValue = Signal()
            TempValue.MessageName = MessageName
            TempValue.SignalName = SignalName
            TempValue.BaseType = SignalBaseType
            MappingSignalDict.append(TempValue)
    return MappingSignalDict

