const form = document.getElementById('chat-form');
const chatHistory = document.getElementById('chat-history');


const chatBubble = (align, content) => {

    leftColorScheme = 'dark-blue';
    rightColorScheme = 'dark-green';

    const chatContainer = document.createElement('div');
    chatContainer.classList.add('chat-bubble-container');

    const textContainer = document.createElement('div');
    textContainer.className = 'text-container'
    textContainer.textContent = content;

    const bubbleDirection = document.createElement('div');
    bubbleDirection.className = 'bubble-direction';

    if(align === 'right') {
        textContainer.classList.add(rightColorScheme);
        bubbleDirection.classList.add(rightColorScheme);
        bubbleDirection.style.right = '0'; //text bubble margin
        chatContainer.style.justifyContent='flex-end'
        
    } else {
        textContainer.classList.add(leftColorScheme);
        bubbleDirection.classList.add(leftColorScheme);
        bubbleDirection.style.left = '0'; //text bubble margin
    }

    chatContainer.appendChild(textContainer);
    chatContainer.appendChild(bubbleDirection);


    return chatContainer;

}


chatHistory.appendChild(chatBubble('right', 'hello'));
chatHistory.appendChild(chatBubble('left', 'this is a test'));

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

    chatHistory.appendChild(chatBubble('left', `User: ${messageInput}`));
    chatHistory.appendChild(chatBubble('right', `AI:  ${aiReply}`))

/* 
    // Append AI reply to chat history
    const messageElement = document.createElement('div');
    messageElement.classList.add('message-element');
    messageElement.textContent = `User: ${messageInput}`;
    chatHistory.appendChild(messageElement);

    const replyElement = document.createElement('div');
    replyElement.classList.add('reply-element');
    replyElement.textContent = `AI:  ${aiReply}`;
    chatHistory.appendChild(replyElement); */

    // Clear input field
    document.getElementById('message').value = '';
});