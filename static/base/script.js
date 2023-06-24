document.addEventListener("DOMContentLoaded", () => {
    var manufacturer_select = document.querySelector("#manufacturer-select");
    manufacturer_select.addEventListener("change", event => {

        document.querySelector("#car-model-field").style.display = "block";
        model_select = document.querySelector("#model-select");

        fetch(`/api/models/${event.target.value}`, {
            method:"GET"
        })
        .then(response => response.json())
        .then(data => {
            model_select.innerHTML = "";

            const models = data.map(item => item.model);
            console.log(models)

            models.forEach(model => {
                new_option = document.createElement("option");
                new_option.value = model;
                new_option.innerHTML = model;
                model_select.append(new_option);
            });
            model_select.size = models.length;
        })
    })

    var add_to_favourites_button = document.querySelector("#add-to-favourites-button");
    add_to_favourites_button.addEventListener("click", () => {
        fetch(`/api/favourite/${add_to_favourites_button.dataset.id}`, {
            method:"PUT"
        })
        .then(response => {
            if(response.ok){
                console.log("uspq idiot takuv");
            }
            else{
                console.log("selqk");
            }
        })
    })
})