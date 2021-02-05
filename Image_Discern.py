import cv2
import math

###图像匹配###
def Image_Discern(imgone,imgtwo):
    # 1.模板匹配
    # 大图
    img = cv2.imread(imgone)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 小图
    template = cv2.imread(imgtwo, 0)
    h, w = template.shape[:2]  # rows->h, cols->w
    img2 = img.copy()

    # 对比图像
    res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF_NORMED)

    # 返回坐标
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 计算中心坐标
    a1, a2 = top_left
    b1, b2 = bottom_right
    c1 = (a1 + w/2)*0.8  # 0.8匹配屏幕分辨率（因为分辨率原因这里乘0.8用于适应平复分辨率坐标位置）
    c2 = (a2 + h/2)*0.8
    e1 = math.ceil(c1)
    e2 = math.ceil(c2)
    d1 = (e1, e2)
    # print(‘中心坐标为：‘ , d1)

    ###测试图像匹配，弹出图像显示匹配位置###
    # 在匹配点画小圆心
    # cv2.circle(res, top_left, 10, 0, 2)
    # cv2.imshow("res", res)

    # # 画矩形
    # cv2.rectangle(img2, top_left, bottom_right, (0, 255, 0), 2)
    # cv2.imshow("img2",img2)
    # cv2.waitKey(0)

    # 两张图片是否匹配
    # print(‘各个参数为：‘,min_val, max_val, min_loc, max_loc)

    ###进行图像筛选###
    if min_val <= 0.03:
        # print(‘图片匹配‘)
        return(d1)
    else:
        # print(‘图片不匹配‘)
        return(0)


# 测试
# Image_Discern(‘e1.png‘,‘a2.png‘) # （大图，小图）匹配图像