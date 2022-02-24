from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp import models
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.text import MIMEText

shoppinglist = []
memb = []
seller = []

def index(request):
    global memb, seller
    sel = seller
    mem = memb
    
    productall = models.Product.objects.all()
    return render(request,"index.html",locals())

def detail(request, id=None):
    global memb, seller
    sel = seller
    mem = memb
    product = models.Product.objects.get(id=id)
    return render(request, "detail.html", locals())

def shoppingcar(request):
    global memb, seller, shoppinglist
    sel = seller
    mem = memb
    shoplist = shoppinglist
    total = 0
    for unit in shoppinglist:
        total += int(unit[3])
    finaltotal = total + 60
    return render(request,"shoppingcar.html",locals())

def addtocar(request, id=None, mode=None):
    global memb, seller, shoppinglist
    sel = seller
    mem = memb
    if mode == "add":  
        product = models.Product.objects.get(id=id)	
        flag = True
        for unit in shoppinglist:
            if product.pName == unit[0]:
                unit[2] = str(int(unit[2])+1)
                flag = False
                break
        if flag:
            templist = []
            templist.append(product.pName)
            templist.append(str(product.pPrice))
            templist.append('1')
            templist.append(str(product.pPrice))
            shoppinglist.append(templist)
        request.session['shoppinglist'] = shoppinglist
        return redirect("/shoppingcar/")

    elif mode == "update":
        n=0
        for unit in shoppinglist:
            unit[2] = request.POST.get('qty'+str(n),'1')
            unit[3] = str(int(unit[1]) * int(unit[2]))
            n += 1
        request.session['shoppinglist'] = shoppinglist
        return redirect("/shoppingcar/")   

    elif mode == "delete":
        shoppinglist = []
        request.session['shoppinglist'] = shoppinglist
        return redirect("/shoppingcar/")

    elif mode == "remove":
        del shoppinglist[int(id)]
        request.session['shoppinglist'] = shoppinglist
        return redirect("/shoppingcar/")

def memberpro(request):
    global memb, seller
    sel = seller
    mem = memb
    memberall = models.Member.objects.all()
    if(request.method == "POST"):
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        cAccount = request.POST["cAccount"]
        cPswd = request.POST["cPswd"]
        cPswdCheck = request.POST["cPswdCheck"]
        
        for member in memberall:
            if cPswdCheck != cPswd:
                mode = "pswd"
                return render(request, "memberpro.html", locals())
            elif cAccount == member.cAccount:
                mode = "account"
                return render(request, "memberpro.html", locals())
            elif cEmail == member.cEmail:
                mode = "email"
                return render(request, "memberpro.html", locals())
            else:
                unit = models.Member.objects.create(cName=cName, cSex=cSex ,cBirthday=cBirthday, cEmail=cEmail, cPhone=cPhone, cAddr=cAddr, cAccount=cAccount, cPswd=cPswd)
                unit.save()
                mode = "ok"
                return render(request, "memberpro.html", locals())
    else:
        return render(request, "memberpro.html", locals())

def memberlogin(request):
    global memb, seller
    mem = memb
    seller = []
    if(len(memb) == 0):
        if(request.method == "POST"):
            cAccount = request.POST["cAccount"]
            cPswd = request.POST["cPswd"]
            button = request.POST["button"]
            if(button == "註冊"):
                return redirect('/memberpro/')
            else:
                try:
                    member = models.Member.objects.get(cAccount=cAccount)
                    if(member.cPswd == cPswd):
                        memb.append(member.cName)
                        memb.append(member.cSex)
                        memb.append(str(member.cBirthday))
                        memb.append(member.cEmail)
                        memb.append(member.cPhone)
                        memb.append(member.cAddr)
                        memb.append(member.cAccount)
                        memb.append(member.cPswd)
                        memb.append("2")
                        return redirect('/index/')
                    else:
                        mode = "default"
                        return render(request, "memberlogin.html", locals())
                except:
                    mode = "fault"
                    return render(request, "memberlogin.html", locals())
        else:           
            return render(request, "memberlogin.html", locals())
    else:
       return redirect('/membercheck/') 

