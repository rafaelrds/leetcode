from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        sizes = [len(s) for s in strs]
        res = []
        for size, s in zip(sizes, strs):
            res.append(f"[{size}]{s}")
        str_res = "".join(res)
        return str_res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            i += 1  # skip [
            size = []
            while s[i] != "]":
                size.append(s[i])
                i += 1
            int_size = int("".join(size))
            i += 1  # skip ]
            word = []
            while int_size:
                word.append(s[i])
                int_size -= 1
                i += 1
            str_word = "".join(word)
            res.append(str_word)
        return res


if __name__ == "__main__":
    dummy_input = ["Hello", "World"]
    codec = Codec()
    print(codec.decode(codec.encode(dummy_input)))
    dummy_input2 = [""]
    print(codec.decode(codec.encode(dummy_input2)))
    dummy_input3 = ["Leetcode", "is", "Awesome"]
    print(codec.decode(codec.encode(dummy_input3)))
