#coding:utf-8
from bs4 import BeautifulSoup, Tag


class Html_Parse(object):
    papers = []
    content={'tag':'','content':''}#tag = text,code,img
    @classmethod
    def parse(self,response):

        soup = BeautifulSoup(response, "lxml")#,'html.parser',from_encoding='utf-8'
        pres = soup.findAll('pre')
        for pre in pres:
            pre.name ='p'
            pre['code']='yes'
        # print soup
        ps = soup.findAll('p')
        for p in ps:
            img = p.img
            if img !=None:
                self.content={'tag':'img','content':img['src']}
                self.papers.append(self.content)

            if p.get('code')=='yes':
                self.content={'tag':'code','content':p.text.replace('&nbsp;','').strip()}
                self.papers.append(self.content)
            elif p.span != None:
                spans = p.findAll('span')#找到所有的span标签
                for span in spans:
                    # print span.text
                    if span.get('style').find('color')!=-1:
                        # del span['style']
                        # span.name='color'
                        if span.string!=None:
                            span.string = 'c_start'+span.string+'c_end'
                links =p.findAll('a')
                for link in links:
                    if link.string!=None:
                        link.string = '['+link.string+']'+'('+link.string+')'
                self.content={'tag':'text','content':p.text.replace('&nbsp;','').strip()}
                self.papers.append(self.content)
            else:
                self.content={'tag':'text','content':p.text.replace('&nbsp;','').strip()}
                self.papers.append(self.content)

        return self.papers
