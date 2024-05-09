const form = document.getElementById('chat-form');
const chatHistory = document.getElementById('chat-history');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const messageInput = document.getElementById('message').value;

    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: messageInput })
    });

    const data = await response.json();
    const aiReply = data.reply;

    // Append AI reply to chat history
    const messageElement = document.createElement('div');
    messageElement.textContent = `User: ${messageInput}`;
    chatHistory.appendChild(messageElement);

    const replyElement = document.createElement('div');
    replyElement.textContent = `AI: ${aiReply}`;
    chatHistory.appendChild(replyElement);

    // Clear input field
    document.getElementById('message').value = '';
});