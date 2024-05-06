import pytest
import translate_API

class TestMultiPara:
    def test_1(self):
        result = translate_API.baidu_api('Hello World! This is 1st paragraph.\nThis is second paragraph.', 'auto', 'zh')
        ans1 = result['trans_result'][0]['dst']
        assert ans1 == "你好，世界！这是第一段。"
        ans2 = result['trans_result'][1]['dst']
        assert ans2 == "这是第二段。"

class TestNormal:
    def test_1(self):
        result = translate_API.baidu_api('NBA', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "美国篮球职业联盟"

    def test_2(self):
        result = translate_API.baidu_api('Hello World!', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "你好，世界！"

    def test_3(self):
        result = translate_API.baidu_api('To be or not to be, this is the question', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "生存与否，这就是问题所在"

    def test_4(self):
        result = translate_API.baidu_api("Je m'appelle Claude", 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "我叫克劳德"

class TestSpecialCha:
    def test_1(self):
        result = translate_API.baidu_api('/a/b', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "/a/b"

    def test_2(self):
        result = translate_API.baidu_api('@', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "@"



class TestAmbiguousSrc:
    def test_1(self):
        result = translate_API.baidu_api('chat', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "猫"

    def test_2(self):
        result = translate_API.baidu_api('chat', 'fra', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "猫"

    def test_3(self):
        result = translate_API.baidu_api('ton', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "吨"

    def test_4(self):
        result = translate_API.baidu_api('ton', 'en', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "吨"

    def test_5(self):
        result = translate_API.baidu_api('loin', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "腰肉"

    def test_6(self):
        result = translate_API.baidu_api('loin', 'en', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "腰肉"

    def test_7(self):
        result = translate_API.baidu_api('loin', 'fra', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "遥远"


class TestTwoLanguage:
    def test_1(self):
        result = translate_API.baidu_api('七人の侍 We Bought a Zoo ', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "七个武士我家买了动物园"

    def test_2(self):
        result = translate_API.baidu_api('北京東京New York', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "北京东京纽约"

    def test_3(self):
        result = translate_API.baidu_api('小米Tesla삼성', 'auto', 'zh')
        ans = result['trans_result'][0]['dst']
        assert ans == "小米特斯拉三星"


if __name__ == '__main__':
    pytest.main(['-vs', 'test_API.py'])
