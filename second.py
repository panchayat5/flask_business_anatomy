from flask import Blueprint, render_template,send_file, request
import io
import os
import pandas as pd
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


second = Blueprint("second", __name__, static_folder="static", template_folder="templates")


sales = pd.read_csv('static/csv/supermarket_sales.csv')

Mum = pd.read_csv('static/csv/Mumbai Sales_Analysis.csv')

Del = pd.read_csv('static/csv/Delhi Sales_Analysis.csv')

Bang = pd.read_csv('static/csv/Bangalore Sales_Analysis.csv') 
    

@second.route("/settings")
def settings():
    return render_template('settings.html')          


@second.route("/Total/Month")
def Q1():

    Total_Sales = sales.groupby('Month').Total.sum()
    months = range(1,4)
        
    plt.figure(figsize=(10,7))
    colors = ['#e01616', '#612f75', '#db3d7a']
        
    plt.bar(months, Total_Sales, color = colors)
        
    plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
        
    labels = ['Jaunuary', 'February', 'March']
    plt.xticks(months, size = 14, labels = labels)
    plt.yticks(size=14)
        
    plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.savefig("static/graph_Img/Total_Sales/Month.png")

    return render_template('dashboard.html')        

@second.route("/Total/City")
def Q2():

    # Delhi = sales.loc[sales['City'] == 'DELHI'].count()[0]
    # Mumbai = sales.loc[sales['City'] == 'MUMBAI'].count()[0]
    # Bangalore = sales.loc[sales['City'] == 'BANGALORE'].count()[0]

    Mumbai = sales.loc[sales['City'] == 'MUMBAI'].Total.sum().astype(int)
    Delhi = sales.loc[sales['City'] == 'DELHI'].Total.sum().astype(int)
    Bangalore = sales.loc[sales['City'] == 'BANGALORE'].Total.sum().astype(int)

    labels = ['Mumbai', 'Delhi', 'Bangalore']
    colors = ['#4755a6', '#6da32f']
    explode = (0.1,0.1,0.1)

    plt.pie([Delhi,Mumbai,Bangalore], labels = labels, explode = explode, autopct = '%.2f %%', radius=1.5,textprops={'fontsize': 15} )

    plt.savefig("static/graph_Img/Total_Sales/City.png")

    return render_template('dashboard.html')

@second.route("/Total/Time")
def Q3():

    sales['Hour'] = pd.to_datetime(sales['TIME']).dt.hour
    sales['Minute'] = pd.to_datetime(sales['TIME']).dt.minute
    sales['Count'] = 1

    keys = [pair for pair, df in sales.groupby(['Hour'])]

    plt.figure(figsize=(9,6))

    plt.title('Sales By Hour', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.plot(keys, sales.groupby(['Hour']).count()['Count'], color='#32b865')

    plt.xticks(keys,size = 13)
    plt.yticks(size = 13)

    plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Time in Hours', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.grid()
    plt.savefig("static/graph_Img/Total_Sales/Time.png")

    return render_template('dashboard.html')


@second.route("/Total_Product")
def Q4():

    Total_Sales = sales.groupby('Product line').Total.sum()

    Product = sales.groupby('Product line')
    keys = [pair for pair, df in Product]

    plt.figure(figsize=(14,9))

    plt.title('Sales Of Product', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    colors = ['#4755a6', '#6da32f', '#ad283e', '#d6d01e', '#913d5b', '#5b7fe3']

    plt.bar(keys, Total_Sales, color = colors)

    plt.xticks(keys, size=12)
    plt.yticks(size = 14)

    plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 25 })
    plt.xlabel('Product Line', fontdict= {'fontname': 'Georgia','fontsize': 25 })

#     # quantity_ordered = Product.sum()['Quantity']

#     # fig, ax1 = plt.subplots()

#     # ax2 = ax1.twinx()

#     # ax1.bar(keys, Total_Sales, color='g')
#     # ax2.plot(keys, quantity_ordered, color='b')

#     # # plt.figure(figsize=(8,4))

#     # ax1.set_xlabel('Product Line', size=20)
#     # ax1.set_ylabel('Sales', color='g', size=20)
#     # ax2.set_ylabel('Quantity', color='b',size=20)
#     # ax1.set_xticklabels(keys, rotation='vertical', size=15)
#     # plt.yticks(size = 13)

    plt.savefig("static/graph_Img/Total_Sales/Product.png")

    return render_template('dashboard.html')

