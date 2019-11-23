# Tes-ArkademyArisSupardiman
Tes Masuk Bootcamp

untuk tes 6a hanya query
jadi untuk runningnya silahkan import file arkademy.sqlnya ke database anda
setelah itu masukan query ini 

select cashier.name as cashier, product.name as product, category.name as category, product.price from product join cashier on product.id_cashier=cashier.id join category on product.id_category=category.id 

agar bisa terlihat output yang di inginkan

