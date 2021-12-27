from django.http import response ,HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from pymysql import NULL
from .import pool
import pdfkit
import io

data = {'firstname':NULL,'lname':NULL,'jtitle':NULL,'dp':NULL,'address':NULL,'city':NULL,'state':NULL,'phone':NULL,'email':NULL,'github':NULL,'linkedin':NULL,'skill':NULL,'school_name':NULL,'class10':NULL,'class12':NULL,'Collage_Name':NULL,'collage_CGPA':NULL,'about_me':NULL,'CompanyName':NULL,'Company_summary':NULL,'Tproject':NULL,'Dproject':NULL}

       


def main(request):
     return render (request, 'resume.html',{'msg':''})

def submitdata(request):
    
    try :
        # print("hello")
        firstname=request.POST['fname']
        lname=request.POST['lname']
        jtitle=request.POST['jtitle']
        # print("hello2")
        dp=request.FILES['dp']
        # print("hello3")
        address=request.POST["address"]
        city=request.POST["city"]
        state=request.POST["state"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        github=request.POST["github"]
        linkedin=request.POST["linkedin"]
        school_name=request.POST["school_name"]
        class10= request.POST['class10']
        class12= request.POST['class12']
        Collage_Name=request.POST["Collage_Name"]
        collage_CGPA=request.POST["collage_CGPA"]
        skill=request.POST["skill"]
        about_me=request.POST["about_me"]
        CompanyName=request.POST["CompanyName"]
        Company_summary=request.POST["Company_summary"]
        Tproject=request.POST["Tproject"]
        Dproject=request.POST["Dproject"]
        global data

        data = {'firstname':firstname,'lname':lname,'jtitle':jtitle,'dp':dp.name,'address':address,'city':city,'state':state,'phone':phone,'email':email,'github':github,'linkedin':linkedin,'skill':skill,'school_name':school_name,'class10':class10,'class12':class12,'Collage_Name':Collage_Name,'collage_CGPA':collage_CGPA,'about_me':about_me,'CompanyName':CompanyName,'Company_summary':Company_summary,'Tproject':Tproject,'Dproject':Dproject}
        # print(data)
        db,cmd=pool.connection()
        # q = "INSERT INTO profile ( `first_name`, `second_name`, `job_title`, `image`, `address`, `city`, `state`, `phone`, `emaill`, `github`, `linkeden`, `skill`, `school_name`, `collage_name`, `about_me`, `company_name`, `Tproject`, `Dproject`, `class10_marks`, `class12_marks`, `collage_cgpa`, `company_summary`) VALUES ( 'jk', 'kj', 'vf', 'vf', 'f', 'vf', 'vf', '12', 'ke@g.c', 'dddddddddd', 'dddddd', 'dddddw', 'eeeeee', 'nvk', 'jvkjj', 'kdddddd', 'ffffff', 'dddddd', '32', '23', '32', ' djvjdn');"
        q="insert into profile(first_name,second_name,job_title,image,address,city,state,phone,emaill,github,linkeden,skill,school_name,collage_name,about_me,company_name,Tproject,Dproject,class10_marks,class12_marks,collage_cgpa,company_summary) " \
           "values('{0}'      ,   '{1}' ,  '{2}'  ,'{3}'   ,    '{4}'   , '{5}','{6}'   ,'{7}'    ,  '{8}',      '{9}',      '{10}',   '{11}',       '{12}',         '{13}',      '{14}',         '{15}',      '{16}',      '{17}',     '{18}',     '{19}',           '{20}',           '{21}')".\
             format(firstname ,  lname  ,  jtitle , dp.name ,  address  , city ,  state ,  phone  ,  email ,  github  ,  linkedin  ,  skill  , school_name , Collage_Name  ,  about_me  ,  CompanyName  ,  Tproject  ,  Dproject  ,  class10  ,  class12  ,  collage_CGPA  ,  Company_summary )
        # print("11111111111111111")
        cmd.execute(q)
        
        # print(q)
        db.commit()
        # print("process 2222222222222222222222")
        db.close()
        
        # print("process 33333333333333333333333")

        f=open("D:/django/resueme_builder/asset/"+dp.name,"wb")
        for chunk in dp.chunks():
            f.write(chunk)
        f.close()
        # print("good")
        # pdfkit.from_file("result.html","resume.pdf")
        # print("vry")
        return render (request, 'result.html',{'data':data})
    except  Exception as e:
        print(e)
        return render(request, "resume.html")



def pdf(request):
    email =data['email']
    db,cmd=pool.connection()
    q2="SELECT * FROM profile WHERE emaill ='{0}'".format(email)
    cmd.execute(q2)
    row=cmd.fetchone()
    # db.commit()
    # print(row)
    # {'row':row}
    # print(row)
    db.close()
    template = loader.get_template("pdf.html")
    html = template.render({'row':row})
    option={
        'page-size' : 'Letter',
        'encoding' : 'UTF-8'}
    # config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")    
    pdf = pdfkit.from_string(html,False,option) 
    # pdf = pdfkit.from_file("pdf.html","resume.pdf")
    # pdfkit.from_url("http://google.com","pdf.html")
    response = HttpResponse(pdf,content_type = 'applicaiton/pdf')
    response['Content-Disposition'] = 'attachment'
    return response
    # return render (request, 'pdf.html',{'row':row})

    
    
           
        