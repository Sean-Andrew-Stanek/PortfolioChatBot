const form = document.getElementById('chat-form');
const chatHistory = document.getElementById('chat-history');

// Single Chat Bubble
const chatBubble = (align, content) => {

    //Class names for chat bubble styles
    leftColorScheme = 'dark-blue';
    rightColorScheme = 'dark-green';

    //Master Container
    const chatContainer = document.createElement('div');
    chatContainer.classList.add('chat-bubble-container');

    //Text Container
    const textContainer = document.createElement('div');
    textContainer.className = 'text-container'
    textContainer.textContent = content;

    //Decorative Div
    const bubbleDirection = document.createElement('div');
    bubbleDirection.className = 'bubble-direction';

    //Proper alignment
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

    //Attach all children and send
    chatContainer.appendChild(textContainer);
    chatContainer.appendChild(bubbleDirection);
    return chatContainer;

}

// Listener for new user chat request
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

    //Adds two new bubbles - 
    //User request => left
    //AI response => right
    chatHistory.appendChild(chatBubble('left', `User: ${messageInput}`));
    chatHistory.appendChild(chatBubble('right', `AI:  ${aiReply}`))

    //Resets request field
    document.getElementById('message').value = '';
});