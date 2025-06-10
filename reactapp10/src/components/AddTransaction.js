import { useState } from "react";

function AddTransaction({ addTransaction }) {
  const [text, setText] = useState("");
  const [amount, setAmount] = useState("");

  const onSubmit = (e) => {
    e.preventDefault();
    if (!text || !amount) return;

    const newTransaction = {
      id: Date.now(),
      text,
      amount: +amount,
    };

    addTransaction(newTransaction);
    setText("");
    setAmount("");
  };

  return (
    <>
      <h3>Add new transaction</h3>
      <form onSubmit={onSubmit}>
        <input className="balance" type="text" value={text} onChange={(e) => setText(e.target.value)} placeholder="Enter description" />
        <input className="balance"type="number" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Enter amount" />
        <br></br><br></br>
        <button className="balance">Add transaction</button>
      </form>
    </>
  );
}
export default AddTransaction;
