document.addEventListener('DOMContentLoaded', () => {
  fetch('/api/transactions/')
    .then(res => res.json())
    .then(data => {
      document.getElementById('transaction-summary').innerText = JSON.stringify(data, null, 2);
    });
});
