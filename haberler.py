import feedparser

"""
    NTV son dakika haberlerini çekme
"""
url = "https://www.ntv.com.tr/gundem.rss"
haberler = feedparser.parse(url)

i = 0
for haber in haberler.entries:
    i += 1
    print("{}. haber".format(i))
    print(haber.title)
    print(haber.link)

    print("\n")