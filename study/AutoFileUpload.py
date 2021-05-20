# from simple_salesforce import Salesforce
from simple_salesforce import Salesforce, format_soql
import os
import json
import requests

global industry_list
def salesforceCon():
    sf = Salesforce(username='deokjun.kim@lgcpartner.com.test', password='ejrwns48', security_token="", domain="test")
    print("session Id : " + sf.session_id)
    return sf

def getHierarchy(sf):
    response = sf.query("SELECT Industry__r.Name, Detail_Industry__r.Name, Application__c, Application__r.Name, Id, Name FROM LG_Part__c where id = Null")
    print(response)
    print(response["records"])

    industry = {}
    for record in response["records"]:

        Industry_Name = record["Industry__r"]["Name"]
        Detail_Industry_Name = record["Detail_Industry__r"]["Name"]
        Application = record["Application__c"]
        Application_Name = record["Application__r"]["Name"]
        Part = record["Id"]
        Part_Name = record["Name"]

        if industry.get(Industry_Name) == None:
            industry[Industry_Name] = {
                Detail_Industry_Name: {
                    Application_Name: {
                        "Id": Application,
                        Part_Name: {
                            "Id": Part
                        }
                    }
                }
            }

        elif industry.get(Industry_Name).get(Detail_Industry_Name) == None:
            industry[Industry_Name][Detail_Industry_Name] = {
                Application_Name: {
                    "Id": Application,
                    Part_Name: {
                        "Id": Part
                    }
                }
            }
        elif industry.get(Industry_Name).get(Detail_Industry_Name).get(Application_Name) == None:
            industry[Industry_Name][Detail_Industry_Name][Application_Name] = {
                "Id": Application,
                Part_Name: {
                    "Id": Part
                }
            }
        elif industry.get(Industry_Name).get(Detail_Industry_Name).get(Application_Name).get(Part_Name) == None:
            industry[Industry_Name][Detail_Industry_Name][Application_Name][Part_Name] = {"Id":Part}

    return industry
def upload3(sf, hierarchy):
    # data = [{
    #     'LinkedEntityId': 'a0H1s000003kaHCEAY',
    #     'ContentDocumentId': '0691s000000kDaiAAE',
    # }]
    # sf.bulk.Contact.insert(data,batch_size=10000,use_serial=True)
    sf.Contact.insert({
        'LinkedEntityId': 'a0H1s000003kaHCEAY',
        'ContentDocumentId': '0691s000000kCZ6AAM',
    })
    # data = [
    #     {'ContentDocumentId': '0691s000000kCZ6AAM', 'LinkedEntityId': 'a0H1s000003kaHCEAY'}
    # ]
    #
    # sf.bulk.Contact.insert(data, batch_size=10000, use_serial=True)

def upload2(sf, hierarchy):
    response = sf.query(
        format_soql("SELECT Id,ContentDocumentId,Title from ContentVersion WHERE OwnerID = {}", "0051s000001DWDpAAO"))
    # data = []
    count = 0
    for record in response["records"]:
        industry = record["Title"].split('_')[1]
        dindustry = record["Title"].split('_')[2]
        applicaiotn = record["Title"].split('_')[3]
        part = record["Title"].split('_')[4]
        data = {
            'LinkedEntityId': hierarchy[industry][dindustry][applicaiotn][part]["Id"],
            'ContentDocumentId': record["ContentDocumentId"],
        }
        print(hierarchy[industry][dindustry][applicaiotn][part]["Id"],record["ContentDocumentId"])
        # print('ContentDocumentLink dl' + str(count) +'= new ContentDocumentLink();')
        # print('dl'+str(count)+'.LinkedEntityId = \''+ hierarchy[industry][dindustry][applicaiotn][part]["Id"]+'\';')
        # print('dl'+str(count)+'.ContentDocumentId = \'' + record["ContentDocumentId"]+'\';')
        # print('dlList.add(dl'+str(count)+');')
        # count +=1
        # sf.bulk.ContentDocumentLink.insert(data, batch_size=1000)
        # print(data)
    # ContentDocumentLink
    # dl = new
    # ContentDocumentLink();
    # dl.LinkedEntityId = 'a0H1s000003kaHCEAY';
    # dl.ContentDocumentId = '0691s000000kCZ6AAM';
    # dlList.add(dl);


    # for d in data:
    #     print(d)

def uploade(sf,cvidList,ContentVersion):
    print('=== bulk uploade ===')
    data = []
    response = sf.query(
        format_soql("SELECT Id, ContentDocumentId from ContentVersion WHERE Id IN {idList}", idList=cvidList))

    for record in response["records"]:
        data.append({
            'LinkedEntityId': ContentVersion[record["Id"]],
            'ContentDocumentId': record["ContentDocumentId"]
        }
        )
    print(data)
    sf.bulk.ContentDocumentLink.insert(data, batch_size=100, use_serial=True)

