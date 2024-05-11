const form = document.getElementById('chat-form');
const chatHistory = document.getElementById('chat-history');


const chatBubble = (align, content) => {
    const chatSpan = document.createElement('span');
    chatSpan.classList.add('chat-bubble-span');

    console.log(align);
    if(align ==='right')
        chatSpan.style.flexDirection = 'row-reverse'

    const chatContainer = document.createElement('div');
    chatContainer.classList.add('chat-bubble-container');

    const topImage = document.createElement('img');
    topImage.src = '/static/assets/ChatTop.png';
    topImage.style.width = '100%';

    const bottomImage = document.createElement('img');
    bottomImage.src = '/static/assets/ChatBottom.png';
    bottomImage.style.width = '100%';
    bottomImage.style.height = '100%';
    if(align === 'left')
        bottomImage.style.transform = 'scaleX(-1)';

    const middleImageContainer = document.createElement('div');
    middleImageContainer.classList.add('middle-image-container')
    middleImageContainer.style.position = 'relative';
    middleImageContainer.style.width = '100%';

    const middleImage = document.createElement('img');
    middleImage.src = '/static/assets/ChatMiddle.png';

    const middleText = document.createElement('p')
    middleText.textContent = content;

    middleImageContainer.appendChild(middleImage);
    middleImageContainer.appendChild(middleText);

    chatContainer.appendChild(topImage);
    chatContainer.appendChild(middleImageContainer);
    chatContainer.appendChild(bottomImage);

    chatSpan.appendChild(chatContainer);

    return chatSpan;

}

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