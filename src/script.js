function submitForm() {
  var name = document.getElementById('name').value;
  var email = document.getElementById('email').value;

  var data = {
    name: name,
    email: email
  };

  // Convert data to JSON
  var jsonData = JSON.stringify(data);

  console.log('JSON Data:', jsonData);

  // Create a new issue using GitHub API
  fetch('https://api.github.com/repos/Onyx39/onyx39.github.io/issues', {
    method: 'POST',
    headers: {
      'Authorization': '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',
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
