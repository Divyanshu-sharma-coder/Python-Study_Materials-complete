





# ______________________DEMON SLAYER STYLE _______________________________________








from abc import ABC, abstractmethod
import math
from typing import Dict, Type, List, Any
from flask import Flask, render_template, request, jsonify

# --- 1. OOP Core: Abstract Base Class (Upgraded for flexibility) ---
class Operation(ABC):
    @abstractmethod
    def execute(self, *args: float) -> float:
        """Execute operation supporting variable number of mathematical arguments."""
        pass

# --- 2. OOP Core: Concrete Operations (Binary & Unary) ---
class Addition(Operation):
    def execute(self, *args: float) -> float: return args[0] + args[1]

class Subtraction(Operation):
    def execute(self, *args: float) -> float: return args[0] - args[1]

class Multiplication(Operation):
    def execute(self, *args: float) -> float: return args[0] * args[1]

class Division(Operation):
    def execute(self, *args: float) -> float:
        if args[1] == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return args[0] / args[1]

class Power(Operation):
    def execute(self, *args: float) -> float: return math.pow(args[0], args[1])

class Modulo(Operation):
    def execute(self, *args: float) -> float: return args[0] % args[1]

class SquareRoot(Operation):
    def execute(self, *args: float) -> float:
        if args[0] < 0:
            raise ValueError("Square root of a negative number is undefined")
        return math.sqrt(args[0])

class Logarithm(Operation):
    def execute(self, *args: float) -> float:
        if args[0] <= 0:
            raise ValueError("Logarithm of zero or a negative number is undefined")
        return math.log10(args[0])

# --- 3. OOP Core: Stateful History Logger ---
class HistoryManager:
    """Manages computation tracking and session state separation of concerns."""
    def __init__(self) -> None:
        self._logs: List[Dict[str, Any]] = []

    def log_success(self, operator: str, num1: float, num2: float | None, result: Any) -> None:
        expr = f"{num1} {operator} {num2}" if num2 is not None else f"{operator}({num1})"
        self._logs.append({"expression": expr, "result": result, "status": "success"})

    def log_failure(self, operator: str, num1: float, num2: float | None, error_msg: str) -> None:
        expr = f"{num1} {operator} {num2}" if num2 is not None else f"{operator}({num1})"
        self._logs.append({"expression": expr, "result": error_msg, "status": "failed"})

    def get_all(self) -> List[Dict[str, Any]]:
        return self._logs

    def clear(self) -> None:
        self._logs.clear()

# --- 4. OOP Core: Operation Factory ---
class OperationFactory:
    def __init__(self) -> None:
        self._operations: Dict[str, Type[Operation]] = {
            "+": Addition,
            "-": Subtraction,
            "*": Multiplication,
            "/": Division,
            "^": Power,
            "%": Modulo,
            "sqrt": SquareRoot,
            "log": Logarithm
        }

    def execute_symbol(self, symbol: str, *args: float) -> float:
        op_class = self._operations.get(symbol)
        if not op_class:
            raise ValueError(f"Operator '{symbol}' not supported.")
        return op_class().execute(*args)

    def is_unary(self, symbol: str) -> bool:
        """Helper to determine if operation requires only a single number input."""
        return symbol in ["sqrt", "log"]

# --- 5. Flask Web Application Core ---
app = Flask(__name__)
factory = OperationFactory()
history = HistoryManager()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json() or {}
    operator = data.get('operator', '+')
    
    try:
        num1 = float(data.get('num1', 0))
        # Handle second argument gracefully if it's an operation requiring only 1 number
        num2_raw = data.get('num2')
        num2 = float(num2_raw) if num2_raw is not None else None
        
        # Determine execution context and pass parameters safely
        if factory.is_unary(operator):
            result = factory.execute_symbol(operator, num1)
        else:
            if num2 is None:
                raise ValueError("Missing second parameter for execution context")
            result = factory.execute_symbol(operator, num1, num2)
        
        # Strip trailing decimals for clean presentation
        if result.is_integer():
            result = int(result)
            
        # Log to in-memory app history
        history.log_success(operator, num1, num2, result)
        return jsonify({"success": True, "result": str(result)})
        
    except ZeroDivisionError as e:
        history.log_failure(operator, num1, num2 if 'num2' in locals() else None, str(e))
        return jsonify({"success": False, "error": str(e)})
    except ValueError as e:
        history.log_failure(operator, num1, num2 if 'num2' in locals() else None, str(e))
        return jsonify({"success": False, "error": str(e)})
    except Exception:
        return jsonify({"success": False, "error": "Invalid Input"})

@app.route('/history', methods=['GET', 'DELETE'])
def manage_history():
    if request.method == 'DELETE':
        history.clear()
        return jsonify({"success": True, "message": "History wiped successfully"})
    return jsonify(history.get_all())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
