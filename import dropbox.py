import dropbox

class TransferData:
    os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])

    import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

      for root, dirs files in os.walk(file_from):

          relative_path = os.path.relpath(local_path, file_from)
          dropbox_path = os.path.join(file_to, relative_path)

      def __init__(self, access_token):
        self.access_token = access_token

      def upload_file(self, file_from, file_to): 
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite') file_to)

def main():
    access_token = 'sl.BCE-0YuNCtZ5ncb_3rB1EWTZm0mS-vvK311-5dLLGhCeSWj1IOP8Tnqh_9otXNQSE7NeRxAdIO3D1hCbl8F86RWLyx3Loxt2Uwu-WiXlAQpZ_00bc7yaSucTVuXHvGKeg7HFBbU'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full part to upload to dropbox: ")
    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")
    main()