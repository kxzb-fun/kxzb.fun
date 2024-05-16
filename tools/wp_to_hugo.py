import xml.etree.ElementTree as ET
import os
from datetime import datetime
import html2text
import re

# 定义 WordPress 导出文件路径
wordpress_export_file = 'WordPress.xml'

# 定义输出目录
output_directory = 'converted_posts'

# 创建输出目录
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 解析 WordPress 导出文件
tree = ET.parse(wordpress_export_file)
root = tree.getroot()

# 遍历每个 <item> 元素
for item in root.findall('.//item'):
    # 获取文章标题
    title = item.find('title').text

    # 获取文章内容并转换为 Markdown
    content = item.find('content:encoded', {'content': 'http://purl.org/rss/1.0/modules/content/'}).text

    # 将 <xmp> 标签替换为 Markdown 代码块
    content = re.sub(r'<xmp>(.*?)</xmp>', r'```bash\n\1\n```', content, flags=re.DOTALL)

    # 使用 html2text 库将 HTML 转换为 Markdown 格式
    converter = html2text.HTML2Text()
    content = converter.handle(content)

    # 获取文章发布日期
    pub_date = item.find('pubDate').text
    pub_date = datetime.strptime(pub_date, '%a, %d %b %Y %H:%M:%S %z')
    pub_date_str = pub_date.strftime('%Y-%m-%dT%H:%M:%S%z')

    # 获取文章标签
    tags = [tag.text for tag in item.findall('category') if tag.attrib.get('domain') == 'post_tag']

    # 创建 Markdown 文件并写入内容
    file_name = pub_date.strftime('%Y-%m-%d-') + title.replace(' ', '-').lower() + '.md'
    file_path = os.path.join(output_directory, file_name)
    with open(file_path, 'w') as f:
        f.write(f"---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"date: \"{pub_date_str}\"\n")
        f.write(f"tags: {tags}\n")
        f.write(f"---\n\n")
        f.write(content)

    print(f"Converted {title} to Markdown format: {file_path}")
