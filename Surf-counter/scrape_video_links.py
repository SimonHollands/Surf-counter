from bs4 import BeautifulSoup
import requests

class ScrapeVideoLinks:

    def __init__(self, camrewind_link,tofind_str='20191027T', occurance_n=3):
        self.main="https://camrewinds.cdn-surfline.com/live/wc-venicebeachclose.stream."
        self.camrewind_link=camrewind_link
        self.tofind_str =tofind_str
        self.page = requests.get(self.camrewind_link)
        self.soup = BeautifulSoup(self.page.content)
        self.soup_str=str(self.soup)



    def nth(self,Xstr):
        first_start = Xstr.find(self.tofind_str)
        first_end = first_start + len(self.tofind_str)
        
        second_start = first_end + Xstr[first_end:].find(self.tofind_str)
        second_end = second_start + len(self.tofind_str) 

        third_start = second_end + Xstr[second_end:].find(self.tofind_str)
        third_end = third_start + len(self.tofind_str) 
        return Xstr[third_end:third_end+9]

    def get_link(self):
        self.end_of_link=self.tofind_str+self.nth(self.soup_str)+'.mp4'
        return self.main+self.end_of_link

v=ScrapeVideoLinks("http://www.surfline.com/surfdata/video-rewind/video_rewind.cfm?id=146850&camAlias=wc-venicebeachclose&CFID=459565&CFTOKEN=85392160")
print(v.get_link())

