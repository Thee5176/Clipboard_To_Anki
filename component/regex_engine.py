import re

class RegexEngine:
    def clean(input_str):
        '''remove whitespace and special characters'''
        cleaned_str = re.sub(r'[\'\'\[\-\+\.\^\:\,\]\s\?\!\#\*\&\(\)]', '', input_str)
        
        '''check if all character is kanji'''
        kanji_pattern = re.compile(r'[\u3041-\u3096\u30A0-\u30FF\u4E00-\u9FAF]')
        if len(kanji_pattern.findall(cleaned_str)) == len(cleaned_str):
            return cleaned_str
        else:
            raise ValueError(f'text concist non-kanji character: {cleaned_str}')