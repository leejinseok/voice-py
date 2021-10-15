from exception import AudioRecordException
from utils import record, read_text

filePath = record()

try:
  read_text(filePath=filePath)
except AudioRecordException as ex:
  print(ex)

