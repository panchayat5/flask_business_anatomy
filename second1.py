from flask import Blueprint, render_template,send_file, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

second1 = Blueprint("second1", __name__, static_folder="static", template_folder="templates")

sales = pd.read_csv('static/csv/supermarket_sales.csv')

Mum = pd.read_csv('static/csv/Mumbai Sales_Analysis.csv')

Del = pd.read_csv('static/csv/Delhi Sales_Analysis.csv')

Bang = pd.read_csv('static/csv/Bangalore Sales_Analysis.csv') 


@second1.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', ProductLine = bpl, BestMonth = bms, BestCity = bcs, Member = mvn, Payment = ppm, SalesByH = sbh_s)
  
mm=dict()
# best product line--------------------------------------
ea=Bang[Bang['Product line']=='Electronics accessories']['Quantity'].sum()
fa=Bang[Bang['Product line']=='Fashion ccessories']['Quantity'].sum()
fb=Bang[Bang['Product line']=='Food and beverages']['Quantity'].sum()
hb=Bang[Bang['Product line']=='Health and beauty']['Quantity'].sum()
hl=Bang[Bang['Product line']=='Home and lifestyle']['Quantity'].sum()
sp=Bang[Bang['Product line']=='Sports and travel']['Quantity'].sum()
pl={'electronics accessories':ea,'Fashion accessories':fa,'food and beverages':fb,'health and beauty':hb,'home and lifestyle':hl,'sports and travel':sp}
bpl=max(pl,key=pl.get)
# print(f"{bpl}")


#best month----------------------------------
jan=sales[sales['Month']=='January']['Total'].sum()
feb=sales[sales['Month']=='February']['Total'].sum()
mar=sales[sales['Month']=='March']['Total'].sum()
monthlysalesdict={'January':jan,'february':feb,'march':mar}
bms=max(monthlysalesdict,key=monthlysalesdict.get)
# print(f"{bms}")  

#best city---------------------------------------------
mum=sales[sales['City']=='MUMBAI']['Total'].sum()
delh=sales[sales['City']=='DELHI']['Total'].sum()
blr=sales[sales['City']=='BANGALORE']['Total'].sum()
citysalesdict={'MUMBAI':mum,'DELHI':delh,'BANGALORE':blr}
bcs=max(citysalesdict,key=citysalesdict.get)
# print(f'{bcs}')

#membersVnormal---------------------------------------
mem=sales[sales['Customer type']=='Member']['Total'].sum()
non=sales[sales['Customer type']=='Normal']['Total'].sum()
memvsnordict={'Member':mem,'Normal':non}
mvn=max(memvsnordict,key=memvsnordict.get)
# print(f'MOST CUSTOMER WERE:{mvn}')

#preferablepaymentmode--------------------------------
cc=sales[sales['Payment']=='Credit Card']['Total'].sum()
cash=sales[sales['Payment']=='Cash']['Total'].sum()
ew=sales[sales['Payment']=='Ewallet']['Total'].sum()
paymentmodedict={'credit card':cc,'cash':cash,'Ewallet':ew}
ppm=max(paymentmodedict,key=paymentmodedict.get)
# print(f'most preferred payment mode:{ppm}')

#salesbyhour----------------------------------------
sales['Hour']=pd.to_datetime(sales['TIME']).dt.hour
sales['Minute']=pd.to_datetime(sales['TIME']).dt.minute
sales['Count']=1
ten=sales[sales['Hour']==10]['Total'].sum()
elv=sales[sales['Hour']==11]['Total'].sum()
twl=sales[sales['Hour']==12]['Total'].sum()
thr=sales[sales['Hour']==13]['Total'].sum()
frt=sales[sales['Hour']==14]['Total'].sum()
fif=sales[sales['Hour']==15]['Total'].sum()
six=sales[sales['Hour']==16]['Total'].sum()
svn=sales[sales['Hour']==17]['Total'].sum()
eig=sales[sales['Hour']==18]['Total'].sum()
nin=sales[sales['Hour']==19]['Total'].sum()
twn=sales[sales['Hour']==20]['Total'].sum()
salesbyhourdict={'10am':ten,'11am':elv,'12pm':twl,'1pm':thr,'2pm':frt,'3pm':fif,'4pm':six,'5pm':svn,'6pm':eig,'7pm':nin,'8pm':twn}
sbh_s=max(salesbyhourdict,key=salesbyhourdict.get)
# print(f'best time for sales:{sbh}')


