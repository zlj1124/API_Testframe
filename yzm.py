
import ddddocr
import random
import string
from sympy import sympify
import base64
import cv2
import numpy as np
from Params.parseYaml import ReadYaml
import time
import requests
tl = ReadYaml()

 #用于计算型验证码识别，感觉也不太准
def generate_random_string(length: int) -> str:
    """生成指定长度的随机字符串"""
    
    characters = string.ascii_letters + string.digits
    # 随机选择字符并拼接成指定长度的字符串
    return ''.join(random.choice(characters) for _ in range(length))

def generate_rando_mx() -> str:
    """生成与前端相同的 randoMx 参数：毫秒级时间戳 + 10位随机字符串"""
    # 1. 获取当前毫秒级时间戳（与前端 Date.now() 一致）
    timestamp = int(time.time() * 1000)
    # 2. 生成10位随机字符串
    random_str = generate_random_string(10)
    # 3. 拼接时间戳（转字符串）和随机字符串
    return f"{timestamp}{random_str}"


def generate_captcha():
    # 生成参数
    rando_mx = generate_rando_mx()
    host = tl.get_datas["host"]
    path = tl.get_datas["captcha_path"]
    # 调用验证码接口
    response = requests.get(
        url = host + path,
        params={"randoMx": rando_mx}
        )
    # 处理验证码图片（如保存）
    print(response.text)
    base64_data=response.json()['data']
    image_data = base64.b64decode(base64_data.split(",")[1])
    nparr = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("captcha.png", image)   
    return rando_mx

def verify_code():
    # 初始化OCR
    ocr = ddddocr.DdddOcr()
    generate_captcha()
    # 读取验证码图片（二进制）
    with open("captcha.png", "rb") as f:
        img_bytes = f.read()
    # 识别计算题文本（如"3+5"）
    captcha_text = ocr.classification(img_bytes).strip()
    # 处理可能的干扰字符（如去除"="“?”等）
    captcha_text = captcha_text.replace("=", "").replace("?", "").replace("x", "*").replace("÷", "/").replace("+", "+")
    print(captcha_text)
    # 计算结果
    try:
        result = sympify(captcha_text)  # 解析表达式并计算
        print(f"识别的表达式: {captcha_text}，答案: {int(result)}")  # 结果转整数（验证码答案通常为整数）
    except Exception as e:
        print(f"识别或计算失败: {e}")
    return result
