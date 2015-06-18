# Create your views here.
# coding=utf-8

import qrcode  
import Image  
import os  

def gen_ecard(vstr):
    print vstr
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
    img.save("/home/sl/download/test.png")

if __name__ == "__main__":
    begin = "BEGIN:VCARD\n"
    name = "FN:沈潋\n"
    phone = "TEL:522292222\n"
    tel = "TEL;TYPE=cell:15242673389\n"
    phone_work = "TEL;WORK;VOICE:(111) 555-1212\n"
    email = "EMAIL:shenlian@baidu.com\n"
    address = "ADR;TYPE=WORK:;;100 Waters Edge;Baytown;LA;30314;United States of America\n"
    url = "URL:wwww.baidu.com\n"
    end = "END:VCARD\n"

    vstr = begin + name + phone + tel + phone_work + email + address + url + end
    print vstr

    gen_ecard(vstr)
