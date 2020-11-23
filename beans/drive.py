import dropbox
import base64

class Dpx:
    def __init__(self):
        with open('beans/secret.key','r') as key:
            # YOUR_ACCESS_TOKEN on beans/secret.key archive
            self.dbx = dropbox.Dropbox(key.read())
        self.dbx.users_get_current_account()

    def listEntries(self):
        try:
            return [e.name for e in self.dbx.files_list_folder('').entries]
        except Exception as e:
            print(e)
            return []
    
    def upload(self,file,meta, base = False):
        try:
            if base:
                r = self.dbx.files_upload(base64.b64decode(file), "/%s" % meta)
            else:
                r = self.dbx.files_upload(file, "/%s" % meta)
            return r.id
        except Exception as e:
            print(e)
            return False
        
    def delete(self, filename):
        try:
            self.dbx.files_delete("/%s" % filename)
            return True
        except Exception as e:
            print(e)
            return False
    
    def download(self,filename, filedestination):
        try:
            with open(filedestination, "wb") as f:
                metadata, res = self.dbx.files_download(path="/%s" % filename)
                f.write(res.content)
                return metadata.name
        except Exception as e:
            print(e)
            return False