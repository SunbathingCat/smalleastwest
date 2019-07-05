import requests
import re
import os
from lxml import etree

class ThunderSniffer():
    def __init__(self,key_word,pages=1):
        self.wd = key_word
        self.pns = pages
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
        }
        self.name = key_word
    def baidu(self):
        '''
        百度搜索关键词
        :return: 搜索结果链接列表
        '''
        urls = []
        wd = self.wd
        for p in range(self.pns):
            pn = p * 10
            url = 'https://www.baidu.com/s?wd={}&pn={}'.format(wd,pn)
            response = requests.get(url=url, headers=self.headers)
            list_html = response.text
            html = etree.HTML(list_html)
            h3 = html.xpath('//h3/a/@href')
            for h in h3:
                if re.match('http://www.baidu.com/link\?url=',h):
                    urls.append(h)
        return urls

    def url_smeller(self,urls):
        '''
        传入单个链接或一个列表链接
        :param urls:
        :return: 返回这些链接网页内所有子链接
        '''
        if isinstance(urls,str):
            response = requests.get(url=urls, headers=self.headers)
            text = response.text
            url_list = re.findall('https://[a-zA-Z0-9/\.]+?\.html',text)
            e_url_list = re.findall('/[a-zA-Z0-9/\.]+?\.html',text)
            print(url_list)
            print(e_url_list)
        elif isinstance(urls,list):
            pass
        else:
            pass

    def res_smeller(self,url):
        '''
        传入单个链接
        :param url:
        :return: 返回此链接网页内所有 资源链接
        '''
        response = requests.get(url=url, headers=self.headers)
        text = response.text
        print(text)
        thunder_urls = re.findall('thunder://[a-zA-Z0-9]+',text)
        ed2k_urls = re.findall('ed2k://.*?\|/',text)
        magnet_urls = re.findall('magnet:\?xt=urn:btih:[a-zA-Z0-9]{40}',text)
        print(thunder_urls)
        print(ed2k_urls)
        print(magnet_urls)


    def write_to_html(self,data):
        '''
        传来数据字典写入 result.html 中
        :param data: data[{'name':' ','link':' '},{'name':' ','link':' '},{'name':' ','link':' '},{'name':' ','link':' '}]
        :return:
        '''
        result = self.name
        html_part1 = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{}</title></head><body>'.format(result)
        html_part2 = ''
        for one in data:
            name = one['name']
            link = one['link']
            line = '<p><a href="{}">{}</a></p>'.format(link,name)
            html_part2 += line
        html_part3 = '</body></html>'
        html = html_part1 + html_part2 + html_part3
        with open('result.html','w') as f:
            f.write(html)
        pass

    def analysis_magnet(self,magnet):
        '''
        解析资源链接
        :param magnet:
        :return: 资源相关信息
        '''
        pass

    def deep_search(self,depth=1):
        '''
        深度搜索
        :param depth: 搜索深度，默认为1层
        :return: 返回 depth 层深度的所有链接
        '''
        search_list = self.baidu()
        data = {0:search_list}
        for i in range(depth):
            data[i+1] = self.url_smeller(data[i])
        return data[depth]