@second.route("/Total_Customer")
def Q5():

    normal = sales.loc[sales['Customer type'] == 'Normal'].count()[0]
    member = sales.loc[sales['Customer type'] == 'Member'].count()[0]

    labels = ['Normal', 'Member']
    colors = ['#6097a8', '#ab8c26']
    explode = (0.13,0.13)

    plt.pie([normal,member],labels = labels, colors = colors, explode = explode, autopct = '%.2f %%', radius=1.2 ,textprops={'fontsize': 16})

    plt.savefig("static/graph_Img/Total_Sales/Customer.png")

    return render_template('dashboard.html')

@second.route("/Total_Payment")
def Q6():

    Credit_card = sales.loc[sales['Payment'] == 'Credit card'].count()[0]
    Cash = sales.loc[sales['Payment'] == 'Cash'].count()[0]
    Ewallet = sales.loc[sales['Payment'] == 'Ewallet'].count()[0]

    labels = ['Credit card', 'Cash', 'Ewallet']
    colors = ['#4755a6', '#6da32f','#c24127']
    explode = (0.1,0.1,0.1)

    plt.pie([Credit_card, Cash, Ewallet], labels = labels,explode = explode, colors = colors, autopct = '%.2f %%', radius=1.3,textprops={'fontsize': 14})

    plt.savefig("static/graph_Img/Total_Sales/Payment.png")

    return render_template('dashboard.html')

@second.route("/Mumbai_Month")
def M1():

    #  sales.groupby(['Month']).sum()
    Total_Sales = Mum.groupby('Month').Total.sum()

    months = range(1,4)
    # print(months)

    plt.figure(figsize=(10,7))
    color = ['#e01616', '#b4ed2d', '#9e48db']

    plt.bar(months, Total_Sales, color = color)

    plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    labels = ['Jaunuary', 'February', 'March']

    plt.xticks(months, size = 14, labels = labels)
    plt.yticks(size=14)

    plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.savefig("static/graph_Img/Mumbai_Graph/Month.png")

    return render_template('mumbai.html')

@second.route("/Mumbai_Product")
def M2():

    Total_Sales = Mum.groupby('Product line').Total.sum()

    Product = sales.groupby('Product line')
    keys = [pair for pair, df in Product]

    plt.figure(figsize=(15,8))

    plt.title('Sales Of Product', fontdict= {'fontname': 'Georgia','fontsize': 25 })
    colors = ['#4755a6', '#6da32f', '#ad283e', '#d6d01e', '#913d5b', '#5b7fe3']

    plt.bar(keys, Total_Sales, color = colors)

    plt.xticks(keys, size=12)
    plt.yticks(size = 14)

    plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 25 })
    plt.xlabel('Product Line', fontdict= {'fontname': 'Georgia','fontsize': 25 })

    plt.savefig("static/graph_Img/Mumbai_Graph/Product.png")

    return render_template('mumbai.html')

