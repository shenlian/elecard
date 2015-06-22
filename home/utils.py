# Create your views here.
# coding=utf-8

import qrcode  
import Image  
import os  

def gen_ecard(vstr,path):
    # print vstr
    qr = qrcode.QRCode(
        # version值为1~40的整数,控制二维码的大小,(最小值是1,是个12*12的矩阵)
        # 如果想让程序自动确定,将值设置为 None 并使用 fit 参数即可
        version=2,
        # error_correction: 控制二维码的错误纠正功能,可取值下列4个常量
        #   ERROR_CORRECT_L: 大约7%或更少的错误能被纠正
        #   ERROR_CORRECT_M(默认): 大约15%或更少的错误能被纠正
        #   ERROR_CORRECT_Q: 大约25%或更少的错误能被纠正
        #   ERROR_CORRECT_H: 大约30%或更少的错误能被纠正
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        # 控制二维码中每个小格子包含的像素数
        box_size=4,
        # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4,是相关标准规定的最小值)
        border=3,
    )

    # 将vCard数据填入qr
    qr.add_data(vstr)

    qr.make(fit=True)

    # 生成图片
    img = qr.make_image()

    # 将图片存入指定路径文件
    img.save(path)

def get_ecard_path(name,phone,email,address,url,position,card_id):
    begin = "BEGIN:VCARD\n"
    ename = ephone = eemail = eaddress = eurl = etitle =""
    if name:
        ename = "FN:%s\n" % name
    if phone:
        ephone = "TEL;TYPE=cell:%s\n" % phone
    if email: 
        eemail = "EMAIL:%s\n" % email
    if address:
        eaddress = "ADR;TYPE=WORK:;%s\n" % address
    if url:
        eurl = "URL:%s\n" % url
    if position:
        etitle = "TITLE:%s\n" % position
    end = "END:VCARD\n"

    current_root = os.path.dirname(__file__)

    vstr = begin + ename + ephone + eemail + eaddress + eurl + etitle +end
    path = os.path.join("/home/sl/workspace/elecard/media/uploadfile/qrcode", "%s.png" % card_id)
    print path
    gen_ecard(vstr,path)
    return path
if __name__ == "__main__":
    get_ecard_path("杨宝玲","15250413229","","yang.bl@qq.com","http://oriental13.lofter.com","东南大学学生","1")
