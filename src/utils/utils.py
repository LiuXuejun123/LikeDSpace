def longest_common_substring(str1, str2):
    # 获取字符串长度
    m, n = len(str1), len(str2)

    # 初始化 DP 表格，记录公共子串长度
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 记录最长公共子串的长度和结束位置
    max_length = 0
    end_index = 0

    # 填充 DP 表格
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    # 提取最长公共子串
    longest_substring = str1[end_index - max_length:end_index]

    return longest_substring, max_length
def BestMatchString(Searchstr,StringList):
    if Searchstr.lower() in (item.lower() for item in StringList):
        #print(f"'{Searchstr}' 在列表中")
        BestmatchStr = Searchstr
    else:
        maxfitbest = 0
        for str11 in StringList:
            longest_substring, max_length = longest_common_substring(Searchstr, str11)
            if max_length>maxfitbest:
                maxfitbest = max_length
                BestmatchStr = str11

        #print(f"'{Searchstr}' 不在列表中，替换为{BestmatchStr}")
    return BestmatchStr