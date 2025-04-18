import src.Xlsx.Xlsx as Xlsx
import src.DatabaseContainer.DatabaseContainer as DBC
import src.utils.utils as util

filename = Xlsx.SearchFilePath_Xlsx()
workbook,sheet = Xlsx.read_Xlsx(filename,"Sheet1")
DBCfile1 = DBC.SearchFilePath_dbc()
db1 = DBC.ReadDBC(DBCfile1)
message_names1 = [message.name for message in db1.messages]
DBCfile2 = DBC.SearchFilePath_dbc()
db2 = DBC.ReadDBC(DBCfile2)
message_names2= [message.name for message in db2.messages]
message_names = message_names1+message_names2

for i in range(2,sheet.max_row+1):
    MessageName = str(sheet.cell(i, 1).value).replace('\n','')
    SignalName = str(sheet.cell(i, 2).value).replace('\n','')
    DataType = str(sheet.cell(i, 3).value).replace('\n','')

    MessageName = util.BestMatchString(MessageName,message_names)
    message1 = DBC.GetMessage(db1,MessageName)
    if message1:

        signal = None
        maxfit = 0
        for sig in message1.signals:
            longest_substring, max_length = util.longest_common_substring(SignalName,sig.name)
            if max_length>maxfit:
                maxfit = max_length
                signal = sig
        signalsampletime = message1.cycle_time
        if DataType == "single":
            signalvaluetable = []
        else:
            signalvaluetable = signal.choices
    else:
        message2 = DBC.GetMessage(db2, MessageName)
        if message2:

            signal = None
            maxfit = 0
            for sig in message2.signals:
                longest_substring, max_length = util.longest_common_substring(SignalName, sig.name)
                if max_length > maxfit:
                    maxfit = max_length
                    signal = sig
            signalsampletime = message2.cycle_time
            signalvaluetable = signal.choices
        else:
            signalsampletime = "Error"
            signalvaluetable = []
            print("MessageName:",MessageName)
    print("SignalName",SignalName,"signalsampletime",signalsampletime)
    print(signalvaluetable)
    print("____________________________________________________________")