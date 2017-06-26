# -*- encoding: utf8 -*-

import pycurl

postarr = {
    "token"                     : "e64c026cea54d38be64c026cea54d38b",  #访问令牌 京东
#    "token"                     : "dc47280b595ea34707cec75a6d4ff068", #饿了么
#    "token"                     : "db06c78d1e24cf709453997fedf62efd", #美团


    "origin_id"                 : "66652",#原始订单id（即第三方对接平台订单id）
    "city_name"                 : "上海市",  #订单所在城市名称(如上海就填"上海")
    "city_code"                 : "021",
#    "city_name"                 : "南京市",
#    "city_code"                 : "025",
#    "city_name"                 : "北京市",
#    "city_code"                 : "010",
    "info"                      : "具体请向达达客服咨询", #订单说明（针对订单的说明信息）

    "pay_for_supplier_fee"      : 100,#付给商家的费用，如果无需支付，传0
    "fetch_from_receiver_fee"   : 100,   #向客户收取的费用，如果无，传0
    "deliver_fee"               : 0,#订单运费

    "create_time"               : 1407832493,#订单创建时间

    "cargo_type"                : 1, #订单商品类型 （1、餐饮 2、饮料 3、鲜花 4、票务 5、其他）
    "cargo_weight"              : 20,#订单商品重量
    "cargo_price"               : 18, #订单商品价格
    "is_prepay"                 : 1,
    "expected_fetch_time"       : 1416799180,#期望取货时间
    "expected_finish_time"      : 0,#期望送达时间

    "supplier_id"               : "jd123",  #发货人ID
    "supplier_name"             : "测试单",  #发货人姓名
    "supplier_address"          : "上海市浦东新区浦东南路1603号",#发货地址
    "supplier_phone"            :  "",#发货人手机
    "supplier_tel"              : "888888881",#发货人座机
    "supplier_lat"              : 31.229004,#发货人（商家）纬度 北京
    "supplier_lng"              : 121.515028,#发货人（商家）经度 北京


    "invoice_title"             : " ",#发票抬头（个人就是个人姓名，公司为公司名称)

    "receiver_name"             : "测试单123",#收货人姓名
    "receiver_address"          : "测试测试测试",#收货人地址
    "receiver_phone"            : 18017289912,#收货人手机

    "callback"                  : "http://www.imdada.cn",   #回调URL
    "cargo_num"                 : 3,
    "ispublish"                 : 0

}

#print postarr

postfields = "&".join(["%s=%s" % (k, v) for k, v in postarr.items()])
#print "------------------------------------------------"
#print postfields

c = pycurl.Curl()
#c.setopt(c.URL, "http://public.imdada.cn/v1_0/addOrder/")
c.setopt(c.URL, "http://public.ga.dev.imdada.cn/v1_0/addOrder/")
#c.setopt(c.URL, "http://public.dev.imdada.cn/v1_0/addOrder/")
#c.setopt(c.URL, "http://192.168.196.203:5004/v1_0/addOrder/")
c.setopt(c.POSTFIELDS, postfields)
c.perform()