def memberlogout(request):
    global memb, seller
    sel = seller
    mem = memb
    if(len(seller) == 0):
        memb = []
        return redirect('/memberlogin/')
    else:
        seller = []
        return redirect('/sellerlogin/')

def memberinfo(request):
    global memb, seller
    sel = seller
    mem = memb
    member = models.Member.objects.get(cAccount=memb[6])
    return render(request,'memberinfo.html',locals())

def memberedit(request):
    global memb, seller
    sel = seller
    mem = memb
    member = models.Member.objects.get(cAccount=memb[6])
    member.cBirthday=str(member.cBirthday)
    if(request.method == "POST"):
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        cAccount = memb[6]

        unit = models.Member.objects.get(cAccount=cAccount)
        unit.cName=cName
        unit.cSex=cSex
        unit.cBirthday=cBirthday
        unit.cEmail=cEmail
        unit.cPhone=cPhone
        unit.cAddr=cAddr
        unit.save()
        return redirect('/memberinfo/') 
    else:    
        return render(request,'memberedit.html',locals())
    
def order(request):
    global memb, seller, shoppinglist
    sel = seller
    mem = memb
    shoplist = shoppinglist
    total = 0
    for unit in shoppinglist:
        total += int(unit[3])
    finaltotal = total + 60
    return render(request, "order.html", locals())

def checkok(request):
    global memb, seller, shoppinglist
    sel = seller
    mem = memb
    total = 0
    for unit in shoppinglist:
        total += int(unit[3])
    rGrandtotal = total+60
    if(request.method == "POST"):
        rAccount = mem[6]
        rName = request.POST["rName"]
        rPhone = request.POST["rPhone"]
        rAddr= request.POST["rAddr"]
        rEmail = request.POST["rEmail"]
        rPay = request.POST["rPay"]
        rState = "賣家備貨中"

        aunit = models.Addressee.objects.create(rAccount=rAccount, rName=rName, rPhone=rPhone, rAddr=rAddr, rEmail=rEmail, rPay=rPay, rGrandtotal=rGrandtotal, rState=rState)
        aunit.save()

        for unit in shoppinglist:
            rProduct = unit[0]
            rPrice = unit[1]
            rQty = unit[2]
            rTotal = unit[3]
            ounit = models.Order.objects.create(rOrder=aunit, rProduct=rProduct, rPrice=rPrice, rQty=rQty, rTotal=rTotal)
            ounit.save()
        orderid = aunit.id

        shoppinglist = []
        request.session['shoppinglist'] = shoppinglist

        return render(request, "checkok.html", locals())
    else:
        return redirect('/order/') 
                
def ordercheck(request): 
    global memb, seller
    sel = seller
    mem = memb 
    orderid = request.GET.get('orderid', '')  
    phone = request.GET.get('phone','')  
    if orderid == '' and phone == '':  
        firstsearch = 1
    else:
        addressee = models.Addressee.objects.filter(id=orderid).first()
        if addressee == None or addressee.rPhone != phone: 
            notfound = 1
        else:  
             orders = models.Order.objects.filter(rOrder=addressee)
    return render(request, "ordercheck.html", locals())		  

def background(request,mode=None, id=None):
    global memb, seller
    sel = seller
    mem = memb
    addressees = models.Addressee.objects.all().order_by("id")
    if(mode == "send"):
        unit = models.Addressee.objects.get(id=id)
        unit.rState = "商品已寄出"
        unit.save()
        return redirect('/background/')
    elif(mode == "delete"):
        unit = models.Addressee.objects.get(id=id)
        unit.rState = "取消訂單"
        unit.save()
        return redirect('/background/')
    else:
        return render(request, "background.html", locals())	

def membercheck(request,mode=None, id=None):
    global memb, seller
    sel = seller
    mem = memb
    
    addressees = models.Addressee.objects.filter(rAccount=mem[6])
    orders = models.Order.objects.filter(rOrder=addressees)

    if(mode == "send"):
        unit = models.Addressee.objects.get(id=id)
        unit.rState = "已取件"
        unit.save()
        return redirect('/membercheck/')
    else:
        return render(request,"membercheck.html",locals())

