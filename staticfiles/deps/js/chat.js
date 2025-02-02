document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll(".delete-chat-button");
    const modal = document.getElementById("delete-confirm-modal");
    const confirmButton = document.getElementById("confirm-delete");
    const cancelButton = document.getElementById("cancel-delete");

    let chatToDelete = null;

    // Показ модального окна
    deleteButtons.forEach(button => {
        button.addEventListener("click", (e) => {
            chatToDelete = e.currentTarget.dataset.chatname;
            modal.classList.remove("hidden");
        });
    });

    // Подтверждение удаления
    confirmButton.addEventListener("click", () => {
        if (chatToDelete) {
            fetch(`/chat/delete-chat/${chatToDelete}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/';  // Перенаправляем на главную страницу после удаления
                } else {
                    alert("Ошибка при удалении чата.");
                }
            })
            .catch(error => console.error("Ошибка:", error));
        }
        modal.classList.add("hidden");
    });

    // Отмена удаления
    cancelButton.addEventListener("click", () => {
        chatToDelete = null;
        modal.classList.add("hidden");
    });
});
