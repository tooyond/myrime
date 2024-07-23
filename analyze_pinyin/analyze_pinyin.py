import pypinyin
from collections import Counter
import re

# 提取拼音中的韵母
def extract_vowels(pinyin):
    # 定义所有可能的韵母
    vowel_patterns = ['iong','iang','uang','ing','ong','iao','eng','ian','ang','uan','uai','ao','en','an','ua','ei','ai','ui','ie','ue','ve','ia','uo','un','ve','er','vn','in','ou','iu','a','o','e','i','u','v',]
    # 查找拼音中包含的韵母模式
    for pattern in vowel_patterns:
        if pattern in pinyin:
            return pattern
    return ''  # 如果没有找到匹配的韵母模式

# 统计文本中韵母的数量和比例
def count_vowels_in_text(text):
    # 将中文文本转换为拼音列表
    pinyin_list = pypinyin.lazy_pinyin(text)
    # 提取每个拼音中的韵母
    vowels = [extract_vowels(p) for p in pinyin_list if extract_vowels(p)]
    # 统计每个韵母出现的次数
    vowel_count = Counter(vowels)
    # 计算韵母总数
    total_vowels = sum(vowel_count.values())
    # 计算每个韵母的比例
    vowel_percentage = {vowel: count / total_vowels * 100 for vowel, count in vowel_count.items()}
    return vowel_count, vowel_percentage

# 读取文本文件内容
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 主函数
def main(file_path):
    # 读取中文文本文件内容
    text = read_text_file(file_path)
    # 统计韵母的数量和比例
    vowel_count, vowel_percentage = count_vowels_in_text(text)
    # 按照数量排序韵母统计结果
    sorted_vowel_count = sorted(vowel_count.items(), key=lambda item: item[1], reverse=True)
    # 按照比例排序韵母比例结果
    sorted_vowel_percentage = sorted(vowel_percentage.items(), key=lambda item: item[1], reverse=True)
    
    # 打印韵母数量结果
    print("Vowel Count:")
    for vowel, count in sorted_vowel_count:
        print(f"{vowel}: {count}")
    
    # 打印韵母比例结果
    print("\nVowel Percentage:")
    for vowel, percentage in sorted_vowel_percentage:
        print(f"{vowel}: {percentage:.2f}%")

if __name__ == "__main__":
    file_path = input("请输入中文文本文件的地址：")
    main(file_path)
