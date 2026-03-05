from flask import Flask, render_template, request, jsonify
from datetime import datetime
import math
import json

app = Flask(__name__)

class AdvancedCalculator:
    def __init__(self):
        self.history = []
    
    # العمليات الأساسية
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "خطأ: لا يمكن القسمة على صفر"
        return a / b
    
    @staticmethod
    def modulo(a, b):
        if b == 0:
            return "خطأ: لا يمكن إيجاد الباقي على صفر"
        return a % b
    
    @staticmethod
    def power(a, b):
        return a ** b
    
    # الوظائف العلمية
    @staticmethod
    def square_root(a):
        if a < 0:
            return "خطأ: لا يمكن إيجاد جذر عدد سالب"
        return math.sqrt(a)
    
    @staticmethod
    def sin(a):
        return math.sin(math.radians(a))
    
    @staticmethod
    def cos(a):
        return math.cos(math.radians(a))
    
    @staticmethod
    def tan(a):
        return math.tan(math.radians(a))
    
    @staticmethod
    def log(a, base=10):
        if a <= 0:
            return "خطأ: اللوغاريتم يجب أن يكون موجباً"
        return math.log(a, base)
    
    @staticmethod
    def ln(a):
        if a <= 0:
            return "خطأ: اللوغاريتم الطبيعي يجب أن يكون موجباً"
        return math.log(a)
    
    @staticmethod
    def factorial(a):
        if a < 0 or a != int(a):
            return "خطأ: يجب أن يكون العدد موجباً وصحيحاً"
        return math.factorial(int(a))
    
    @staticmethod
    def absolute(a):
        return abs(a)
    
    @staticmethod
    def percentage(a, b):
        return (a / 100) * b
    
    # تحويل الوحدات
    @staticmethod
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            return (value - 32) * 5/9
        elif from_unit == 'celsius' and to_unit == 'kelvin':
            return value + 273.15
        elif from_unit == 'kelvin' and to_unit == 'celsius':
            return value - 273.15
        return value
    
    @staticmethod
    def convert_length(value, from_unit, to_unit):
        # التحويل إلى متر أولاً
        to_meter = {
            'mm': 0.001,
            'cm': 0.01,
            'm': 1,
            'km': 1000,
            'inch': 0.0254,
            'foot': 0.3048,
            'mile': 1609.34
        }
        
        if from_unit not in to_meter or to_unit not in to_meter:
            return "خطأ: وحدة غير معروفة"
        
        meter_value = value * to_meter[from_unit]
        return meter_value / to_meter[to_unit]
    
    @staticmethod
    def convert_weight(value, from_unit, to_unit):
        # التحويل إلى كيلوجرام أولاً
        to_kg = {
            'mg': 0.000001,
            'g': 0.001,
            'kg': 1,
            'ton': 1000,
            'oz': 0.0283495,
            'lb': 0.453592
        }
        
        if from_unit not in to_kg or to_unit not in to_kg:
            return "خطأ: وحدة غير معروفة"
        
        kg_value = value * to_kg[from_unit]
        return kg_value / to_kg[to_unit]
    
    def add_to_history(self, operation, result):
        self.history.append({
            'operation': operation,
            'result': result,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history = []

calc = AdvancedCalculator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        operation = data.get('operation')
        num1 = data.get('num1')
        num2 = data.get('num2')
        
        result = None
        operation_text = ""
        
        # تحويل إلى أرقام حيث يكون ممكناً
        try:
            if num1 is not None:
                num1 = float(num1)
            if num2 is not None:
                num2 = float(num2)
        except:
            return jsonify({'error': 'قيم غير صحيحة'}), 400
        
        # العمليات الأساسية
        if operation == 'add':
            result = calc.add(num1, num2)
            operation_text = f"{num1} + {num2} = {result}"
        elif operation == 'subtract':
            result = calc.subtract(num1, num2)
            operation_text = f"{num1} - {num2} = {result}"
        elif operation == 'multiply':
            result = calc.multiply(num1, num2)
            operation_text = f"{num1} × {num2} = {result}"
        elif operation == 'divide':
            result = calc.divide(num1, num2)
            operation_text = f"{num1} ÷ {num2} = {result}"
        elif operation == 'modulo':
            result = calc.modulo(num1, num2)
            operation_text = f"{num1} mod {num2} = {result}"
        elif operation == 'power':
            result = calc.power(num1, num2)
            operation_text = f"{num1}^{num2} = {result}"
        
        # الوظائف العلمية
        elif operation == 'sqrt':
            result = calc.square_root(num1)
            operation_text = f"√{num1} = {result}"
        elif operation == 'sin':
            result = calc.sin(num1)
            operation_text = f"sin({num1}°) = {result}"
        elif operation == 'cos':
            result = calc.cos(num1)
            operation_text = f"cos({num1}°) = {result}"
        elif operation == 'tan':
            result = calc.tan(num1)
            operation_text = f"tan({num1}°) = {result}"
        elif operation == 'log':
            result = calc.log(num1)
            operation_text = f"log({num1}) = {result}"
        elif operation == 'ln':
            result = calc.ln(num1)
            operation_text = f"ln({num1}) = {result}"
        elif operation == 'factorial':
            result = calc.factorial(num1)
            operation_text = f"{num1}! = {result}"
        elif operation == 'abs':
            result = calc.absolute(num1)
            operation_text = f"|{num1}| = {result}"
        elif operation == 'percentage':
            result = calc.percentage(num1, num2)
            operation_text = f"{num1}% من {num2} = {result}"
        
        # تحويل الوحدات
        elif operation == 'convert_temp':
            from_unit = data.get('from_unit')
            to_unit = data.get('to_unit')
            result = calc.convert_temperature(num1, from_unit, to_unit)
            operation_text = f"{num1} {from_unit} = {result} {to_unit}"
        elif operation == 'convert_length':
            from_unit = data.get('from_unit')
            to_unit = data.get('to_unit')
            result = calc.convert_length(num1, from_unit, to_unit)
            operation_text = f"{num1} {from_unit} = {result} {to_unit}"
        elif operation == 'convert_weight':
            from_unit = data.get('from_unit')
            to_unit = data.get('to_unit')
            result = calc.convert_weight(num1, from_unit, to_unit)
            operation_text = f"{num1} {from_unit} = {result} {to_unit}"
        else:
            return jsonify({'error': 'عملية غير معروفة'}), 400
        
        if isinstance(result, str):  # خطأ
            return jsonify({'error': result}), 400
        
        calc.add_to_history(operation_text, result)
        return jsonify({'result': round(result, 10)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(calc.get_history())

@app.route('/clear-history', methods=['POST'])
def clear_history():
    calc.clear_history()
    return jsonify({'status': 'تم مسح السجل'})

if __name__ == '__main__':
    app.run(debug=True)