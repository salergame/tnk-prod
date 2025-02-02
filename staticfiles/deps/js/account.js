// Получаем модальные окна
var changePasswordModal = document.getElementById("change-password-modal");
var changeEmailModal = document.getElementById("change-email-modal");
var deleteAccountModal = document.getElementById("delete-account-modal");

// Получаем кнопки открытия модальных окон
var changePasswordLink = document.getElementById("change-password-link");
var changeEmailLink = document.getElementById("change-email-link");
var deleteAccountLink = document.getElementById("delete-account-link");

// Получаем кнопки закрытия модальных окон
var closeChangePassword = document.getElementById("close-change-password");
var closeChangeEmail = document.getElementById("close-change-email");
var closeDeleteAccount = document.getElementById("close-delete-account");

// Открытие модальных окон при клике на ссылки
changePasswordLink.onclick = function() {
    changePasswordModal.style.display = "block";
}
changeEmailLink.onclick = function() {
    changeEmailModal.style.display = "block";
}
deleteAccountLink.onclick = function() {
    deleteAccountModal.style.display = "block";
}

// Закрытие модальных окон при клике на кнопку закрытия
closeChangePassword.onclick = function() {
    changePasswordModal.style.display = "none";
}
closeChangeEmail.onclick = function() {
    changeEmailModal.style.display = "none";
}
closeDeleteAccount.onclick = function() {
    deleteAccountModal.style.display = "none";
}

// Закрытие модальных окон при клике вне модального окна
window.onclick = function(event) {
    if (event.target == changePasswordModal) {
        changePasswordModal.style.display = "none";
    }
    if (event.target == changeEmailModal) {
        changeEmailModal.style.display = "none";
    }
    if (event.target == deleteAccountModal) {
        deleteAccountModal.style.display = "none";
    }
}
