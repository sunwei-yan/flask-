# coding=utf-8

from random import randint
from re import X
from flask import Flask,render_template
from flask import Flask, render_template, request, url_for, flash, redirect

app=Flask(__name__)
import sqlite3

def get_db_connection():
    # 创建数据库链接到database.db文件
    conn = sqlite3.connect('database.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn
def test():
    import requests
    from lxml import etree
    url="https://www.gushiwen.cn/"
    header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    resp=requests.get(url=url,headers=header)
    html=etree.HTML(resp.text)
    s=' '
    for i in range(75):
        xpaths="/html/body/div[2]/div[2]/div[2]/div[2]/a["+str(i)+"]/text()"
        biaoti=html.xpath(xpaths)
        s=s+"\n"+str(biaoti)
    return s
def dyttre():
    from ntpath import join
    import re
    import requests
    from lxml import etree
    s=['https://m.dytt8.net/']
    t=''
    for i in range(1,2):
        
        url="https://m.dytt8.net/html/gndy/dyzz/list_23_"+str(i)+".html"
        resp=requests.get(url)
        resp.encoding='gb2312'
        html=etree.HTML(resp.text)
        for x in range(1,25):
            final=html.xpath("/html//table["+str(x)+"]//tr[2]//b/a/text()")
            finalweb=html.xpath("/html//table["+str(x)+"]//tr[2]//b/a/@href")
            # print(final)
        
            x=s+finalweb
            w=''.join(x)
            t=t+str(final)+"\t"+str(w)
    return t 
def jtcsm():
    

    l1=['[杭州 湾]第一食堂', '[本部北区]星美乐（自助水果捞.自助沙拉简餐）', '[本部南区]问茶', '宁波鸿大汽车驾校。新学期优惠！！！', '[本部南区]酸奶大麻花 （美食广场22号）', '[本部南区]巴比汉堡', '[本部南区]美食坊', '[本部南区]兰庆鸡子馃', '[本部北区]千里香馄饨', '[本部南区] 渝小碗.酸辣粉（第 五食堂内)', '[本部南区]淮南牛肉汤（美食广场4号）', '[本部南区]老孙饭堂', '[本部南区]鲜椒鸡 火锅鸡(第四食堂内）', '[本部南区]小胖哥，卤肉饭 （美食广场11号店）', '[本部南区]神炖特工焗海鲜焖饭（美食广场9号）', '[本部南区] 川渝重庆小面～杂酱面【美食广场15号焗面焗】', '[本部南区]缘 味先石锅焗饭(美食广场17号)', '[本部南区]土耳其烤肉饭、双拼套餐饭（美食广场3号焗）', '[本部南区 一品香(美食广场19号)焗', '[本部南区]串烤粥妹 (美食广场20号)焗', '[本部南区]一姐骨汤麻辣烫焗（美食广场25号）', '[本部北区]第二食堂（饭饭帮食尚餐厅）', '[本部北区]卡士多汉堡', '[本部北区 ]麦香园', '[本部北区]蜀一蜀二', '[本部南区]622鸡柳年糕薯条（美食广场2号）', '[本部南区]Do eat', '[本部南区]第四食堂', '[本部南区]翻滚吧小火 锅、小干锅']
    l2=[ '[本部南区]港式炒饭&过桥米线(美食广场21号)', '[本部南区]灌汤锅贴（第四食堂内)', '[本部南区]灌汤煎包', '[本部南区]豪大大', '[本 部南区]何记酸菜鱼（美食广场16号）', '[本部南区]淮南牛肉汤', '[本部南区]黄焖鸡米饭(美食广场14号)', '[本部南区]卡萨宝披萨意面(美食广场13号）', '[本部南区]粮缘粥铺', '[本部南区]玲珑坊(各类套餐饭）', '[本部南区]美之味蛋糕店', '[本部南区]莫问斋黄焖鸡米饭（第五食堂）', '[本部南区]如 意馄饨(美食广场24号店)', '[本部南区]沙县小吃', '[本部南区]陕西美食（美食广场1号）', '[本部南区]上汤沙锅', '[本部南区]私房饺子馆( 美食广场8 号）', '[本部南区]泰式咖喱饭（美食广场6号）', '[本部南区]瓦罐汤杨传老厨瓦缸汤饭', '[本部南区]魏小宝', '[本部南区]无骨小份烤鱼饭（美食广场12号）', '[本部南区]有嘉小吃', '[本部南区]正新鸡排&汉堡套餐&小吃(美食广场23号)', '[本部南区]煲来乐', '[杭州湾]巴比汉堡', '[杭州湾]黄焖鸡米饭 美食城三楼店', '[杭州湾]麦迪堡', '[杭州湾]食面八方', '[本部南区]杂粮鱼粉（美食广场18号）', '[杭州湾]龍门花甲 纸上烤鱼', '[杭州湾]芝佳格芝士 焗饭', '[杭州湾]F+牛肉饭']
    l3=['[杭州湾]《炸串》', '[杭州湾]八扣碗', '[杭州湾]茶扣奶茶吧', '[杭州湾]锅石头', '[杭州湾]韩国料理', '[杭州湾]吉阿 婆麻辣烫', '[杭州湾]可鱼可饭无刺酸菜鱼米饭', '[杭州湾]美妙食刻煎饼（汉堡.炸鸡）', '[杭州湾]面疙瘩~手工石磨肠粉', '[杭州湾]魔饭大叔', '[杭州 湾]牛肉汤', '[杭州湾]千寻寿司/面皮', '[杭州湾]土耳其烤肉饭', '[杭州湾]闻净铁板', '[杭州湾]无骨烤鱼捞饭', '[杭州湾]享瘦四季轻食', '[杭州湾] 鸭食代', '[杭州湾]缘味先石板饭', '[杭州湾]镇江锅盖面', '[杭州湾]正宗纯手工水饺',]
    l6=['[杭州湾]重庆小面', '[杭州湾]粥粥好运（手抓饼，灌汤小笼包 ）', '[本部北区]F⁺牛肉饭', '[杭州湾]金马排挡-实惠-良心-❤', '[本部北区]城市麦田烘培', '[本部北区]第一食堂', '[本部北区]哈喽炒饭炒面（成都串 串香）', '[本部北区]汉堡派、韩式炸鸡', '[本部北区]喝吧便利店', '[本部北区]教工办公订水', '[本部北区]美润东北水饺', '[本部北区]酸菜鱼米饭（ 第二食堂内）', '[本部北区]鲜花水果店', '[本部北区]新发现麻辣烫', '[本部北区]自选轻食简餐（第二食堂内）', '[本部北区]嗨族拌面', '[本部南区 ]第五食堂', '[本部南区]教工办公订水']
    l4=['[本部南区]孔明村麻辣香锅', '[本部南区]启真超市', '[本部南区]桶装订水', '[本部南区]缙云烧饼', '[杭州湾 ]6号楼沙县小吃', '[杭州湾]八号便档/套餐/砂锅/炒饭/盖浇饭', '[杭州湾]巴比馒头', '[杭州湾]百年面霸', '[杭州湾]馋嘴屋', '[杭州湾]超人龙虾', '[杭州湾]灌汤煎饺', '[杭州湾]海盗船小吃店', '[杭州湾]嘿糖奶茶', '[杭州湾]黄焖鸡米饭', '[杭州湾]集客咖啡', '[杭州湾]佳美清真', '[杭州湾]教工办 公订水', '[杭州湾]丽丽饼店', '[杭州湾]粮缘茶饮', '[杭州湾]麻辣香锅美食', '[杭州湾]麦可茶奇', '[杭州湾]麦香烘焙', '[杭州湾]蜜果奶茶', '[杭州 湾]桥头排骨', '[杭州湾]如意馄饨', '[杭州湾]食尚潮流(水煮酸汤肥牛系列 盖浇饭 套餐饭)', '[杭州湾]酸菜鱼', '[杭州湾]台湾饭团', '[杭州湾]天府家 园', '[杭州湾]田园水果店', '[杭州湾]桶装订水', '[杭州湾]五谷鱼粉', '[杭州湾]西里巷铁板厨房', '[杭州湾]小米餐厅', '[杭州湾]星期八美食', '[杭 州湾]幸福舌尖 粥 包子 粽子 手抓饼 饭团 套餐饭', '[杭州湾]张亮麻辣烫', '[杭州湾]怡欣果园', '[杭州湾]缙云烧饼', '[杭州湾]甬金麻辣香锅', '[象 山校区]free轻脂', '[象山校区]巴必屋，炸鸡汉堡']
    l5=[ '[象山校区]半亩果园', '[象山校区]包大哥', '[象山校区]东北烤冷面（颐佳生活餐饮）', '[象山校 区]鸡本部：鸡排小吃便当', '[象山校区]鸡本部烤酸奶', '[象山校区]麦界风手工烘焙', '[象山校区]奈思大咖餐厅', '[象山校区]牛杂面、牛肉面', '[象 山校区]清清美食 麻辣烫', '[象山校区]清真美食2', '[象山校区]三楼快餐（颐佳生活餐饮）', '[象山校区]手工水饺', '[象山校区]蜀道麻辣香锅 麻辣烫', '[象山校区]淘小果（颐佳生活餐饮）', '[象山校区]脱丹炒饭&烧饼', '[象山校区]味思餐厅', '[象山校区]味思餐厅2', '[象山校区]味思餐厅早点来', '[象山校区]锡纸花甲粉：桂林米粉', '[象山校区]闲散江湖', '[象山校区]香米米牛肉饭', '[象山校区]小鱼儿酸菜鱼', '[象山校区]遇见你 轻食店', '[象 山校区]缘味先石锅饭', '[象山校区]周周龙虾小炒（颐佳生活餐饮）', '[象山校区]厝内小眷村', '手抓饼/鲜包/铁板炒', '[本部北区]桶装订水']
    lx=[]
    
    lx.append(l1)
    lx.append(l2)
    lx.append(l3)
    lx.append(l4)
    lx.append(l5)
    lx.append(l6)
    n=randint(1,5)
    s=randint(1,len(lx[n])-1)
    # print(n,s)
    # print(lx[n][s])
    return(str(lx[n][s]))
@app.route('/')
def index():
    conn = get_db_connection()

    # 查询所有数据，放到变量posts中
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return  render_template('index.html',posts=posts)
@app.route('/posts/new', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            return('标题不能为空!')
        elif not content:
            return('内容不能为空')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('new.html')

@app.route('/日志')
def rizhi():
    return render_template('日志.html')
@app.route('/代码')
def daima():
    return render_template('代码.html')
@app.route('/工具箱')
def gjx():
    return render_template('工具箱.html')
@app.route('/资助')
def zz():
    return render_template('资助.html')
@app.route('/404notfound')
def four():
    return render_template('not found.html')
@app.route('/404notfound')
def js():
    return render_template('项目介绍.html')
@app.route('/test')
def tests():
    x=test()
    s=dyttre()
    return render_template('test.html',x=x,s=s)
@app.route('/jtcsm')
def jtcsmh():
    x=jtcsm()
    return render_template('jtcsm.html',x=x)
@app.route('/admin7905')
def houtai():
    conn = get_db_connection()

    # 查询所有数据，放到变量posts中
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return  render_template('admin.html',posts=posts)
@app.route('/delt',methods=('POST','GET'))
def delt():
    ids=request.args.get('id')
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id=?',(ids,))
    conn.commit()
    conn.close()
    print(ids+"this")
    return redirect(url_for('houtai'))
# @app.route('/new', methods=('GET', 'POST'))
# def new():
#     conn = get_db_connection()

#     # 查询所有数据，放到变量posts中
#     posts = conn.execute('SELECT * FROM posts').fetchall()
#     conn.close()
#     return  render_template('1.html',posts=posts)
if __name__ == '__main__':
    app.debug=True
    app.run()
    
    
