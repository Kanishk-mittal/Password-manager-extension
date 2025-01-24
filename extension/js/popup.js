document.getElementById("fetch-message").addEventListener("click", () => {
    fetch("http://127.0.0.1:5000/hello")
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("api-message").textContent = data.message;
        })
        .catch((error) => {
            console.error("Error fetching the message:", error);
            document.getElementById("api-message").textContent = "Failed to fetch message!";
        });
});
