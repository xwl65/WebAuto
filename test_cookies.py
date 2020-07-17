# Generated by Selenium IDE
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test():
    def setup_method(self, method):
        #chromedriver的端口
        chrome_options = Options()
        #和浏览器打开的调试端口进行通信
        #浏览器要使用 --remote-debugging-port=9222 开启调试
        #chromedriver也需要开口
        chrome_options.debugger_address = "127.0.0.1:9222"
        #如下两句加上有很大的区别。后面的如果不加上，那么就不会产生服用的效果
        #第一句会弹出一个新的浏览器。
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Chrome(options=chrome_options)

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "su").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 – 测试开发工程师的黄埔军校").click()
    def test_xwork(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #self.driver.find_element(By.ID,"menu_contacts").click()
        print(self.driver.get_cookies())
        db = shelve.open("cookies")
        #cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851900816845'},
#{'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '5862822912'},
#{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Ie0tt3TF0qJzTQtQi0q987dN0pEh6nlib4jW6ST8D4jVAIeIhMdzMSz2vfyBH0UP'},
#{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
#{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'WUz4ilGoiQDsjxOprGKgP0B7_L6dTcB8MdK76XayC3sZ6CKETMQigdLMrQUWJ-dPme8Rj64B8ZaAZjbXC4vFNgSM0VSTcsX4EtsdBaRUa_i3CHRW5P71BrfIVNc1UDee3Zqb6TAxIFF1yWyLe6dcLOdCxxZhEr-I4UdGJrrCsEhR7aVuitDp25ZYG64frpPQFYyFk9k3b73gE7pQJNFhxomI3_kvYHbTqT7OkFrwiTpplehQXygKffn9AqGlaNke3pX7M2w5WvMcqTYt76GG1A'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},
#{'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s978163538'},
#{'domain': '.qq.com', 'expiry': 1595000515, 'httpOnly': False, 'name': 'webwx_data_ticket', 'path': '/', 'secure': True, 'value': 'gSftQlhoDaeAXP43hFzLCBB4'},
#{'domain': '.qq.com', 'expiry': 1595053527, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1354939.1594901085'},
#{'domain': '.qq.com', 'expiry': 1658039127, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.132793747.1594901085'},
#{'domain': '.work.weixin.qq.com', 'expiry': 1597561943, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'},
#{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8016378'},
#{'domain': '.qq.com', 'expiry': 1597388460, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '492980423'},
#{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '33235628131482192'},
# {'domain': '.work.weixin.qq.com', 'expiry': 1626437089, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1594901084'},
# {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325044149434'},
# {'domain': '.qq.com', 'expiry': 1910194450, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_492980423'},
# {'domain': '.qq.com', 'expiry': 9141255873, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': 'e85329aa24e6bcb3'},
# {'domain': '.work.weixin.qq.com', 'expiry': 1594998615, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
# {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '6afe3e91cb3390edba4528907e699caa5df7a9eeb8de4c4c2484116b4655193a'},
# {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '6089502817'},
# {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '492980423'},
# {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '2ECFeLFsHs'},
# {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851900816845'},
# {'domain': 'work.weixin.qq.com', 'expiry': 1594998615, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '23stp6u'}]
 #       db["cookies"] = cookies

        cookies = db["cookies"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def test_wework(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 创建或者打开一个数据库
        db = shelve.open("cookies")
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/',
        # 'secure': False, 'value': 'QggRK2Smqd5_lH6k6RDLimOx5yJ2Lfg5Gf8irncrB648gbArqGhg3bPA5k_NlXPF'},
        # {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5484050'},
        # {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850888546920'},
        # {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850888546920'},
        #{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325091099135'},
        #{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '16764371053223907'},
        #{'domain': 'work.weixin.qq.com', 'expiry': 1594932599, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '2plvpn'},
        # {'domain': '.work.weixin.qq.com', 'expiry': 1594932599, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
        # {'domain': '.work.weixin.qq.com', 'expiry': 1597497421, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'},
       # {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'exywTkwmcl'},
       #  {'domain': '.qq.com', 'expiry': 1597489128, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000db2ca3a4bb964b0eed65356b900e1beae1f7a34e9e1b87fec2788e87760b807c4cfa59f7f489949c'}, {'domain': '.qq.com', 'expiry': 1596428506, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '742976679'}, {'domain': '.qq.com', 'expiry': 1656768418, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1486340881.1579059579'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '1256305343'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '21184e650f6a6683b1089473bd27234cc787221ed0761e762ef7c706c95c1153'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'SSvtaG0HPX3LrumGQo-0d8z8F9NDIt2-SJar2k4JleK8PcHpjPYXXt2qyrgbY5zCAiTy4KEuHlMTID5PRPO-ibY9A298-8R7Rg05GZ0CvuGsu_LU2mYtkkbpM1kHBlNrdFf1zbkZlOQ4P6Y35tIelk5ewe1ePJ9zXUcDsxuTVU-9Ocwk4YT31_gwl4WtraACGf4-ngdcxZ4GrTw3s5b9g5ktpP6kg9bi1sL_noxgoRxxowU9YO2pGe1X8_oKqXBVQmrSNTuQObkteGYkLqmI_w'}, {'domain': '.qq.com', 'expiry': 1597489128, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o1256305343'}, {'domain': '.qq.com', 'expiry': 1897608032, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': 'db5af6172ed41f4b'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '535707648'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1625229244, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1591409096,1593693242'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '5034123288'}]
        #将数据存储到 shelve 中
        #db["cookies"] = cookies
        # 取出数据
        cookies = db["cookies"]
        # 获取 cookies
        # print(self.driver.get_cookies())
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            # 把字典加入到 driver 的 cookie 中
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        db.close()

