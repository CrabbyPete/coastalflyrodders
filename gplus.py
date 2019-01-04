from gspread import Client


class ClientPlus( Client ):
    """
    Create a new class which adds the get_all_files function 
    to the Client
    """
    
    def get_all_files(self):
        files = []
        page_token = ''
        url = "https://www.googleapis.com/drive/v3/files"
        params = {
            'corpora':['user', 'domain'], 
            "pageSize": 1000,
            'supportsTeamDrives': True,
            'includeTeamDriveItems': True,
        }

        while page_token is not None:
            if page_token:
                params['pageToken'] = page_token

            res = self.request('get', url, params=params).json()
            files.extend(res['files'])
            page_token = res.get('nextPageToken', None)

        return files

    def get_file_id( self, file_name ):
        url = "https://www.googleapis.com/drive/v3/files"
        
        params = {
            'q': "name ='{}'".format(file_name),
            'corpora':['user', 'domain'], 
            "pageSize": 1000,
            'supportsTeamDrives': True,
            'includeTeamDriveItems': True,
        }

        res = self.request('get', url, params=params).json()
        try:
            for fyl in res['files']:
                if 'id' in fyl:
                    return fyl['id']
        except:
            pass
        
        return None
        
        

        