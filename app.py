### Establishing a connection to the SQL server ###

from flask import Flask,jsonify,request,render_template
import sqlite3
app=Flask(__name__)

#creating function for id generation for all tables
def idgenerator(tab):
    conn=sqlite3.connect('ims.db')
    cur = conn.cursor()
    idval = ''
    if tab=='CUSTOMER':
        idval = 'CUSTOMER_ID'
    if tab=='PRODUCT':
        idval = 'PRODUCT_ID'
    if tab=='ORDERS':
        idval = 'ORDER_ID'
    if tab=='SUPPLIER':
        idval = 'SUPPLIER_ID'
    print(tab,idval)
    cur.execute(f"SELECT {idval} FROM {tab}")
    new = cur.fetchall()
    cud = str(new[len(new)-1][0])
    for i in range(len(str(cud))):
        if cud[i].isnumeric():
            f = i
            break
    myint = cud[f:]
    myint = int(myint)+1
    return idval[0:3]+str(myint)

@app.route('/')    # routing homepage
def home():
    return render_template('index.html')

#Functions or API's for every front end hyperlinks

################################## For Showing Customers ######################################

@app.route("/show-customers")
def customer_show():
    conn=sqlite3.connect('ims.db')
    cn=conn.cursor()
    cn.execute("select * from customer")
    data=[]
    for i in cn.fetchall():
        customer={}
        customer['customer_id']=i[0]
        customer['customer_name']=i[1]
        customer['customer_addr']=i[2]
        customer['customer_email']=i[3]
        data.append(customer)
    return render_template('showcustomers.html',data=data)

################################## For Showing Products #######################################

@app.route("/show-product")
def product_show():
    conn=sqlite3.connect('ims.db')
    cn=conn.cursor()
    cn.execute("select * from product")
    data=[]
    for i in cn.fetchall():
        product={}
        product['product_id']=i[0]
        product['product_name']=i[1]
        product['product_stock']=i[2]
        product['product_price']=i[3]
        product['product_supplier']=i[4]

        data.append(product)
    print(data)
    return render_template('showproduct.html',data=data)

################################## For Showing Orders #######################################

@app.route("/show-orders")
def order_show():
    conn=sqlite3.connect('ims.db')
    cn=conn.cursor()
    cn.execute("select * from orders")
    data=[]
    for i in cn.fetchall():
        orders={}
        orders['order_id']=i[0]
        orders['product_ID']=i[1]
        orders['customer_id']=i[2]
        orders['quantity']=i[3]

        data.append(orders)
    print(data)
    return render_template('showorders.html',data=data)

################################## For Showing Suppliers #######################################

@app.route("/show-suppliers")
def supplier_show():
    conn=sqlite3.connect('ims.db')
    cn=conn.cursor()
    cn.execute("select * from supplier")
    data=[]
    for i in cn.fetchall():
        suppliers={}
        suppliers['supplier_id']=i[0]
        suppliers['supplier_name']=i[1]
        suppliers['supplier_addr']=i[2]
        suppliers['supplier_email']=i[3]

        data.append(suppliers)
    print(data)
    return render_template('showsuppliers.html',data=data)

################################## For Adding Customers #######################################

