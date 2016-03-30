def get_url_info(url, seg):
	import tldextract
	url_info = tldextract.extract( url )
	#get subdomain
	if(seg == 1):
		return url_info.subdomain
	#get domain
	if(seg == 2):
		return url_info.domain
	#get suffix
	if(seg == 3):
		return url_info.suffix
	#get domain and suffix
	if(seg == 4):
		return url_info.domain+'.'+url_info.suffix

