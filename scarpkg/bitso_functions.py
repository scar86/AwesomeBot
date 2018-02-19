import bitso
from get_variables import get_info
from log import logMsg

def create_api(key=None,secret=None,get='bitso'):
    INFO = get_info()
    
    if not key:
        bitso_key=INFO[get]['key']
    if not secret:
        bitso_secret=INFO[get]['secret']
        
    api = bitso.Api(bitso_key,bitso_secret)
    
    return api
    
    
def get_bitso_balance(key=None,secret=None):
    logMsg("Function: get_bitso_balance")
    api = bitso.Api()
    try:
        balance = api.balances() #using some undermethos of the bitso api
    except:
        logMsg("Failed to connect to bitso api, verify key and secret are correct")
        return 1
    lst=[]
    txt=[]
    for a in balance.currencies:
        if a == 'currencies' or a == 'mxn':
            pass
        elif getattr(balance, a).total:
            lst.append((a,getattr(balance, a).total))
    
    total_mx=0.0
    for coin, total in lst:
        tick = api.ticker("{0}_mxn".format(coin))
        logMsg("Coin {0} currently 1 in mxn ${1:}".format(coin,tick.last))
        txt.append("Coin {0} currently 1 in mxn ${1:}".format(coin,tick.last))
        
        logMsg("For {0} you have {1:>12} in mxn ${2:.2f}".format(coin,total,total*tick.last))
        txt.append("For {0} you have {1:>12} in mxn ${2:.2f}".format(coin,total,total*tick.last))
        total_mx += float(total*tick.last)
    
    if balance.mxn.total > 0:
        logMsg("You have {0:.2f} MXN on your wallet ready to buy coins".format(balance.mxn.total))
        txt.append("You have {0:.2f} MXN on your wallet ready to buy coins".format(balance.mxn.total))
    total_mx += float(balance.mxn.total)
    logMsg("Total in MXN : ${0:.2f}".format(total_mx))
    txt.append("Total in MXN : ${0:.2f}".format(total_mx))
    return '\n'.join(txt)

def get_orders(key=None,secret=None):
    api = bitso.Api()
    logMsg("Getting open orders")
    try:
        books = api.available_books()
    except:
        logMsg("Failed to connect to bitso api to get books info, verify key and secret are correct")
        return 1
    r_lst=[]
    for book in books.__dict__.keys():
        if book == 'books':
            continue
        try:
            oo = api.open_orders(book) #using some undermethos of the bitso api
        except:
            logMsg("Failed to connect to book {0}".format)
            return 1
        if oo:
            txt = ["Book : {0}".format(book)]
            for order in oo:
                txt.append("\nOrder id : {0}".format(order.oid))
                txt.append("Order side : {0}".format(order.side))
                txt.append("Order type : {0}".format(order.type))
                txt.append("At Coin price : {0}".format(order.price))
                txt.append("Coin amount : {0}".format(order.original_amount))
                txt.append("Value in MXN : {0}".format(order.original_value))
                #txt.append("-"*20)
            r_lst.append("\n".join(txt))
            logMsg("\n".join(txt))
    
    return r_lst
    
def put_order(args):
    logMsg("Function : put_order")
    api = create_api()
    book, op, price, mxn = args
    op = op.lower()
    major = "{0:.7}".format(1*float(mxn)/float(price))
    logMsg("Book {0}, op {1}, price {2}, major {3}, mxn {4}".format(book,op,price,major,mxn))
    try:
        order = api.place_order(book=book, side=op, order_type='limit', major=major, price=price)
    except ApiError as e:
        logMsg("ERROR setting the order {0}".format(e))
        order =  {'oid' : 'ERROR setting order'}
    
    return order

def get_ticker(book='eth_mxn'):
    logMsg("Function : put_order")
    api = create_api()
    info = api.ticker(book)
    
    return info
