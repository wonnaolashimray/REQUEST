import requests
import json
def request():
    a=requests.get("http://saral.navgurukul.org/api/courses")
    x=a.json()
    print("No.of Course---- Id")
    with open("Link1.json","w") as f:
        json.dump(x,f,indent=4)
    with open("Link1.json","r") as f:
        data=json.load(f)
        # print(data)
    l=[]
    i=0
    while i<len(data['availableCourses']):
        print(i+1,":",data['availableCourses'][i]['name'],"------",data['availableCourses'][i]['id'])
        l.append(data['availableCourses'][i]['id'])
        i+=1
    user= int(input("**select the serial number  :"))-1
    ex=requests.get("http://saral.navgurukul.org/api/courses/"+l[user]+"/exercises")
    a=ex.json()
    with open("link2.json","w")as k:
        json.dump(a,k,indent=4)
    with open("link2.json","r")as k:
        c=json.load(k)
        # print(c)
    j=0  
    k=0
    slug=[]
    while j<len(c['data']):
        print(k+1,c['data'][j]['name'])
        slug.append(c['data'][j]['slug'])
        j+=1
        k+=1
    # print(slug)
    slugname=int(input("enter the slug name   :"))-1
    sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
    b=sluglist.json()
    with open("Link3.json","w") as p:
        json.dump(b,p,indent=4)
    with open("Link3.json","r") as p:
        f=json.load(p)
    s=f["name"]
    t=f["content"]
    print(s)
    print(t)
    for index in range(len(slug)):
        pre_next=input("enter n/p: ")
        if pre_next=="n":
            user2=user2+1
            if pre_next<str(len(slug)):
                request()
            else:
                print("content does not exist ")
         # break
        elif pre_next=="p":
            user2=user2-1
            if pre_next>=str(len(slug)):
                request()
            else:
                print("content does not exist")
                break
        else:
            print("exit") 	
request()
        
