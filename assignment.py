#Dictionary of inventory
products = [{"Name" : "omo1KG", "Price" : 150 , "Description" :"Washing Powder"},
            {"Name" : "maizeFlour1KG", "Price" : 100 , "Description" :"Ugali maize meal"},
            {"Name" : "sugar1KG", "Price" : 120 , "Description" :"Pakistan Sugar"},
            {"Name" : "Rice1KG", "Price" : 180 , "Description" :"Mwea Pishori"},
            {"Name" : "Blueband1KG", "Price" : 200 , "Description" :"Sweet margerine"}]

for product in products:

        exclusivePrice = float(product['Price'])
        vatTax = (16/100)
        inclusivePrice  = exclusivePrice +(exclusivePrice * vatTax)
        print(product['Name'] , inclusivePrice , product['Description'])
        
        
    