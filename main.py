import src.Xlsx.Xlsx as Xlsx
import src.DatabaseContainer.DatabaseContainer as DBC
import src.utils.utils as util

filename = Xlsx.SearchFilePath_Xlsx()
workbook,sheet = Xlsx.read_Xlsx(filename,"Sheet1")
# filename1 = Xlsx.SearchFilePath_Xlsx()
# workbook1,sheet1 = Xlsx.read_Xlsx(filename1,"ITS1-FD")
# workbook2,sheet2 = Xlsx.read_Xlsx(filename1,"CHA-FD")
#
# for i in range(2,sheet.max_row+1):
#     SignalName = str(sheet.cell(i, 2).value).replace('\n', '')
#     findflag = 0
#     SignalSymbol = ""
#     for j in range(2,sheet1.max_row+1):
#         SignalName1 = str(sheet1.cell(j, 10).value).replace('\n', '')
#         if(SignalName1 == SignalName):
#             SignalSymbol = str(sheet1.cell(j, 11).value).replace('\n', '')
#             findflag = 1
#             break
#     if findflag == 0:
#         for k in range(2,sheet2.max_row+1):
#             SignalName2 = str(sheet2.cell(k, 10).value).replace('\n', '')
#             if (SignalName2 == SignalName):
#                 SignalSymbol = str(sheet2.cell(k, 11).value).replace('\n', '')
#                 findflag = 1
#
#     sheet.cell(i,4,value=SignalSymbol)
#     print("SignalName",SignalName,"SignalSymbol",SignalSymbol)
#     workbook.save("Step1.xlsx")
# ## DBC ARRGR
DBCfile1 = DBC.SearchFilePath_dbc()
db1 = DBC.ReadDBC(DBCfile1)
message_names1 = [message.name for message in db1.messages]
DBCfile2 = DBC.SearchFilePath_dbc()
db2 = DBC.ReadDBC(DBCfile2)
message_names2= [message.name for message in db2.messages]
message_names = message_names1+message_names2

for i in range(2,sheet.max_row+1):
    MessageName = str(sheet.cell(i, 1).value).replace('\n','')
    SignalName = str(sheet.cell(i, 4).value).replace('\n','')
    DataType = str(sheet.cell(i, 3).value).replace('\n','')

    # MessageName = util.BestMatchString(MessageName,message_names)
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
            BestMatchSignal = signal.name
    else:
        message2 = DBC.GetMessage(db2, MessageName)
        if message2:

            signal = None
            maxfit = 0
            bestlong = ""
            for sig in message2.signals:
                longest_substring, max_length = util.longest_common_substring(SignalName, sig.name)
                if max_length > maxfit:
                    maxfit = max_length
                    bestlong = longest_substring
                    signal = sig
            try:
                signalsampletime = message2.cycle_time
                signalvaluetable = signal.choices
                BestMatchSignal = signal.name
            except Exception as e:
                print("ERRORERROR")
                print("MessageName:",MessageName,"SignalName",SignalName,"BestMatchSignal",bestlong)

        else:
            signalsampletime = "Error"
            signalvaluetable = []
            BestMatchSignal = "Fail"
            print("MessageName:",MessageName)
    # sheet.cell(i,5,value=signalsampletime)
    # sheet.cell(i, 6, value=)
    print("SignalName",SignalName,"BestMatchSignal",BestMatchSignal,"signalsampletime",signalsampletime)
    print(signalvaluetable)
    print("____________________________________________________________")