import requests
from bs4 import BeautifulSoup
s = requests.session()

payload ={
    'log' : 'admin',
    'pwd' : '123456aA',
}

request  = s.post("http://45.79.43.178/source_carts/wordpress/wp-login.php?loggedout=true&wp_lang=en_US",data=payload)
r=s.get("http://45.79.43.178/source_carts/wordpress/wp-admin/").text

soup = BeautifulSoup(r,'lxml')
tk=soup.find('span',class_='display-name').text

print(tk)