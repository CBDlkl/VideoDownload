import urllib.request
import json,sys
from pyquery import PyQuery as pq

host = "http://edu.iqianyue.com/%s"

def Schedule(a,b,c):
       per = 100.0 * a * b / c
       if per>100:
           per = 100
           print('下载完成！')
       sys.stdout.flush()
       sys.stdout.write('%.2f%%' % per+ '\r')
       sys.stdout.flush()

def openUrl(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1")
    req.add_header("Cookie","PHPSESSID=ftk3id35tbaijrlhj5pr5clvg6")
    req.add_header("Referer","http://edu.iqianyue.com/index_course_study_cid_11")
    req.add_header("Host","edu.iqianyue.com")
    r = urllib.request.urlopen(req)
    rootHtml = r.read().decode('utf-8')
    return rootHtml

doc = pq(openUrl("http://edu.iqianyue.com/index_course_study_cid_11_lid_1"))
for i in doc("h4 a"):
    print(host%pq(i).attr('href'), pq(i).text())
    doc = pq(openUrl(host%pq(i).attr('href')))
    video_id = doc(".col-md-8").eq(0).find("div").eq(0).attr("id").replace("id_video_container_","")
    js_json = urllib.request.urlopen("http://play.video.qcloud.com/index.php?interface=Vod_Api_GetPlayInfo&1=1&file_id=%s&app_id=1251728304&refer=edu.iqianyue.com"%video_id).read().decode('utf-8')
    vurl = json.loads(js_json)['data']['file_info']['image_video']['videoUrls'][0]['url']
    urllib.request.urlretrieve(vurl, "机器学习_%s.mp4"%pq(i).text(),Schedule)



