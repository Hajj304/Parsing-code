!pip install py_mini_racer esprima

import esprima

# كود JavaScript كنص
js_code = """
function greet(name) {
    var message = "Hello, " + name + "!";
    console.log(message);
}

let age = 25;
greet("Mawardi");
"""

# تحليل الكود
parsed = esprima.parseScript(js_code)

# عرض أسماء الدوال والمتغيرات
for node in parsed.body:
    if node.type == "FunctionDeclaration":
        print(f"🔹 Found function: {node.id.name}")
    elif node.type in ["VariableDeclaration"]:
        for decl in node.declarations:
            print(f"🔸 Found variable: {decl.id.name}")
# النتيجة
🔹 Found function: greet
🔸 Found variable: age
