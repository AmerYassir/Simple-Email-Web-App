// Select the textarea where the draft content is entered
const recivier=document.getElementById('to')
const subject=document.getElementById('subject')
const messageBodyArea=document.getElementById('message')
const sendButton = document.getElementById('send-button')

let Sended=false;
// Listen for the beforeunload event to trigger autosave
window.addEventListener('beforeunload', function(event) {
    // save the current draft data into local storage
    if (Sended) {
        return;
    }
    localStorage.setItem('draftRecivier', recivier.value);
    localStorage.setItem('draftSubject', subject.value);
    localStorage.setItem('draftContent', messageBodyArea.value);

});

// Restore the draft content when the page is loaded
window.addEventListener('DOMContentLoaded', function() {
    // Get the draft content from localStorage
    const savedDraftContent = localStorage.getItem('draftContent');
    const savedDraftRecivie = localStorage.getItem('draftRecivier');
    const savedDraftSubject = localStorage.getItem('draftContent');
    // Restore the draft content in the textarea
    if (savedDraftContent || savedDraftRecivie || savedDraftSubject) {
        messageBodyArea.value = savedDraftContent;
        subject.value=savedDraftSubject;
        recivier.value=savedDraftRecivie;
    }
});
sendButton.addEventListener('click',function () {
    Sended=true;
    localStorage.clear();
})
