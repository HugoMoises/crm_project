document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById("form-container");
    const addButton = document.getElementById("add-form");
    const totalForms = document.getElementById("id_form-TOTAL_FORMS");
    const emptyFormHtml = document.querySelector("#empty-form").innerHTML;
  
    addButton.addEventListener("click", function() {
      const formCount = parseInt(totalForms.value);  
      const newForm = emptyFormHtml.replace(/__prefix__/g, formCount);
      container.insertAdjacentHTML("beforeend", newForm);  
      totalForms.value = formCount + 1;
    });
  });