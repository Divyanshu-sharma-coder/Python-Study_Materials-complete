# SO this is a advanced oops program of a Calculator Try to understand it, it is Robust and Scalable--
from abc import ABC, abstractmethod
import math
from typing import Dict, Type, List
import streamlit as st

# --- 1. Abstract Base Class for Operations ---
class Operation(ABC):
    """Abstract base class for all calculator operations."""
    @abstractmethod
    def execute(self, *args: float) -> float:
        pass

# --- 2. Concrete Operation Implementations ---
class Addition(Operation):
    def execute(self, *args: float) -> float:
        return sum(args)

class Subtraction(Operation):
    def execute(self, *args: float) -> float:
        if not args: return 0
        return args[0] - sum(args[1:])

class Multiplication(Operation):
    def execute(self, *args: float) -> float:
        if not args: return 0
        result = 1
        for num in args: result *= num
        return result

class Division(Operation):
    def execute(self, *args: float) -> float:
        if len(args) < 2:
            raise ValueError("Division requires at least two numbers.")
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= num
        return result

class Power(Operation):
    def execute(self, *args: float) -> float:
        if len(args) != 2:
            raise ValueError("Power operation requires exactly two numbers (base, exponent).")
        return math.pow(args[0], args[1])

# --- 3. Factory for Operations ---
class OperationFactory:
    """Manages registered operations and instantiates them."""
    def __init__(self) -> None:
        self._operations: Dict[str, Type[Operation]] = {}
        self.register_operation("+ Addition", Addition)
        self.register_operation("- Subtraction", Subtraction)
        self.register_operation("* Multiplication", Multiplication)
        self.register_operation("/ Division", Division)
        self.register_operation("^ Power", Power)

    def register_operation(self, name: str, operation_class: Type[Operation]) -> None:
        self._operations[name] = operation_class

    def get_operation(self, name: str) -> Operation:
        operation_class = self._operations.get(name)
        if not operation_class:
            raise ValueError(f"Operation '{name}' is not supported.")
        return operation_class()
    
    def get_registered_names(self) -> List[str]:
        return list(self._operations.keys())

# --- 4. Core Calculator Engine ---
class Calculator:
    """Core engine that handles execution and returns logs."""
    def __init__(self, factory: OperationFactory) -> None:
        self._factory = factory

    def calculate(self, name: str, *args: float) -> float:
        operation = self._factory.get_operation(name)
        return operation.execute(*args)

# --- 5. Streamlit GUI Controller ---
def run_gui():
    # Page setup
    st.set_page_config(page_title="Advanced OOP Calculator", page_icon="🧮", layout="centered")
    st.title("🧮 Advanced OOP Calculator")
    st.write("Powered by clean SOLID design principles.")

    # Initialize backend components inside Streamlit session state so they persist
    if "factory" not in st.session_state:
        st.session_state.factory = OperationFactory()
    if "engine" not in st.session_state:
        st.session_state.engine = Calculator(st.session_state.factory)
    if "history" not in st.session_state:
        st.session_state.history = []

    # UI Layout: Sidebar for History
    with st.sidebar:
        st.header("⏳ Calculation History")
        if not st.session_state.history:
            st.info("No calculations yet.")
        else:
            for log in reversed(st.session_state.history):
                st.text(log)
            if st.button("Clear History"):
                st.session_state.history = []
                st.rerun()

    # UI Layout: Main interactive card
    with st.container(border=True):
        st.subheader("Compute Expression")
        
        # 1. Select Operation
        options = st.session_state.factory.get_registered_names()
        selected_op = st.selectbox("Choose an operation:", options)
        
        # 2. Dynamic Input Help
        if "^" in selected_op:
            help_text = "Enter exactly two numbers separated by spaces (e.g., 2 3 for 2³)"
        else:
            help_text = "Enter numbers separated by spaces (e.g., 10 5 2.5)"
            
        user_input = st.text_input("Enter your numbers:", placeholder="e.g. 10 20 30", help=help_text)
        
        # 3. Trigger Calculation
        if st.button("Calculate", type="primary"):
            if not user_input.strip():
                st.warning("Please enter some numbers first!")
                return
                
            try:
                # Convert space-separated text to float arguments
                args = [float(x) for x in user_input.split()]
                
                # Run engine calculation
                result = st.session_state.engine.calculate(selected_op, *args)
                
                # Update State & Display Success
                st.success(f"**Result:** {result}")
                
                # Log to app session history
                args_str = ", ".join(map(str, args))
                st.session_state.history.append(f"{selected_op.split()[0]}({args_str}) = {result}")
                
            except ValueError as e:
                st.error(f"**Input Error:** {e}. Ensure you only entered numbers.")
            except ZeroDivisionError as e:
                st.error(f"**Math Error:** {e}")
            except Exception as e:
                st.error(f"**Error:** {e}")

if __name__ == "__main__":
    run_gui()
