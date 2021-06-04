# from simple_salesforce import Salesforce
from simple_salesforce import Salesforce, format_soql
import os
import json
import requests

global industry_list
folderName = '업종_Mai'

def salesforceCon():
    sf = Salesforce(username='ohjong@lgcpartner.com', password='password123', security_token="")
    print("session Id : " + sf.session_id)
    return sf

def getHierarchy(sf):
    response = sf.query("SELECT Industry__r.Name, Detail_Industry__r.Name, Detail_Industry__c, Application__c, Application__r.Name, Id, Name FROM LG_Part__c")
    print(response)
    print(response["records"])

    industry = {}
    for record in response["records"]:

        Industry_Name = record["Industry__r"]["Name"]
        Detail_Industry_Name = record["Detail_Industry__r"]["Name"]
        Detail_Industry = record["Detail_Industry__c"]
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
                    , "Id" : Detail_Industry
                }
            }

        elif industry.get(Industry_Name).get(Detail_Industry_Name) == None:
            industry[Industry_Name][Detail_Industry_Name] = {
                Application_Name: {
                    "Id": Application,
                    Part_Name: {
                        "Id": Part
                    }
                },
                "Id" : Detail_Industry
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
            'ContentDocumentId': record["ContentDocumentId"],
            'Visibility':'AllUsers'
        }
        )
    print(data)
    sf.bulk.ContentDocumentLink.insert(data, batch_size=10, use_serial=True)

def searchDirectory(hierarchy):
    # PNG

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
            print('         ' + path_dir + '/' + file)
            file = file.split('.')[0]

            industry = file.split('_')[1]
            dindustry = file.split('_')[2]
            applicaiotn = file.split('_')[3]

            uploadFileList.append({
                "Title": file,
                "PathOnClient": file + '.png'
            })

            if len(file.split('_')) > 4:
                part = file.split('_')[4]

                # print(file.split('_')[-1])
                if file.split('_')[-1] != 'AppEmpty' and file.split('_')[-1] != 'Hover':
                    linkMap[file] = hierarchy[industry][dindustry][applicaiotn][part]["Id"]
                    print(hierarchy[industry][dindustry][applicaiotn][part]["Id"])
                else:
                    linkMap[file] = hierarchy[industry][dindustry][applicaiotn]["Id"]
                    # print(industry, dindustry, applicaiotn, part)
                    # print('         ' + path_dir + '/' + file)
                    # print('empty', file)
                    print(hierarchy[industry][dindustry][applicaiotn]["Id"])
            else:
                linkMap[file] = hierarchy[industry][dindustry]["Id"]
                print(hierarchy[industry][dindustry]["Id"])





    # print(uploadFileList[0])
    print('fl',forder_list)
    return uploadFileList, linkMap


def file_uplode(sf, uploadFileList,linkMap):
    print('=== file upload ===')
    sessionId = sf.session_id
    cvidList =[]
    ContentVersion ={}

    path_dir = '/Users/deokjunekim/Downloads/' + folderName

    for upladFile in uploadFileList:
        entity = upladFile
        print(entity)
        files = {
            'entity_content': (None, json.dumps(entity), 'application/json'),
            'VersionData': (os.path.basename(path_dir + '/' + upladFile.get('PathOnClient')),
                            open(path_dir + '/' +upladFile.get('PathOnClient'), 'rb'), 'application/octet-stream')
        }
        response = requests.post('https://lgchem.my.salesforce.com/services/data/v51.0/sobjects/ContentVersion',
                                 headers={'Authorization': 'Bearer %s' % sessionId},
                                 files=files
                                 )
        # print(type(linkMap))
        # print(response.content)
        ContentVersion[response.json().get('id')] = linkMap.get(entity["Title"])

        cvidList.append(response.json().get('id'))

    uploade(sf, cvidList, ContentVersion)

def search_documentLink(linkMap):
    linkList = list(linkMap.values())
    sf = salesforceCon()
    cdIdList = []
    response_cv = sf.query(
        format_soql("SELECT Id, LinkedEntityId, ContentDocumentId FROM ContentDocumentLink where LinkedEntityId IN {idList}", idList=linkList))

    for record in response_cv["records"]:
        cdIdList.append(record["ContentDocumentId"])

    response_cd = sf.query(
        format_soql("SELECT Id, Title from ContentDocument WHERE Id IN {idList}", idList=cdIdList))

    delIdList = []
    c = 0
    for record in response_cd["records"]:
        if linkMap.get(record["Title"]) != None:
            print(linkMap.get(record["Title"]), record["Title"])
            # linkMap.pop(record["Title"])
            delIdList.append({'Id':record["Id"]})
        elif linkMap.get(record["Title"].split('.')[0]) != None:
            print(linkMap.get(record["Title"].split('.')[0]), record["Title"])
            # linkMap.pop(record["Title"].split('.')[0])
            delIdList.append({'Id':record["Id"]})
        # elif record["Title"].split('_')[-1] == 'Hover' :
        #     c +=1
        #     print(record["Title"])
    # print(c)
        # elif record["Title"].split('_')[-1] == 'Active' or record["Title"].split('_')[-1] == 'AppEmpty':
        #     print(record["Id"], record["Title"])
        #     delIdList.append({'Id': record["Id"]})
            # for key in linkMap:
            #     if key.split('_')[-2] == record["Title"].split('_')[0] or key.split('_')[-3] == record["Title"].split('_')[0]:
            #         a = 0
            #         delIdList.append({'Id': record["Id"]})
            #         print(key)
            #         # linkMap.pop(key)
            #         break
            # print()

        # print(linkMap)
        # elif record["Title"].find('Btn') != -1 and record["Title"].find('Active') == -1:
        #     print(record["Title"].split('_')[6])
        #     tMap[record["Title"].split('_')[6]] = record["Id"]
            # print(record["Title"], record["Id"])

    # INDUSTRIES_Electrical & Electronics_Security_Security Alarm_Housing_Active.png

    # for i in tMap.keys():
    #     print(tMap.get(i))
    # print(delIdList)
    # print(len(delIdList), len(linkMap.keys()))
    # print(linkMap)
    print(delIdList)

    sf.bulk.ContentDocument.delete(delIdList, batch_size=100, use_serial=True)



# Salesforce Session 가져오기
sf = salesforceCon()

# Salesforce Application 구조 가져오기
industry = getHierarchy(sf)

# 다운로드 받은 파일 id 매핑
uploadFileList, linkMRap = searchDirectory(industry)

# 업로드 진행할 파일이 존재 시 파일 삭제
# search_documentLink(linkMRap)

# ContentVersion 파일 업로드
file_uplode(sf, uploadFileList, linkMRap)

"""
    Application 2-Dept
    Industry - Application
    SELECT Industry__c FROM Application__c Group by Name
"""

"""
    Part 3-Dept
    Industry - Application - Part
    
"""
