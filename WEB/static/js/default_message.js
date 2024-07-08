document.addEventListener('DOMContentLoaded', function() {
  // Check if there is a notification message in localStorage
  var notificationMessage = localStorage.getItem('notificationMessage');
  
  if (notificationMessage) {
    // Create notification element
    var notificationContainer = document.getElementById("notification-container");
    var notification = document.createElement("div");
    notification.className = "notification";
    notification.textContent = notificationMessage;

    // Append notification to container
    notificationContainer.appendChild(notification);

    // Activate notification (show it)
    setTimeout(function() {
      notification.classList.add("active");
    }, 100); // Delay to ensure smooth transition

    // Automatically hide notification after 4 seconds
    setTimeout(function() {
      notification.classList.remove("active");

      // Remove notification from DOM after transition ends
      setTimeout(function() {
        notification.remove();
      }, 300); // Wait for 0.3s transition duration
    }, 4000); // 4000 milliseconds = 4 seconds

    // Clear localStorage after displaying the notification
    localStorage.removeItem('notificationMessage');
  }
});