# ########################################## BANGALORE #####################################


@second1.route("/bangalore")
def bangalore():
    return render_template('bangalore.html', MonthB = bms, ProductLineB = dmp_b, ByHourB = bsh_b)  

bpl=dict()

#monthlysales--------------------------------------------------
bmp=Bang.groupby('Month')['Total'].sum()
bms=list(bmp.keys())[0]
# print(f'best month for sales in bangalore:{bms}')

#productline----------------------------------------------------
ea_b=Bang[Bang['Product line']=='Electronics accessories']['Quantity'].sum()
fa_b=Bang[Bang['Product line']=='Fashion ccessories']['Quantity'].sum()
fb_b=Bang[Bang['Product line']=='Food and beverages']['Quantity'].sum()
hb_b=Bang[Bang['Product line']=='Health and beauty']['Quantity'].sum()
hl_b=Bang[Bang['Product line']=='Home and lifestyle']['Quantity'].sum()
sp_b=Bang[Bang['Product line']=='Sports and travel']['Quantity'].sum()
bangalorepl={'electronics accessories':ea_b,'Fashion accessories':fa_b,'food and beverages':fb_b,'health and beauty':hb_b,'home and lifestyle':hl_b,'sports and travel':sp_b}
dmp_b=max(bangalorepl,key=bangalorepl.get)
# print(f'best product line in bangalore is:{dmp_b}')

#salesbyhour-----------------------------------------------------
Bang['Hour']=pd.to_datetime(Bang['TIME']).dt.hour
Bang['Minute']=pd.to_datetime(Bang['TIME']).dt.minute
Bang['Count']=1
bsh=Bang.groupby('Hour')['Total'].sum()
bsh_b=list(bsh.keys())[0]
# print(f'best time for sales:{bsh_b}am')



########################################## Mumbai #####################################


@second1.route("/mumbai")
def mumbai():
    return render_template('mumbai.html', MonthM = mms, ProductLineM = mmp, ByHourM = sbhm)

#monthlysales--------------------------------------------------
mum_jan=Mum[Mum['Month']=='January']['Total'].sum()
mum_feb=Mum[Mum['Month']=='February']['Total'].sum()
mum_mar=Mum[Mum['Month']=='March']['Total'].sum()
monthly={'january':mum_jan,'february':mum_feb,'march':mum_mar}
mms=max(monthly,key=monthly.get)
# print(f'best month for sales in mumbai:{mms}')

#productline----------------------------------------------------
ea_m=Mum[Mum['Product line']=='Electronics accessories']['Quantity'].sum()
fa_m=Mum[Mum['Product line']=='Fashion accessories']['Quantity'].sum()
fb_m=Mum[Mum['Product line']=='Food and beverages']['Quantity'].sum()
hb_m=Mum[Mum['Product line']=='Health and beauty']['Quantity'].sum()
hl_m=Mum[Mum['Product line']=='Home and lifestyle']['Quantity'].sum()
sp_m=Mum[Mum['Product line']=='Sports and travel']['Quantity'].sum()
mumbaipl={'electronics accessories':ea_m,'Fashion accessories':fa_m,'food and beverages':fb_m,'health and beauty':hb_m,'home and lifestyle':hl_m,'sports and travel':sp_m}
mmp=max(mumbaipl,key=mumbaipl.get)
# print(f'the best product line is:{mmp}')

