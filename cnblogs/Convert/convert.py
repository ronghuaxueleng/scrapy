#coding:utf-8

class Convert(object):

    @classmethod
    def convert(self,papers):
        str = ''
        with open('markdown.md','w') as file_writer:
            for p in papers:
                if p['tag']=='text':
                    str = p['content'].replace('c_start','**').replace('c_end','**')
                    pass
                elif p['tag']=='code':
                    str = '```'+'\r\n'+p['content']+'\r\n'+'```'

                else:
                    str = '![](%s)'%(p['content'])
                    str = '\r\n'+str+'\r\n'

                file_writer.write(str.encode('utf-8'))
                file_writer.write('\r\n'.encode('utf-8'))

        file_writer.close()

