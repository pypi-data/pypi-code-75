import sys
import os
import pickle
import json

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request 
from googleapiclient.discovery import build

from sync_dl import config as cfg



# Any attempt to modify this script will result in sync-dl no longer being able to decrypt the client api key.
# This is by design, to prevent the api key from being stolen.

from ntpath import dirname
ytapiModulePath = dirname(__file__)

def newCredentials(scopes,credPath):
    trace = sys.gettrace()

    if trace is not None:
        #debugger is on, not getting flow
        return None
    
    try: # obfuscated code is platform dependant, it may not work on some platforms
        from sync_dl_ytapi.encrypted import getDecryptedProxy,encryptFileProxy, encryptBytesProxy
    except:
        cfg.logger.error("Unable to Load Obfuscated Code on This Platform (required to use youtube api)")
        return None

    clientSecretsEncrypted = f'{ytapiModulePath}/encrypted/encrypted_client_secrets'

    decrypted = getDecryptedProxy(clientSecretsEncrypted).decode('utf8')

    clientConfig = json.loads(decrypted)

    flow = InstalledAppFlow.from_client_config(clientConfig,scopes=scopes)

    prompt = '\nMake sure you are using sync-dl which you Installed via pip.\nIf not, then this api key may be stolen!\n\nTerms of Service can be found here: http://sync-dl.com/licence \n\nPrivacy Policy can be found here: http://sync-dl.com/privacy-policy/ \n\nAuthentificate at:\n{url}'
    # start local server on localhost, port 8080
    flow.run_local_server(prompt = 'consent', authorization_prompt_message=prompt,open_browser=False)


    credentials = flow.credentials

    if os.path.exists(credPath):
        os.remove(credPath)
    with open(credPath,"wb") as f:
        f.write(encryptBytesProxy(pickle.dumps(credentials)))

    cfg.logger.info("Authentification Completed!")
    return credentials


def getCredentials():
    trace = sys.gettrace()

    if trace is not None:
        #debugger is on, not getting flow
        return None

    try: # obfuscated code is platform dependant, it may not work on some platforms
        from sync_dl_ytapi.encrypted import getDecryptedProxy,encryptFileProxy, encryptBytesProxy
    except:
        cfg.logger.error("Unable to Load Obfuscated Code on This Platform (required to use youtube api)")
        return None
    
    credPath = f'{ytapiModulePath}/credentials'
    scopes = ['https://www.googleapis.com/auth/youtubepartner']

    
    if os.path.exists(credPath):
        
        credentials = pickle.loads(getDecryptedProxy(credPath))
        

        if credentials.refresh_token:
            if credentials.expired:
                credentials.refresh(Request())
        else:
            credentials = newCredentials(scopes,credPath)

    else:
        credentials=newCredentials(scopes,credPath)
    
    return credentials

def getYTResource():    
    credentials = getCredentials()
    youtube = build('youtube', 'v3', credentials=credentials)
    return youtube