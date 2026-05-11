class Solution:
    # use a header to count the chars 
    def encode(self, strs: List[str]) -> str:
        word_count_array = []
        body = ""
        for string in strs:
            word_count_array.append(len(string))
            body = body + string
        header = str(len(word_count_array)) + '#'
        for count in word_count_array:
            header = header + "/" + str(count)
        return header + "/" + body 

    def decode(self, s: str) -> List[str]:
        header_count = s.split("#", 1)[0]
        header_and_body = s.split("#", 1)[1]
        split_by_slash = header_and_body.split("/", int(header_count) + 1)
        header = split_by_slash[1:int(header_count) + 1]
        body = split_by_slash[int(header_count) + 1:]
        output = []
        body_string = body[0]
        for char_count_str in header: 
            char_count = int(char_count_str)
            output.append(body_string[0:char_count])
            body_string = body_string[char_count:]
        return output