def searchDirectory(hierarchy):
    # PNG
    folderName = 'part'
    path_dir = '/Users/deokjunekim/Downloads/' + folderName

    forder_list = os.listdir(path_dir)
    # 기본 폴더
    # upload 구조
    """
    {
        Name,
        Id,
        Path   
    }
    """
    linkMap ={}
    uploadFileList = []
    # for forder in forder_list:
    #     if forder != ".DS_Store":
    #         print('Forder : ' + forder)
    #
    #         id_forder_list = os.listdir(path_dir + '/' + forder)
    #         # Industry 폴더
    #         for id_forder in id_forder_list:
    #             if id_forder != ".DS_Store":
    #                 print(' Industry : ' + id_forder)
    #                 # industry = id_forder.split('_')[1]
    #                 ap_forder_list = os.listdir(path_dir + '/' + forder + '/' + id_forder)
    #
    #                 # Application 폴더
    #                 for ap_forder in ap_forder_list:
    #                     if ap_forder != ".DS_Store":
    #                         print('      Sub-Industry: ' + ap_forder)
    #                         # dindustry = ap_forder.split('_')[1]
    #                         pt_forder_list = os.listdir(path_dir + '/' + forder + '/' + id_forder + '/' + ap_forder)
    #
    #                         # Part 폴더
    #                         for pt_forder in pt_forder_list:
    #                             if pt_forder != ".DS_Store":
    #                                 print('         Application : ' + pt_forder)
    #                                 # applicaiotn = pt_forder.split('_')[1]
    #                                 file_list = os.listdir(path_dir + '/' + forder + '/' + id_forder + '/' + ap_forder + '/' + pt_forder)
    #                                 print('         ' + str(file_list))
    #                                 # File 폴더
    #                                 for file in file_list:
    #                                     if file != ".DS_Store":
    #                                         industry = file.split('_')[1]
    #                                         dindustry = file.split('_')[2]
    #                                         applicaiotn = file.split('_')[3]
    #                                         part = file.split('_')[4]
    #                                         print('         '+path_dir + '/' + forder + '/' + id_forder + '/' + ap_forder + '/' + pt_forder + '/' + file )
    #
    #                                         uploadFileList.append({
    #                                             "Title" : file,
    #                                             "PathOnClient" : path_dir + '/' + forder + '/' + id_forder + '/' + ap_forder + '/' + pt_forder + '/' + file,
    #                                             # "Id" : hierarchy[industry][dindustry][applicaiotn][part]["Id"]
    #                                         })
    #                                         linkMap[file] = hierarchy[industry][dindustry][applicaiotn][part]["Id"]
    #                                         print(hierarchy[industry][dindustry][applicaiotn][part]["Id"])
    file_list = os.listdir(path_dir)
    for file in file_list:
        if file != ".DS_Store":
            industry = file.split('_')[1]
            dindustry = file.split('_')[2]
            applicaiotn = file.split('_')[3]
            part = file.split('_')[4]
            print('         '+path_dir + '/' + file )

            uploadFileList.append({
                "Title" : file,
                "PathOnClient" : path_dir + '/' + file,
                # "Id" : hierarchy[industry][dindustry][applicaiotn][part]["Id"]
            })
            linkMap[file] = hierarchy[industry][dindustry][applicaiotn][part]["Id"]
            print(hierarchy[industry][dindustry][applicaiotn][part]["Id"])

    # print(uploadFileList[0])
    print(forder_list)
    return uploadFileList, linkMap

def file_uplode(sf, uploadFileList,linkMap):
    print('=== file upload ===')
    sessionId = sf.session_id
    cvidList =[]
    ContentVersion ={}
    # count = 0
    for upladFile in uploadFileList:
        entity = upladFile
        print(entity)
        files = {
            'entity_content': (None, json.dumps(entity), 'application/json'),
            'VersionData': (os.path.basename(upladFile.get('PathOnClient')),
                            open(upladFile.get('PathOnClient'), 'rb'), 'application/octet-stream')
        }
        response = requests.post('https://lgchem1--test.my.salesforce.com/services/data/v51.0/sobjects/ContentVersion',
                                 headers={'Authorization': 'Bearer %s' % sessionId},
                                 files=files
                                 )
        ContentVersion[response.json().get('id')] = linkMap.get(entity["Title"])

        # ContentVersion = {
        #     "ContentDocumentId" : response.json().get('id'),
        #     "LinkedEntityId" : linkMap.get(entity["Title"])
        #
        # }
        cvidList.append(response.json().get('id'))
        # count += 1
        #
        # if count > 10:
        #     break

    uploade(sf, cvidList, ContentVersion)


sf = salesforceCon()
industry = getHierarchy(sf)
# upload3(sf, '')
# upload2(sf, industry)
# uploadFileList, linkMRap = searchDirectory(industry)
# file_uplode(sf, uploadFileList, linkMap)

"""
    Application 2-Dept
    Industry - Application
    SELECT Industry__c FROM Application__c Group by Name
"""

"""
    Part 3-Dept
    Industry - Application - Part
    
"""
