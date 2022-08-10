#[]原子表
[a] 匹配字母a
[ab] 匹配字母a或者b
[abc] 匹配字母a或者b或者c
[a1] 匹配a或者1
[a-z] 匹配任意一位小写字母
[A-Z]   匹配任意一位大写字母
[0-9]   匹配任意一位数字
[a-zA-Z]    匹配任意一位字母
[a-zA-Z0-9] 匹配任意一位数字或字母

#[][]两个原子表
[a][b]  匹配字母ab
[a][bc] 匹配字母ab或者ac
#{m} 代表匹配前面表达式m个

[a-z]{5}
[0-9]{5}

#匹配手机号码
[1][3-9][0-9]{9}

12{3}

#{m,n} 匹配前面表达式m-n个
[a-z]{2,4} #匹配2-4位的小写字母

#{m,} 匹配前面表达式之手m个
[a-z]{2,} #至少匹配2位小写字母

#?可有可无
[a-z]?  匹配到一位小写字母都可以
[a-z]{0,1}
-?[0-9]  #匹配一位1-9之间的正负整数

# . 匹配处理换行符以外的任意字符 \r\n

#  *  匹配前面的表达式0次到多次 {0,}

#  .*?  匹配除换行符以外的任意字符任意次 拒绝贪婪
#   .*  匹配除换行符意外的任意字符任意次  贪婪模式

# + 匹配一次到多次 {1,}

# .+? 匹配除换行符以外的任意字符至少一次 拒绝贪婪
# .+ 匹配除换行符以外的任意字符至少一次 贪婪

# | 或者

# () 作用自存储  一个单元 会把括号中的匹配到的结果进行单独返回
(1[3-9][0-9]{9})|([1-9][0-9]{4,10})

# ^ 开头
# $结尾
