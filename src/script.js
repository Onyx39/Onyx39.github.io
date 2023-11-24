function submitForm() {
  var name = document.getElementById('name').value;
  var email = document.getElementById('email').value;

  var data = {
    name: name,
    email: email
  };

  // Convert data to JSON
  var jsonData = JSON.stringify(data);

  // Create a new issue using GitHub API
  fetch('https://api.github.com/repos/Onyx39/onyx39.github.io/issues', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer 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',
      'Content-Type': 'application/json'
    },
    body: jsonData
  })
  .then(response => response.json())
  .then(result => {
    alert('Form submitted successfully!');
    // You can redirect or do something else here
  })
  .catch(error => {
    console.error('Error:', error);
    alert('Form submission failed. Please try again.');
  });
}
