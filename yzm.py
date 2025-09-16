
import base64
from PIL import Image, ImageOps
import pytesseract
import re  # 用于提取运算式中的数字和运算符

# --------------------------
# 1. Base64解码为验证码图片
# --------------------------
def decode_captcha(base64_str, save_path="captcha.png"):
    # 移除Base64前缀，保留编码内容
    base64_data = base64_str.split(",")[1]
    # 解码并写入文件
    with open(save_path, "wb") as f:
        f.write(base64.b64decode(base64_data.encode("ascii")))
    return save_path  # 返回图片路径

# --------------------------
# 2. 图片预处理（关键：提升OCR识别率）
# --------------------------
def preprocess_image(image_path):
    # 打开图片并转为灰度图（减少颜色干扰）
    img = Image.open(image_path).convert("L")  # "L"表示灰度模式
    # 二值化：将灰度图转为黑白图（阈值设为127，可根据验证码调整）
    # 原理：像素值>127设为255（白色，背景），≤127设为0（黑色，字符）
    threshold = 127
    img = img.point(lambda p: 255 if p > threshold else 0)
    # （可选）反转颜色（若字符是白色、背景是黑色，需反转）
    img = ImageOps.invert(img)
    # 保存预处理后的图片（可选，用于调试）
    img.save("preprocessed_captcha.png")
    return img

# --------------------------
# 3. OCR识别运算式（数字+运算符）
# --------------------------
def ocr_captcha(image):
  
    pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"
    
    # 配置OCR：仅识别数字和运算符（+、-、×、÷），减少干扰
    custom_config = r'--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789+-×÷'
    # 执行OCR识别
    expression = pytesseract.image_to_string(image, config=custom_config).strip()
    
    # 清理识别结果（去除多余字符，只保留“数字+运算符+数字”格式）
    # 用正则表达式提取核心运算式（如从“5 + 3”提取“5+3”）
    pattern = r'(\d+)\s*([+\-×÷])\s*(\d+)'
    match = re.search(pattern, expression)
    if not match:
        raise ValueError(f"OCR识别失败，未提取到有效运算式（识别结果：{expression}）")
    
    num1 = int(match.group(1))  # 第一个数字
    op = match.group(2)         # 运算符
    num2 = int(match.group(3))  # 第二个数字
    return num1, op, num2

# --------------------------
# 4. 解析运算并返回结果
# --------------------------
def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "×":
        return num1 * num2
    elif op == "÷":
        # 验证码除法通常为整数结果，避免浮点数
        if num2 == 0:
            raise ZeroDivisionError("运算式中除数不能为0")
        return num1 // num2 if num1 % num2 == 0 else num1 / num2
    else:
        raise ValueError(f"不支持的运算符：{op}")

# --------------------------
# 主函数：串联所有步骤
# --------------------------
def solve_captcha(base64_str):
    try:
        # 1. 解码图片
        img_path = decode_captcha(base64_str)
        print(f"验证码图片已保存：{img_path}")
        
        # 2. 预处理图片
        preprocessed_img = preprocess_image(img_path)
        print("图片预处理完成")
        
        # 3. OCR识别运算式
        num1, op, num2 = ocr_captcha(preprocessed_img)
        print(f"识别到运算式：{num1} {op} {num2}")
        
        # 4. 计算结果
        result = calculate(num1, op, num2)
        print(f"运算结果：{result}")
        return result
    except Exception as e:
        print(f"处理失败：{str(e)}")
        return None
    

if __name__ == '__main__':
    captcha_base64='data:image/png;base64,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'
    solve_captcha(captcha_base64)
        