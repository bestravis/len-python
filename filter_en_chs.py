import re
string = "Wu Kuiwu  吴奎武"
sub_str = re.sub(u"([\ \u0041-\u005a\u0061-\u007a])","",string)
print(sub_str)             #提取中文字符

import re
string = "Wu Kuiwu  吴奎武"
sub_str = re.sub(u"([\u4e00-\u9fa5])","",string)
print(sub_str)             #提取英文字符