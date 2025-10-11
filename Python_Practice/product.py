product_name="lush lychee"
product_price=45
product_quantity=600
product_gst=3.85
is_guarantee=True
ingredients=["water","suger","grape juice",]
address=("raisen","madhya pradesh")
precaustions={"DO NOT BUY BOTTELS THAT THEY ARE LEAKING,PUFFED OR HAVE A BROKEN CAP SEAL"}
product_profile={"name":product_name,"price":product_price,"quantity":product_quantity,"gst":product_gst,"guarantee":is_guarantee,"ingrediants":ingredients,"address":address,"precaustions":precaustions}
print("product profile")
print("name:",product_profile["name"])
print("price:",product_profile["price"])
print("quantity:",product_profile["quantity"])
print("gst:",product_profile["gst"])
print("ingrediants:",",".join(product_profile["ingrediants"]))
print("address:",",".join(product_profile["address"]))
print("precaustions"",".join(product_profile["precaustions"]))
