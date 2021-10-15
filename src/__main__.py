from exception import AudioRecordException
from utils import record, read_text

filePath = record()
try:
  text = read_text(filePath=filePath)
  print(text)
except AudioRecordException as ex:
  print(ex)

