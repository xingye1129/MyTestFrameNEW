import requests

session = requests.session()
requests.packages.urllib3.disable_warnings()
session.headers['content-type'] = 'application/json; charset=utf-8'
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
session.headers['x-zse-83'] = '3_2.0'
session.headers['cookie'] ='_zap=8e2a124a-7c3d-4736-95fd-dc69b0babbe8; d_c0="AJBYoNRf9hCPTlbrRnvVYDbwoHVNeXwaiZ8=|1584191808"; _ga=GA1.2.1245130151.1584191810; _xsrf=hcmMDHf0UqUlHbK1rdt0i43Dagck4x4F; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1584191809,1584517227; _gid=GA1.2.515130571.1584517227; tst=r; KLBRSID=53650870f91603bc3193342a80cf198c|1584518875|1584517225; _gat_gtag_UA_149949619_1=1; capsion_ticket="2|1:0|10:1584518875|14:capsion_ticket|44:ZjU0MGNiZDVlMjBiNGY5ZDhhNDdjMWM3N2RjYmUzNzE=|c6d77518ba9b2cb65bf5fcea8949aa61d36475bdfcddf21e4f20442b78ae7ae5"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1584518877'
print(session.headers)


res = session.get('https://www.zhihu.com/api/v3/oauth/captcha?lang=cn')
print(res.text)

res = session.post('https://www.zhihu.com/api/v3/oauth/sign_in',data='KbOG-ge8UBXxcTYq8LkM39L1e9oY2BH0sTYqk4R92Ltxg_pKzbN924U0g6S_EGO1BBH0c79hJvOfELp1tUNKEecGoBXxcTYhAhYqk4__2Ltxg0pMK9p1sUCBi9V9XqYhzqNMcCeMsBSYkBF0z_e0g4e8kCV92vCmKC3qk47mF9LxgMNmZrNqk4R92LkfiqxG1wS8S79hbH2X9wLLXgO8fbS0g_xO-GoMBwxMS79hJvOfEXVM1_Yqk4RyoTYxe720YHt924_BJwx9kCSMsBF0gQu0k7FXbRF08LYySHuyQ82Xo0Nq8TO86e9ycXOfNCSq8L20k0U0UCNm2LfB8CpGU9eBDqppkLn8zG3ZchL1iDpuJvS8EqYhggHMcvOOSTYhYLYyQQ906X2pe7Yqm_e0giCmU9VOgcO1KBF0g6HM-GVO2wxMEqYhgDCKevgVEwNMqBF0giU0gutpr0YBmXNqgq982TNXNqtqfXY8SQr8o8SYFq28EqYhHqeVebSYDrS8:',verify=False)

print(res.text)