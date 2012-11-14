import os.path
import urllib
import urllib2
import json

COOKIEFILE = 'cookies.lwp'
# the path and filename to save your cookies in

cj = None
ClientCookie = None
cookielib = None

# Let's see if cookielib is available
try:
    import cookielib
except ImportError:
    # If importing cookielib fails
    # let's try ClientCookie
    try:
        import ClientCookie
    except ImportError:
        # ClientCookie isn't available either
        urlopen = urllib2.urlopen
        Request = urllib2.Request
    else:
        # imported ClientCookie
        urlopen = ClientCookie.urlopen
        Request = ClientCookie.Request
        cj = ClientCookie.LWPCookieJar()

else:
    # importing cookielib worked
    urlopen = urllib2.urlopen
    Request = urllib2.Request
    cj = cookielib.LWPCookieJar()
    # This is a subclass of FileCookieJar
    # that has useful load and save methods

if cj is not None:
# we successfully imported
# one of the two cookie handling modules

    if os.path.isfile(COOKIEFILE):
        # if we have a cookie file already saved
        # then load the cookies into the Cookie Jar
        cj.load(COOKIEFILE)

    # Now we need to get our Cookie Jar
    # installed in the opener;
    # for fetching URLs
    if cookielib is not None:
        # if we use cookielib
        # then we get the HTTPCookieProcessor
        # and install the opener in urllib2
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)

    else:
        # if we use ClientCookie
        # then we get the HTTPCookieProcessor
        # and install the opener in ClientCookie
        opener = ClientCookie.build_opener(ClientCookie.HTTPCookieProcessor(cj))
        ClientCookie.install_opener(opener)



values = {
"lsd":"",
"email":"gnowiefngklsdjfg@gmail.com",
"pass":"zxcvzxcvzxcv",
"default_persistent":0,
"charset_test":"",
"timezone":480,
"lgnrnd":"",
"lgnjs":"",
"locale":"en_US"
}

def get_shared_connections(id1, id2):
  u = "http://www.facebook.com/ajax/browser/dialog/mutual_friends/?uid="+str(id1)+"&node="+str(id2)+"&__a=1"
  req = Request(u)
  response = urllib2.urlopen(req)
  f = open("res.html", "w")
  print response.info()
  res = response.read()
  f.write(res)
  f = open("res.json", "w")
  j = json.loads(res[len("for (;;);"):])
  f.write(str(j))

data = urllib.urlencode(values)
# req = urllib2.Request('https://www.facebook.com/login.php?login_attempt=1', data)
# response = urllib2.urlopen(req)
# print response.read()

theurl = 'https://www.facebook.com'
# an example url that sets a cookie,
# try different urls here and see the cookie collection you can make !

txdata = None
# if we were making a POST type request,
# we could encode a dictionary of values here,
# using urllib.urlencode(somedict)

txheaders =  {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
# fake a user agent, some websites (like google) don't like automated exploration

try:
    req = Request(theurl, txdata, txheaders)
    # create a request object

    handle = urlopen(req)
    # and open it to return a handle on the url

except IOError, e:
    print 'We failed to open "%s".' % theurl
    if hasattr(e, 'code'):
        print 'We failed with error code - %s.' % e.code
    elif hasattr(e, 'reason'):
        print "The error object has the following 'reason' attribute :"
        print e.reason
        print "This usually means the server doesn't exist,"
        print "is down, or we don't have an internet connection."
    sys.exit()

else:
    print 'Here are the headers of the page :'
    print handle.info()

    req = Request('https://www.facebook.com/login.php?login_attempt=1', data)
    response = urllib2.urlopen(req)
    f = open("login.html", "w")
    f.write(response.read())
    get_shared_connections(617147, 100001259293395)

    # handle.read() returns the page
    # handle.geturl() returns the true url of the page fetched
    # (in case urlopen has followed any redirects, which it sometimes does)

print
if cj is None:
    print "We don't have a cookie library available - sorry."
    print "I can't show you any cookies."
else:
    print 'These are the cookies we have received so far :'
    for index, cookie in enumerate(cj):
        print index, '  :  ', cookie
    cj.save(COOKIEFILE)                     # save the cookies again
