'''Hey I am =ODST=
   This is meant for judicial purpose like research and studies.
   It is still in development.
   [1]. How it works:
        [a]. search the specific document on web 
        [b]. copy the link and put the link in the search bar and click on search button 
        [c]. it will analyze the document and find all the Sections specified in the document
        [d]. Then the whole article will appear in 'Analyzed article' section and the laws specified in the 'Law' section
'''

from newspaper import Article
import requests
from bs4 import BeautifulSoup
from tkinter import *
from PIL import ImageTk,Image
import os
#backend function
def analyze():
     url=searchvar.get()
     article=Article(url,language="en")
     article.download()
     article.parse()
     content = article.text
     output.insert(INSERT,content)
     arr=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','29A','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','52A','53','53A','54','55','55A','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','120A','120B','121','122','123','124','125','126','127','128','129','130','131','132','133','134','135','136','137','138','138A','139','140','141','142','143','144','145','146','147','148','149','150','151','152','153','153A','153AA','153B','154','155','156','157','158','159','160','161','162','163','164','165','165A','166','166A','166B','167','168','169','170','171','171','171A','171B','171C','171D','171F','171G','171H','171I','172','173','174','174A','175','176','177','178','179','180','181','182','183','184','185','186','187','188','189','190','191','192','193','194','195','196','197','198','199','200','201','202','203','204','205','206','207','208','209','210','211','212','213','214','215','216','216A','216B','217','218','219','220','221','222','223','224','225','225A','225B','226','227','228','228A','229','229A','230','231','232','233','234','235','236','237','238','239','240','241','242','243','244','245','246','247','248','249','250','251','252','253','254','255','256','257','258','259','260','261','262','263','264','265','266','267','268','269','270','271','272','273','274','275','276','277','278','279','280','281','282','283','284','285','286','287','288','289','290','291','292','293','294','294A','295','295A','296','297','298','299','300','301','302','303','304','304A','304B','305','306','307','308','309','310','311','312','313','314','315','316','317','318','319','320','321','322','323','324','325','326','326A','326B','327','328','329','330','331','332','333','334','335','336','337','338','339','340','341','342','343','344','345','346','347','348','349','350','351','352','353','354','354A','354B','354C','354D','355','356','357','358','359','360','361','362','363','364','364A','365','366','367','368','369','370','371','372','373','374','375','376','376A','376B','376C','376D','376DA','376DB','377','378','379','380','381','382','383','384','385','386','387','388','389','390','391','392','393','394','395','396','397','398','399','400','401','402','403','404','405','406','407','408','409','410','411','412','413','414','415','416','417','418','419','420','421','422','423','424','425','426','427','428','429','430','431','432','433','434','435','436','437','438','439','440','441','442','443','444','445','446','447','448','449','450','451','452','453','454','455','456','457','458','459','460','461','462','463','464','465','466','467','468','469','470','471','472','473','474','475','476','477','477A','478','479','480','481','482','483','484','485','486','487','488','489',"489A","489B","489C","489D","489E",'490','491','492','493','494','495','496','497','498','498A','499','500','501','502','503','504','505','506','507','508','509','510']
     for j in range(len(arr)):
         if ("Section %s "%arr[j] in content) or ("Sections %s "%arr[j] in content):
             url=requests.get("https://devgan.in/index.php?q=%s&a=1"%arr[j])
             info=BeautifulSoup(url.content,"html.parser")
             header=info.find("tr",class_="mys-head")
             des=info.find("tr",class_="mys-desc")
             lawinfo.insert(INSERT,"\n\n========================\nTITLE:\n"+header.text+"\n\n")
             lawinfo.insert(INSERT,"DESCRIPTION:\n"+des.text)

def home():
    root.destroy()
    os.system('main.py')           
     
#GUI
root=Tk()
root.title("Samvidhan_Online")
root.geometry("800x700")
root.configure(background='#b5d9f7')

logoimage=PhotoImage(file='logo.png')
icon=Label(image=logoimage)
icon.place(x=200,y=30,width=391,height=131)

searchvar= StringVar()
searchentry=Entry(root,textvariable=searchvar,width=100,highlightthickness=0,relief='solid',font=('Bahnschrift SemiBold',12),bg='#f5f8fa')
searchentry.place(x=193,y=180,width=420,height=30)

search=Image.open("search.png")
re_image=search.resize((50,50))
searchimage=ImageTk.PhotoImage(re_image)
searchbutton=Button(root,image=searchimage,borderwidth=0,bg='#b5d9f7',activebackground='#b5d9f7',command=analyze)
searchbutton.place(x=620,y=170)

Label(root,text='Analyzed Article:',font=("Cascadia Mono SemiBold",8,'bold')).place(x=10,y=230)

output=Text(root,wrap=WORD,bg='#f5f8fa',fg='black',relief='solid',font=("Arial",11))
output.place(x=10,y=250,height=420,width=510)

Label(root,text="Law:",font=("Cascadia Mono SemiBold",8,'bold')).place(x=530,y=230)

lawinfo=Text(root,wrap=WORD,bg='#f5f8fa',fg='black',relief='solid',font=('Arial',11))
lawinfo.place(x=530,y=250,height=420,width=250)

back=Button(root,text='BACK',width=10,relief='solid',bg='black',fg='white',command=home)
back.place(x=700,y=670)

root.resizable(False,False)
root.mainloop()
