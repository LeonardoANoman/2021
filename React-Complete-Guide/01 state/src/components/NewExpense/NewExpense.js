import ExpenseForm from "./ExpenseForm";
import "./NewExpense.css";

function NewExpense(props) {
  const onSaveExpenseDataHandler = (enteredExepenseData) => {
    const expenseData = {
      ...enteredExepenseData,
      id: Math.random().toString(),
    };
    props.onAddexpense(expenseData);
  };
  return (
    <div className="new-expense">
      <ExpenseForm onSaveExpenseData={onSaveExpenseDataHandler} />
    </div>
  );
}

export default NewExpense;
