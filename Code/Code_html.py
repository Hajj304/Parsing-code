!pip install beautifulsoup4

from bs4 import BeautifulSoup

# كود HTML كنص
html_code = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Hello Mawardi</h1>
    <p class="info">This is a paragraph.</p>
  </body>
</html>
"""

# تحليل HTML
soup = BeautifulSoup(html_code, "html.parser")

# استخراج النصوص والعناصر
print("🔹 Title:", soup.title.string)
print("🔹 Heading:", soup.h1.string)
print("🔹 Paragraph:", soup.p.string)
# النتيجة
🔹 Title: Test Page
🔹 Heading: Hello Mawardi
🔹 Paragraph: This is a paragraph.
