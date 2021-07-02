from kivy.base import Builder
from kivy.base import runTouchApp
from kivy.uix.image import AsyncImage
runTouchApp(Builder.load_string("""
AnchorLayout:
    canvas:
        Color:
            rgb:1,2,3,1
        Rectangle:
            pos:self.pos
            size:self.size
    AsyncImage:
        source:'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffsb.zobj.net%2Fcrop.php%3Fr%3D4cwD2BMYAVvjfev3xWihlC_tDSdF9DXQdiO_5ROC_WMhiLkjxzfcA2Ck5WuPXAgeWOIZMzqhbUHF_6SSMBXx_EQd7K82MhXRQBFqMqGErjsCnRmLWvMXTV072TjrSE4AVU-aAnjEbog_p6ey&f=1&nofb=1'
        size_hint:None,None
        size:dp(400),dp(500)
        anim_delay:4
        
    
"""))