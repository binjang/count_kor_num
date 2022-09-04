import re


class KorNumCounter:
    one_char_dict = {
        "영": 0,
        "공": 0,
        "일": 1,
        "이": 2,
        "삼": 3,
        "사": 4,
        "오": 5,
        "육": 6,
        "칠": 7,
        "팔": 8,
        "구": 9,
    }
    ordinal_small_dict = {
        "영": 0,
        "일": 1,
        "이": 2,
        "삼": 3,
        "사": 4,
        "오": 5,
        "육": 6,
        "칠": 7,
        "팔": 8,
        "구": 9,
    }
    ordinal_large_dict = {
        "십": 10,
        "백": 100,
        "천": 1000,
        "만": 10000,
        "억": 100000000,
        "조": 1000000000000,
        "경": 10000000000000000,
        "해": 100000000000000000000,
    }
    cardinal_dict = {
        "스물": 20,
        "스무": 20,
        "서른": 30,
        "마흔": 40,
        "쉰": 50,
        "예순": 60,
        "일흔": 70,
        "여든": 80,
        "아흔": 90,
        "하나": 1,
        "한": 1,
        "두": 2,
        "둘": 2,
        "세": 3,
        "셋": 3,
        "네": 4,
        "넷": 4,
        "다섯": 5,
        "여섯": 6,
        "일곱": 7,
        "여덟": 8,
        "여덜": 8,
        "아홉": 9,
        "열": 10,
        "십": 10,
        "백": 100,
        "천": 1000,
        "만": 10000,
        "억": 100000000,
        "조": 1000000000000,
        "경": 10000000000000000,
        "해": 100000000000000000000,
    }

    def __init__(self):
        self.__init__()

    def _is_one_char(kor_num: str) -> bool:
        if all((char in one_char_dict) for char in kor_num):
            return True
        return False

    def _is_ordinal(kor_num: str) -> bool:
        if all((char in ordinal_large_dict.update(ordinal_small_dict)) for char in kor_num):
            return True
        return False

    def _is_cardinal(kor_num: str) -> bool:
        pass

    def _read_one_char(kor_num: str) -> int:
        pass

    def _read_ordinal(kor_num: str) -> int:
        pass

    def _read_cardinal(kor_num: str) -> int:
        pass

    def count_kor_num(kor_num: int, return_type="int"):
        if _is_one_char(kor_num):
            output = _read_one_char(kor_num)
        elif _is_ordinal(kor_num):
            output = _read_ordinal(kor_num)
        elif _is_cardinal(kor_num):
            output = _read_cardinal(kor_num)
        else:
            raise ValueError("Not a valid Korean number")

        if return_type is "int":
            return output
        elif return_type is "str":
            return str(output)
        else:
            raise ValueError("Return type not supported. Please enter \"int\" or \"str\"")
