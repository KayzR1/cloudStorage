import dropbox

class TransferData:
    def _init_(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.BA62UxJT5txvGvEEbKyCWTxq8tJjpWJH6iWX1iN37Y1AXU_Dmxlr78A_2o8rJLRuFKyNINgHEyysHAscFdnG8a43eHrNnxKdlYOeSdOcZudZdyTvvhaJm1n-OXN372g6GaWMCa4'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer")
    file_to = input("Enter full path to upload to dropbox")
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()