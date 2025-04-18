import src.Xlsx.Xlsx as Xlsx
import src.SignalBuilder.SignalBuilder as SignalBuilder
import src.Mapping.Mapping as Mapping

filename = Xlsx.SearchFilePath_Xlsx()
workbook,sheet = Xlsx.read_Xlsx(filename,"InputMapping")
MappingRowConfig = Mapping.MappingRowConfig()
MappingSignalDict = Mapping.GetMappingSignal(sheet,MappingRowConfig)
for i in MappingSignalDict:
    i.display()