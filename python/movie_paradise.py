# -*- coding: utf-8 -*-

import urllib2
import re
import MySQLdb
from bs4 import BeautifulSoup

global next_page_addr
global counter

def get_page(page_addr):
    global next_page_addr
    request = urllib2.Request("http://www.ygdy8.net/html/gndy/dyzz/" + page_addr)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, from_encoding="GBK")
    table = soup.find_all('a', attrs={'class':'ulink'})

    get_next_page(soup)

    return table

def get_next_page(soup):
    global next_page_addr
    next_page = soup.find_all('select', attrs={'name':'sldd'})
    value = next_page[0].find_all('option', attrs={'selected':True})
    next_page_addr = value[0].next_sibling.next_sibling
    next_page_addr = next_page_addr.get("value")

def page_show(table):
    table_len = len(table)
    for movie_no in range(0,table_len):
        address = "http://www.ygdy8.net" + table[movie_no].get('href').encode("utf-8")
        print table[movie_no].string
        print "Address: %s" %address

def assemble_movie_addr(table):
    table_len = len(table)
    for movie_no in range(0,table_len):
        address = "http://www.ygdy8.net" + table[movie_no].get('href').encode("utf-8")
        get_movie_info(address)

def get_movie_info(address):
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",\
                 "Referer": 'http://www.ygdy8.net'}
    request = urllib2.Request(address, headers=i_headers)
    response = urllib2.urlopen(request)

    html = response.read()
    soup = BeautifulSoup(html, from_encoding="GBK")

    name = movie_info_name(soup)
    print name

    download_address = movie_info_address(soup)
    print download_address

    print("--------------------------------")

    mysql_link(name,download_address)


def mysql_link(name,address):
    global counter
    name = name.encode("utf-8")
    address= address.encode("utf-8")

    T = (counter,name,address)
    
    counter = counter + 1
    conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='kuailemei1tian',
        db ='test',
        charset="utf8",
    )
    cur = conn.cursor()
    w = 5
    cur.execute("insert into Movie values (%s,%s,%s)",T)
    cur.close()
    conn.commit()
    conn.close()


def movie_info_address(soup):
    download_addr = soup.find_all('td', attrs={'style':'WORD-WRAP: break-word'})
    return download_addr[0].contents[0].get('href')

def movie_info_name(soup):
    name = soup.title.string
    return name

if __name__ == "__main__":
    global counter
    global next_page_addr
    counter = 1
    next_page_addr = "index.html"

    while(next_page_addr != None):
        table = get_page(next_page_addr)
        assemble_movie_addr(table)
        #page_show(table)
