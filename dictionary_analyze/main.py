def load_input_method_dictionary(file_path):
    """
    加载输入法字典文本文件
    字典格式为「汉字+空格+按键编码」，例：「的 u」或「枲 kdem」
    """
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 拆分每行文本，获得汉字和按键编码
            char, encoding = line.strip().split()
            dictionary[char] = encoding
    return dictionary

def classify_keys(left_hand_keys, right_hand_keys):
    """
    根据左右手键盘按键集合，分类键位
    """
    key_classification = {}
    # 标记左手按键为 'L'
    for key in left_hand_keys:
        key_classification[key] = 'L'
    # 标记右手按键为 'R'
    for key in right_hand_keys:
        key_classification[key] = 'R'
    return key_classification

def analyze_dictionary(dictionary, key_classification, words_count_max=1000):
    """
    统计左右手交替互击的文字数量和左右手按键比例
    """
    left_hand_count = 0
    right_hand_count = 0
    alternating_count = 0

    words_count = 0
    
    for char, encoding in dictionary.items():
        if not encoding:  # 跳过空编码
            continue
        if(words_count >= words_count_max):
            break
        words_count += 1
        
        last_hand = key_classification.get(encoding[0], '')
        alternating = False
        
        for key in encoding:
            current_hand = key_classification.get(key, '')
            if current_hand == '':
                continue
            
            if current_hand == 'L':
                left_hand_count += 1
            elif current_hand == 'R':
                right_hand_count += 1
            
            if current_hand != last_hand:
                alternating = True
            last_hand = current_hand

        if alternating:
            alternating_count += 1

    total_keys = left_hand_count + right_hand_count
    if total_keys == 0:
        left_hand_ratio = 0
        right_hand_ratio = 0
    else:
        left_hand_ratio = left_hand_count / total_keys
        right_hand_ratio = right_hand_count / total_keys

    return alternating_count, left_hand_ratio, right_hand_ratio, total_keys ,words_count

# 示例输入法字典文件路径
input_method_dict_path = 'input_method_dictionary.txt'
# 左手和右手按键集合
left_hand_keys = { 'w', 'e','q', 'z','r', 't', 'a', 's', 'd', 'f', 'g',  'x', 'c', 'v', 'b'}
right_hand_keys = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}
left_hand_keys = { 'r', 't', 'a', 's', 'd', 'f', 'g',  'x', 'c', 'v', 'b'}
right_hand_keys = {'w', 'e','q', 'z','y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}
# left_hand_keys = { 'w', 'e','r', 't', 'a', 's', 'd', 'f', 'g',  'x', 'c', 'v', 'b'}
# right_hand_keys = {'q', 'z','y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}

# 加载输入法字典
dictionary = load_input_method_dictionary(input_method_dict_path)
# 分类键位
key_classification = classify_keys(left_hand_keys, right_hand_keys)
# 分析字典
alternating_count, left_hand_ratio, right_hand_ratio, hand_count, words_count = analyze_dictionary(dictionary, key_classification, 6000)

# 输出结果
print(f"总字数: {words_count}")
print(f"总按键数: {hand_count}")
print(f"左右手交替互击的文字数量: {alternating_count}")
print(f"左手按键比例: {left_hand_ratio:.2%}")
print(f"右手按键比例: {right_hand_ratio:.2%}")
