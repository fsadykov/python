input = """pslchi6dpricedev43 |11030 |F0X2YQ1 |10.2.60.198 |Datacenter1 (CHI6) |A15-9 |PowerEdge R640 pslchi6dpricedev44 |11031 |F0X4YQ1 |10.2.60.199 |Datacenter1 (CHI6) |A15-10 |PowerEdge R640 pslchi6dpricedev45 |3960 |3DR6FP1 |10.2.60.154 |Datacenter1 (CHI6) |B16-4 |PowerEdge R640 pslchi6dpricedev46 |3956 |3DS6FP1 |10.2.60.150 |Datacenter1 (CHI6) |A03-9 |PowerEdge R640 """
data = input.split(' ')
for item in data:
    deletedPipe = item.replace('|', '')
    ipaddr = deletedPipe.split('.')
    if ipaddr[0] == '10':
        print(deletedPipe)
