function Balance({ transactions }) {
  const amounts = transactions.map(t => t.amount);
  const total = amounts.reduce((acc, val) => acc + val, 0).toFixed(2);

  return (
    <>
      <h4>Your Balance</h4>
      <h1 className="balance">₹{total}</h1>
    </>
  );
}
export default Balance;
