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
    ordinal_medium_dict = {
        "십": 10,
        "백": 100,
        "천": 1000,
    }
    ordinal_large_dict = {
        "만": 10000,
        "억": 100000000,
        "조": 1000000000000,
        "경": 10000000000000000,
        "해": 100000000000000000000,
    }
    cardinal_front_dict = {
        "열": 10,
        "스물": 20,
        "스무": 20,
        "서른": 30,
        "마흔": 40,
        "쉰": 50,
        "예순": 60,
        "일흔": 70,
        "여든": 80,
        "아흔": 90,
    }
    cardinal_back_dict = {
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
    }
    cardinal_dict = {
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
        "일": 1,
        "이": 2,
        "삼": 3,
        "사": 4,
        "오": 5,
        "육": 6,
        "칠": 7,
        "팔": 8,
        "구": 9,
        "십": 10,
        "백": 100,
        "천": 1000,
        "만": 10000,
        "억": 100000000,
        "조": 1000000000000,
        "경": 10000000000000000,
        "해": 100000000000000000000,
    }
    ordinal_dict = {}
    for d in [ordinal_small_dict, ordinal_medium_dict, ordinal_large_dict]:
        ordinal_dict.update(d)

    def __init__(self):
        pass

    def _is_one_char(self, kor_num: str) -> bool:
        if all((char in self.one_char_dict) for char in kor_num):
            return True
        return False

    def _is_ordinal(self, kor_num: str) -> bool:
        if all((char in self.ordinal_dict) for char in kor_num):
            return True
        return False

    # TODO: 서수는 두자리까지 고려해야함
    def _is_cardinal(self, kor_num: str) -> bool:
        if all((char in self.cardinal_dict) for char in kor_num):
            return True
        return False

    def _read_one_char(self, kor_num: str) -> str:
        result = ""
        for char in kor_num:
            result += str(self.one_char_dict[char])
        return result

    def _read_ordinal(self, kor_num: str) -> int:
        def _read_chuns(kor_num: str) -> int:
            for i, char in enumerate(kor_num):
                if char in self.ordinal_medium_dict.keys():
                    if kor_num[i - 1] in self.ordinal_small_dict.keys():
                        return _read_chuns(kor_num[i + 1:]) + \
                               self.ordinal_medium_dict[char] * self.ordinal_small_dict[kor_num[i - 1]]
                    else:
                        return _read_chuns(kor_num[i + 1:]) + self.ordinal_medium_dict[char]
                elif len(kor_num) == 1:
                    return self.ordinal_small_dict[char]

        for i, char in enumerate(kor_num):
            if char in self.ordinal_large_dict.keys():
                if i > 0:
                    return _read_chuns(kor_num[:i]) * self.ordinal_large_dict[char] + _read_chuns(kor_num[i + 1:])
                else:
                    return self.ordinal_large_dict[char] + _read_chuns(kor_num[i + 1:])
            elif all([num not in self.ordinal_large_dict.keys() for num in kor_num]):
                return _read_chuns(kor_num)

    def _read_cardinal(self, kor_num: str) -> int:
        cardinal_patterns = {}
        for p1 in self.cardinal_front_dict.keys():
            for p2 in self.cardinal_back_dict.keys():
                cardinal_patterns[str(p1) + str(p2)] = self.cardinal_front_dict[p1] + self.cardinal_back_dict[p2]
        for p1 in self.cardinal_front_dict.keys():
            cardinal_patterns[p1] = self.cardinal_front_dict[p1]
        for p2 in self.cardinal_back_dict.keys():
            cardinal_patterns[p2] = self.cardinal_back_dict[p2]
        for i in range(len(kor_num)):
            if kor_num[i:] in cardinal_patterns.keys():
                return self._read_ordinal(kor_num[:i]) + cardinal_patterns[kor_num[i:]]

    def count_kor_num(self, kor_num: str, return_type="int"):
        kor_num = re.sub(" ", "", kor_num)

        if self._is_one_char(kor_num):
            output = self._read_one_char(kor_num)
        elif self._is_ordinal(kor_num):
            output = self._read_ordinal(kor_num)
        elif self._is_cardinal(kor_num):
            output = self._read_cardinal(kor_num)
        else:
            raise ValueError("Not a valid Korean number")

        if return_type == "int":
            return output
        elif return_type == "str":
            return str(output)
        else:
            raise ValueError("Return type not supported. Please enter \"int\" or \"str\"")


if __name__=="__main__":
    kornumcounter = KorNumCounter()
    print(kornumcounter.count_kor_num("스물둘"))