def sellerpro(request):
    global memb, seller
    sel = seller
    mem = memb
    sellerall = models.Seller.objects.all()
    if(request.method == "POST"):
        sName = request.POST["sName"]
        sSex = request.POST["sSex"]
        sBirthday = request.POST["sBirthday"]
        sEmail = request.POST["sEmail"]
        sPhone = request.POST["sPhone"]
        sAddr = request.POST["sAddr"]
        sAccount = request.POST["sAccount"]
        sPswd = request.POST["sPswd"]
        sPswdCheck = request.POST["sPswdCheck"]

        for sell in sellerall:
            if sPswdCheck != sPswd:
                mode = "pswd"
                return render(request, "sellerpro.html", locals())
            elif sAccount == sell.sAccount:
                mode = "account"
                return render(request, "sellerpro.html", locals())
            elif sEmail == sell.sEmail:
                mode = "email"
                return render(request, "sellerpro.html", locals())
            else:
                unit = models.Seller.objects.create(sName=sName, sSex=sSex ,sBirthday=sBirthday, sEmail=sEmail, sPhone=sPhone, sAddr=sAddr, sAccount=sAccount, sPswd=sPswd)
                unit.save()
                mode = "ok"
                return render(request, "sellerpro.html", locals())
    else:
        return render(request, "sellerpro.html", locals())
        
def sellerlogin(request):
    global memb, seller
    sel = seller
    memb=[]
    if(len(seller) == 0):
        if(request.method == "POST"):
            sAccount = request.POST["sAccount"]
            sPswd = request.POST["sPswd"]
            button = request.POST["button"]
            if(button == "註冊"):
                return redirect('/sellerpro/')
            else:
                try:
                    sell = models.Seller.objects.get(sAccount=sAccount)
                    if(sell.sPswd == sPswd):
                        seller.append("1")
                        seller.append(sell.sName)
                        seller.append(sell.sSex)
                        seller.append(str(sell.sBirthday))
                        seller.append(sell.sEmail)
                        seller.append(sell.sPhone)
                        seller.append(sell.sAddr)
                        seller.append(sell.sAccount)                        
                        return redirect('/background/')
                    else:
                        mode = "default"
                        return render(request, "sellerlogin.html", locals())
                except:
                    mode = "fault"
                    return render(request, "sellerlogin.html", locals())
        else:           
            return render(request, "sellerlogin.html", locals())
    else:
       return redirect('/background/') 

def sellerlogout(request,mode=None):
    global memb, seller
    mem = memb
    sel = seller
    if(mode == "delete"):
        seller = []
        return redirect('/sellerlogin/')
    else:
        return render(request, "sellerlogout.html", locals())

def productindex(request):
    global memb, seller
    sel = seller
    mem = memb
    productall = models.Product.objects.all()
    return render(request, "productindex.html", locals())

def productedit(request, id=None, mode=None):
    global memb, seller
    sel = seller
    mem = memb
    product = models.Product.objects.get(id=id)
    if(request.method == "POST"):
        pName = request.POST["pName"]
        pDescription = request.POST["pDescription"]
        pPrice = request.POST["pPrice"]
        pQty = request.POST["pQty"]

        unit = models.Product.objects.get(id=id)
        unit.pName=pName
        unit.pDescription=pDescription
        unit.pPrice=pPrice
        unit.pQty=pQty
        unit.save()
        return redirect('/productindex/')       
    else:    
        return render(request, "productedit.html", locals())

def productupload(request):
    global memb, seller
    sel = seller
    mem = memb
    if request.method == "POST":
        pro_Image = request.FILES["pro_Image"]
        pName = request.POST["pName"]
        pDescription = request.POST["pDescription"]
        pPrice = request.POST["pPrice"]
        pQty = request.POST["pQty"]
        
        unit = models.Product.objects.create(pro_Image=pro_Image,pName=pName,pDescription=pDescription,pPrice=pPrice,pQty=pQty)
        unit.save()
        return render(request, 'productupload.html', locals())
    else:    
        return render(request, 'productupload.html', locals())
