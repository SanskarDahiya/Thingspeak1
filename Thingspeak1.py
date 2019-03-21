#getting data from thingspeak
#=================================
"""
chID  = Channel Id
api   = read api key
"""
def retrivedata(chID,api):
    try:
        import json
        from urllib.request import urlopen
        data = "https://api.thingspeak.com/channels/"+chID+"/feeds.json?api_key="+api+"&results=1"
        data = urlopen(data)
        data = json.loads(data.read())
        #get the FEED only
        data = data['feeds']
        #bcoz data is at 0 index
        data = data[0] #give a dict
        #retriving the data
        field=list()
        for x in range(len(data)-2):
            field.append(data['field'+str(x+1)])
        return(field)
    except Exception as e:
        print("Error Found\n    ",e)
        return None

"""
api = Write api key
n = total number of fields


"""

def uploaddata(api,n,*data):
    try:
        import json
        from urllib.request import urlopen
        url = "https://api.thingspeak.com/update?api_key="+api
        for z in range(n):
            url+="&field"+str(z+1)+"="+str(data[z])
        data = urlopen(url)
        print(url)
        data = json.loads(data.read())
        if(data > 0):
            return True
        else:
            return False
    except Exception as e:
        print("Error Found\n    ",e)
        return False
