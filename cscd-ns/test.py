from aip import AipNlp
import random

# 设置百度 API 密钥
APP_ID = '6222018'
API_KEY = 'MbTbQ0gBQuHQfoGjniuQ70X1'
SECRET_KEY = '1hFDB7bi2dlYNEJw8Mx6UIlri7s4yOQi'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def fetch_baidu_input_method_result(context, pinyin, target):
    """
    :param context: before context
    :param pinyin: pinyin of input word/char
    :param target: target word/char
    :return:
    """
    # 百度拼音转换接口
    result = client.(pinyin)

    if 'error_code' in result:
        return None  # 请求失败时返回 None

    # 获取候选词
    candidates = result.get('pinyins', [])

    if not candidates:
        return None

    # 找到长度相同的候选词
    candidates_filtered = [candidate for candidate in candidates if
                           len(candidate) == len(target) and candidate != target]

    if candidates_filtered:
        return random.choice(candidates_filtered)
    return None


# 测试
context = "一不小心"
pinyin = "yixiaoxin"
target = "选到了"
result = fetch_baidu_input_method_result(context, pinyin, target)
print(result)
