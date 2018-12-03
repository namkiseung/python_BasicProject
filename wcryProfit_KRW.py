#Quick and dirty script created by Matt Graham, @sp4rk2_
#https://pastebin.com/pz09r3cd
#Grabs the BTC transactions to specified BTC addresses.
#Thank you to coinbase and blockchain for pricing information.
#Also thanks to Gregor Spagnolo for keeping an updated list of addresses:
#https://github.com/GregorSpagnolo/WannaCrypt @gregorspagnolo

import urllib.request
import re
 
def getProfit():
    #Place addresses in this array.
    address = [ "12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw",
                "115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn",
                "13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94"]
 
    #Defines empty variable to calculate total.
    totalBTC=0
    #Prints the amount of addresses loaded.
    print(str(len(address)) + " addresses loaded (using coinbase for pricing)\n")
    #Grabs coinbase webpage for BTC to USD price.
    with urllib.request.urlopen('https://www.coinbase.com/charts') as response:
        #Decodes to readable HTML.
        html = str(response.read(), "utf-8")
        #Uses regular expression to grab BTC worth from source code.
        USD = float(re.search(r"(?<=<span>Bitcoin</span>\n<span class='charts-currency-price'>\n<span class='charts-middot'>&middot;</span>\n<span>\$).*?(?= USD</span>)", html).group(0).replace(",",""))

    with urllib.request.urlopen('http://ko.exchange-rates.org/converter/USD/KRW/1/Y') as response:
        #Decodes to readable HTML.
        html = str(response.read(), "utf-8")
        #Uses regular expression to grab BTC worth from source code.
        KRW = float(re.search(r'(?<=<span id="ctl00_M_lblToAmount">).*?(?=</span>)', html).group(0).replace(",",""))
    
 
    #For every address.
    for i in range(len(address)):
        #Grab blockchain webpage for the current address.
        with urllib.request.urlopen('https://blockchain.info/address/' + address[i]) as response:
            #Decodes to readable HTML.
            html = str(response.read(), "utf-8")
            #Uses regular expression to grab the total received BTC from the source code.
            BTC = float(re.search(r'(?<=<td id="total_received"><font color="green"><span data-c=").*?(?= BTC</span>)', html).group(0).split(">")[1])
            #Uses regular expression to grab the transaction amount from the source code.
            transactions = re.search(r'(?<=<td id="n_transactions">).*?(?=</td>)', html).group(0)
            #Prints the address.
            print("\033[95m\033[1mAddress\033[0m: \033[3m" + address[i] + "\033[0m")
            #Prints the amount of transactions.
            print("\033[95mTransactions\033[0m: " + transactions)
            #Prints the BTC receieved.
            print("\033[95mBTC received\033[0m: \033[94m" + str(BTC) + " BTC\033[0m")
            #Prints the USD received.
            print("\033[95mUSD received\033[0m: \033[92m" + format(int(BTC * USD), ',f').split(".")[0] + " USD\033[0m")
	     #Prints the KRW received.
            print("\033[95mKRW received\033[0m: \033[92m" + format(int(BTC * USD * KRW), ',f').split(".")[0] + " KRW\033[0m\n")
            #Increments totalBTC by the address BTC.
            totalBTC += BTC
 
    #Prints the total BTC receieved.
    print("\033[95m\033[1mTotal BTC received\033[0m: \033[94m" + str(totalBTC) + " BTC\033[0m")
    #Prints the total USD receieved.
    print("\033[95m\033[1mTotal USD received\033[0m: \033[92m" + format(int(totalBTC * USD), ',f').split(".")[0] + " USD\033[0m")
    #Prints the total KRW receieved.
    print("\033[95m\033[1mTotal KRW received\033[0m: \033[92m" + format(int(totalBTC * USD * KRW), ',f').split(".")[0] + " KRW\033[0m")
 
getProfit()
