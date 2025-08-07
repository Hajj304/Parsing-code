# مثال بسيط عن Parsing code في Python
import ast

# كود بايثون كنص
code = """
def hello(name):
    message = f"Hello, {name}!"
    print(message)

x = 42
hello("Mawardi")
"""

# تحويل الكود إلى شجرة AST
tree = ast.parse(code)

# دالة لعرض أسماء الدوال والمتغيرات
class CodeAnalyzer(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(f"🔹 Found function: {node.name}")
        self.generic_visit(node)

    def visit_Assign(self, node):
        targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
        for var in targets:
            print(f"🔸 Found variable: {var}")
        self.generic_visit(node)

# تحليل الكود
analyzer = CodeAnalyzer()
analyzer.visit(tree)

