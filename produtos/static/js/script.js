document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById("form-container");
    const addButton = document.getElementById("add-form");
    const removeButton = document.getElementsByClassName("remove-form");
    const totalForms = document.getElementById("id_form-TOTAL_FORMS");
    const emptyFormHtml = document.querySelector("#empty-form").innerHTML;
  
    addButton.addEventListener("click", function() {
      const formCount = parseInt(totalForms.value);  
      const newForm = emptyFormHtml.replace(/__prefix__/g, formCount);
      container.insertAdjacentHTML("beforeend", newForm);  
      totalForms.value = formCount + 1;
    });

    document.addEventListener("click", function(event) {
      if (event.target.classList.contains("remove-form")){
        const formProduto = event.target.closest(".form-produto");
        const deleteInput = formProduto.querySelector("input[type='checkbox'][name$='-DELETE']");
        if (deleteInput) {
          deleteInput.checked = true;
        }
        formProduto.style.display = "none"; 
 
      }
    });
  });