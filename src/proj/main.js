function generateRandomMessage() {
    const messages = [
      "Hello, world!",
      "Testing the SRI update functionality.",
      "This is a random message for CI/CD testing.",
      "Hello from the test script!",
      "Another random message to verify updates.",
      "SRI hash update test in progress.",
      "Let's see if this triggers an update.",
      "Random test message for GitHub Actions."
    ];
  
    const randomIndex = Math.floor(Math.random() * messages.length);
    return messages[randomIndex];
  }
  
  console.log(generateRandomMessage());
  