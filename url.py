from bs4 import BeautifulSoup
import request

source = request.get( "youtube-url" ).text 
soup = BeautifulSoup( source, "lxml" )
soup.prettify

try:
  vid_src = article.find( "iframe", class_="youtube-player" ) ['src']
  vid_id = vid_src.split( "/" ) [4]
  vid_id = vid_id.split( "?" ) [0]
  yt_link = f" https://youtube.com?v={vid_id}
  
except Exeption as e:
  yt_link = None