@app.route("/add-customer",methods=['GET','POST'])
def addcustomer():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn=conn.cursor()
        id=idgenerator('CUSTOMER')
        customername=request.form.get('name')
        customeraddr=request.form.get('addr')
        customeremail=request.form.get('email')
        cn.execute(f"insert into customer(customer_id,customer_name,customer_addr,customer_email) values('{id}','{customername}','{customeraddr}','{customeremail}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addcustomer.html')

################################## For Updating Customers #######################################

@app.route("/update-customer",methods=['GET','POST'])
def updatecustomer():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn=conn.cursor()
        customerid=request.form.get('customer_id')
        change=request.form.get('change')
        newvalue=request.form.get('newvalue')
        cn.execute(f"update  customer set {change} = '{newvalue}' where customer_id = '{customerid}'")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updatecustomer.html')
    
################################## For Adding Products #######################################

@app.route("/add-product",methods=['GET','POST'])
def addproduct():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn=conn.cursor()
        id=idgenerator('PRODUCT')
        productname=request.form.get('productname')
        productstock=request.form.get('stock')
        productprice=request.form.get('price')
        productsupplierid=request.form.get('supplierid')
        cn.execute(f"insert into product(product_id,product_name,stock,price,supplier_id) values('{id}','{productname}','{productstock}','{productprice}','{productsupplierid}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addproduct.html')

################################## For Adding Orders #######################################

@app.route("/add-orders",methods=['GET','POST'])
def addorder():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn=conn.cursor()
        id=idgenerator('ORDERS')
        productid=request.form.get('productid')
        customerid=request.form.get('customerid')
        quantity=request.form.get('quantity')
        cn.execute(f"insert into orders(order_id,product_id,customer_id,quantity) values('{id}','{productid}','{customerid}','{quantity}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addorder.html')
    
################################## For Adding Suppliers #######################################

@app.route("/add-supplier",methods=['GET','POST'])
def addsupplier():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn=conn.cursor()
        id=idgenerator('SUPPLIER')
        suppliername=request.form.get('suppliername')
        supplieraddr=request.form.get('supplieraddr')
        supplieremail=request.form.get('supplieremail')
        cn.execute(f"insert into supplier(supplier_id,supplier_name,supplier_addr,supplier_email) values('{id}','{suppliername}','{supplieraddr}','{supplieremail}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addsupplier.html')

################################## For Updating Products #######################################

@app.route("/update-product",methods=['GET','POST'])
def updateproduct():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn=conn.cursor()
        productid=request.form.get('product_id')
        change=request.form.get('change')
        newvalue=request.form.get('newvalue')
        cn.execute(f"update  product set {change} = '{newvalue}' where product_id = '{productid}'")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updateproduct.html')

################################## For Updating Orders #######################################

@app.route("/update-orders",methods=['GET','POST'])
def updateorder():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn=conn.cursor()
        orderid=request.form.get('order_id')
        change=request.form.get('change')
        newvalue=request.form.get('newvalue')
        cn.execute(f"update orders set {change} = '{newvalue}' where order_id = '{orderid}'")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updateorder.html')
    
################################## For Updating Suppliers #######################################

@app.route("/update-supplier",methods=['GET','POST'])
def updatesupplier():
    if request.method=='POST':
        conn=sqlite3.connect('ims.db')
        cn=conn.cursor()
        supplierid=request.form.get('supplier_id')
        change=request.form.get('change')
        newvalue=request.form.get('newvalue')
        cn.execute(f"update  supplier set {change} = '{newvalue}' where supplier_id = '{supplierid}'")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updatesupplier.html')
    
################################## For Deleting Products #######################################

@app.route("/delete-product", methods=['GET', 'POST'])
def deleteproduct():
    if request.method == 'POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        productid = request.form.get('product_id')
        
        # Check if the product exists in the database
        cn.execute(f"SELECT * FROM product WHERE product_id = '{productid}'")
        product = cn.fetchone()
        
        if product:
            # Delete the product from the database
            cn.execute(f"DELETE FROM product WHERE product_id = '{productid}'")
            conn.commit()
            print('Product has been deleted')
            return jsonify({'message': 'successful'})
        else:
            return jsonify({'error': 'Product does not exist'})
    else:
        return render_template('deleteproduct.html')
    
################################## For Deleting Orders #######################################

@app.route('/delete-orders',methods =['GET','POST'])
def deleteorder():
    if request.method=='POST':
        conn = sqlite3.connect('ims.db')
        cn=conn.cursor()
        ORDER_ID=request.form.get("orderid")
        cn.execute(f"DELETE FROM ORDERS WHERE order_id = '{ORDER_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('deleteorder.html')
    
################################## For deleting Suppliers #######################################

@app.route("/delete-supplier", methods=['GET', 'POST'])
def deletesupplier():
    if request.method == 'POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        supplierid = request.form.get('supplier_id')
        
        # Check if the supplier exists in the database
        cn.execute(f"SELECT * FROM supplier WHERE supplier_id = '{supplierid}'")
        supplier = cn.fetchone()
        
        if supplier:
            # Delete the supplier from the database
            cn.execute(f"DELETE FROM supplier WHERE supplier_id = '{supplierid}'")
            conn.commit()
            print('Supplier has been deleted')
            return jsonify({'message': 'successful'})
        else:
            return jsonify({'error': 'Supplier does not exist'})
    else:
        return render_template('deletesupplier.html')
    
################################## For Deleting Customers #######################################

@app.route("/delete-customer", methods=['GET', 'POST'])
def deletecustomer():
    if request.method == 'POST':
        conn=sqlite3.connect('ims.db')
        cn = conn.cursor()
        customerid = request.form.get('customer_id')
        
        # Check if the customer exists in the database
        cn.execute(f"SELECT * FROM customer WHERE customer_id = '{customerid}'")
        customer = cn.fetchone()
        
        if customer:
            # Delete the customer from the database
            cn.execute(f"DELETE FROM customer WHERE customer_id = '{customerid}'")
            conn.commit()
            print('Customer has been deleted')
            return jsonify({'message': 'successful'})
        else:
            return jsonify({'error': 'Customer does not exist'})
    else:
        return render_template('deletecustomer.html')


    

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=False)