@second.route("/Mumbai_Hour")
def M3():

    Mum['Hour'] = pd.to_datetime(Mum['TIME']).dt.hour
    Mum['Minute'] = pd.to_datetime(Mum['TIME']).dt.minute
    Mum['Count'] = 1

    keys = [pair for pair, df in Mum.groupby(['Hour'])]

    plt.figure(figsize=(9,6))

    plt.title('Sales By Hour', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.plot(keys, Mum.groupby(['Hour']).count()['Count'], color='#32b865')

    plt.xticks(keys,size = 13)
    plt.yticks(size = 13)

    plt.ylabel('Sales Count', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Time in Hours', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.grid()

    plt.savefig("static/graph_Img/Mumbai_Graph/Total_Time.png")

    return render_template('mumbai.html')

@second.route("/Delhi_Month")
def D1():

    #  sales.groupby(['Month']).sum()
    Total_Sales = Del.groupby('Month').Total.sum()

    months = range(1,4)
    # print(months)

    plt.figure(figsize=(10,7))
    color = ['#e01616', '#b4ed2d', '#9e48db']

    plt.bar(months, Total_Sales, color = color)

    plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    labels = ['Jaunuary', 'February', 'March']

    plt.xticks(months, size = 14, labels = labels)
    plt.yticks(size=14)

    plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.savefig("static/graph_Img/Delhi_Graph/Month.png")

    return render_template('delhi.html')

@second.route("/Delhi_Product")
def D2():

   Total_Sales = Del.groupby('Product line').Total.sum()
   Product = Del.groupby('Product line')
   keys = [pair for pair, df in Product]

   plt.figure(figsize=(15,8))

   plt.title('Sales Of Product', fontdict= {'fontname': 'Georgia','fontsize': 25 })
   colors = ['#4755a6', '#6da32f', '#ad283e', '#d6d01e', '#913d5b', '#5b7fe3']
   
   plt.bar(keys, Total_Sales, color = colors)
   
   plt.xticks(keys, size=12)
   plt.yticks(size = 14)
   
   plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 25 })
   plt.xlabel('Product Line', fontdict= {'fontname': 'Georgia','fontsize': 25 })
   
   plt.savefig("static/graph_Img/Delhi_Graph/Product.png")
   
   return render_template('delhi.html')

@second.route("/Delhi_Hour")
def D3():

    Del['Hour'] = pd.to_datetime(Del['TIME']).dt.hour
    Del['Minute'] = pd.to_datetime(Del['TIME']).dt.minute
    Del['Count'] = 1

    keys = [pair for pair, df in Del.groupby(['Hour'])]
    Total_Sales = Del.groupby(['Hour']).count()['Count']

    plt.figure(figsize=(9,6))

    plt.title('Sales By Hour', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.plot(keys, Total_Sales , color='#32b865')

    plt.xticks(keys,size = 13)
    plt.yticks(size = 13)

    plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Time in Hours', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.grid()

    plt.savefig("static/graph_Img/Delhi_Graph/Total_Time.png")

    return render_template('delhi.html')

@second.route("/Bangalore_Month")
def B1():
    
    #  sales.groupby(['Month']).sum()
    Total_Sales = Bang.groupby('Month').Total.sum()

    months = range(1,4)
    # print(months)

    plt.figure(figsize=(10,7))
    color = ['#e01616', '#b4ed2d', '#9e48db']

    plt.bar(months, Total_Sales, color = color)
    
    plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    labels = ['Jaunuary', 'February', 'March']

    plt.xticks(months, size = 14, labels = labels)
    plt.yticks(size=14)

    plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.savefig("static/graph_Img/Bangalore_Graph/Month.png")

    return render_template('bangalore.html')

@second.route("/Bangalore_Product")
def B2():

    Total_Sales = Bang.groupby('Product line').Total.sum()

    Product = Bang.groupby('Product line')
    keys = [pair for pair, df in Product]

    plt.figure(figsize=(14,8))

    plt.title('Sales Of Product', fontdict= {'fontname': 'Georgia','fontsize': 25 })
    colors = ['#4755a6', '#6da32f', '#ad283e', '#d6d01e', '#913d5b', '#5b7fe3']

    plt.bar(keys, Total_Sales, color = colors)

    plt.xticks(keys, size=12)
    plt.yticks(size = 14)

    plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 25 })
    plt.xlabel('Product Line', fontdict= {'fontname': 'Georgia','fontsize': 25 })

    plt.savefig("static/graph_Img/Bangalore_Graph/Product.png")

    return render_template('bangalore.html')

@second.route("/Bangalore_Hour")
def B3():

    Bang['Hour'] = pd.to_datetime(Bang['TIME']).dt.hour
    Bang['Minute'] = pd.to_datetime(Bang['TIME']).dt.minute
    Bang['Count'] = 1

    keys = [pair for pair, df in Bang.groupby(['Hour'])]
    Total_Sales = Bang.groupby(['Hour']).count()['Count']

    plt.figure(figsize=(9,6))

    plt.title('Sales By Hour', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.plot(keys, Total_Sales, color='#32b865')

    plt.xticks(keys,size = 13)
    plt.yticks(size = 13)

    plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Time in Hours', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.grid()

    plt.savefig("static/graph_Img/Bangalore_Graph/Total_Time.png")

    return render_template('bangalore.html')


