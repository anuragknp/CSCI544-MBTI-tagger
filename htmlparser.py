from HTMLParser import HTMLParser



# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self, file):
      HTMLParser.__init__(self)
      self._tweet_found = False
      self._handle_found = False
      self._tweet = ''
      self.__handle = ''
      self._file = file


    def __get_class(self, attrs):
      for attr in attrs:
        if attr[0] == 'class':
          return attr[1]

    def handle_starttag(self, tag, attrs):
        if self.__get_class(attrs) == 'js-tweet-text-container':
          self._tweet_found = True
          self._tweet = ''
        if self.__get_class(attrs) == 'username js-action-profile-name':
          self._handle_found = True
	  self._handle = ''

    def handle_endtag(self, tag):
      if self._tweet_found and tag == 'div':
        self._tweet_found = False
	self._file.write(self._handle.replace('\n', '')+'|$|'+self._tweet.replace('\n', '')+'\n')
      if self._handle_found and tag == 'span':
	self._handle_found = False

    def handle_data(self, data):
        if self._tweet_found:
	  self._tweet += data
	if self._handle_found:
	  self._handle += data