#salesbyhour-----------------------------------------------------
Mum['Hour']=pd.to_datetime(Mum['TIME']).dt.hour
Mum['Minute']=pd.to_datetime(Mum['TIME']).dt.minute
Mum['Count']=1
tenm=Mum[Mum['Hour']==10]['Total'].sum()
elvm=Mum[Mum['Hour']==11]['Total'].sum()
twlm=Mum[Mum['Hour']==12]['Total'].sum()
thrm=Mum[Mum['Hour']==13]['Total'].sum()
frtm=Mum[Mum['Hour']==14]['Total'].sum()
fifm=Mum[Mum['Hour']==15]['Total'].sum()
sixm=Mum[Mum['Hour']==16]['Total'].sum()
svnm=Mum[Mum['Hour']==17]['Total'].sum()
eigm=Mum[Mum['Hour']==18]['Total'].sum()
ninm=Mum[Mum['Hour']==19]['Total'].sum()
twnm=Mum[Mum['Hour']==20]['Total'].sum()
salesbyhourmumbai={'10am':tenm,'11am':elvm,'12pm':twlm,'1pm':thrm,'2pm':frtm,'3pm':fifm,'4pm':sixm,'5pm':svnm,'6pm':eigm,'7pm':ninm,'8pm':twnm}
sbhm=max(salesbyhourmumbai,key=salesbyhourmumbai.get)

# print(f'best time for sales:{sbhm}')


########################################## Delhi #####################################


@second1.route("/delhi")
def delhi():
    return render_template('delhi.html',MonthD = dms, ProductLineD = dmp_d, ByHourD = sbhd)       


dmp=dict()
#monthlysales--------------------------------------------------
del_jan=Del[Del['Month']=='January']['Total'].sum()
del_feb=Del[Del['Month']=='February']['Total'].sum()
del_mar=Del[Del['Month']=='March']['Total'].sum()
monthly1={'january':del_jan,'february':del_feb,'march':del_mar}
dms=max(monthly1,key=monthly1.get)
# print(f'best month for sales in delhi:{dms}')

#productline----------------------------------------------------
ea_d=Del[Del['Product line']=='Electronics accessories']['Quantity'].sum()
fa_d=Del[Del['Product line']=='Fashion ccessories']['Quantity'].sum()
fb_d=Del[Del['Product line']=='Food and beverages']['Quantity'].sum()
hb_d=Del[Del['Product line']=='Health and beauty']['Quantity'].sum()
hl_d=Del[Del['Product line']=='Home and lifestyle']['Quantity'].sum()
sp_d=Del[Del['Product line']=='Sports and travel']['Quantity'].sum()
delhipl={'electronics accessories':ea_d,'Fashion accessories':fa_d,'food and beverages':fb_d,'health and beauty':hb_d,'home and lifestyle':hl_d,'sports and travel':sp_d}
dmp_d=max(delhipl,key=delhipl.get)
# print(f"product line with the most sales is:{dmp_d}")

#salesbyhour-----------------------------------------------------
Del['Hour']=pd.to_datetime(Del['TIME']).dt.hour
Del['Minute']=pd.to_datetime(Del['TIME']).dt.minute
Del['Count']=1
tend=Del[Del['Hour']==10]['Total'].sum()
elvd=Del[Del['Hour']==11]['Total'].sum()
twld=Del[Del['Hour']==12]['Total'].sum()
thrd=Del[Del['Hour']==13]['Total'].sum()
frtd=Del[Del['Hour']==14]['Total'].sum()
fifd=Del[Del['Hour']==15]['Total'].sum()
sixd=Del[Del['Hour']==16]['Total'].sum()
svnd=Del[Del['Hour']==17]['Total'].sum()
eigd=Del[Del['Hour']==18]['Total'].sum()
nind=Del[Del['Hour']==19]['Total'].sum()
twnd=Del[Del['Hour']==20]['Total'].sum()
salesbyhourdelhi={'10am':tend,'11am':elvd,'12pm':twld,'1pm':thrd,'2pm':frtd,'3pm':fifd,'4pm':sixd,'5pm':svnd,'6pm':eigd,'7pm':nind,'8pm':twnd}
sbhd=max(salesbyhourdelhi,key=salesbyhourdelhi.get)
# print(f'best time for sales:{sbhd}')

