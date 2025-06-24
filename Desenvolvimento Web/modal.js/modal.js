let BtnOpenModal = document.getElementById("BtnOpenModal");

let BtnCloseModal = document.getElementById("BtnCloseModal");

let Modal = document.getElementById("DialogModal");

BtnOpenModal.addEventListener("click", () => {
	Modal.classList.add("ModalOpen");
	// classList nesse caso adiciona a classe "ModalOpen" ao modal, tornando-o visível
});

BtnCloseModal.addEventListener("click", () => {
	Modal.classList.remove("ModalOpen");
	// classList nesse caso remove a classe "ModalOpen" do modal, tornando-o invisível
});
