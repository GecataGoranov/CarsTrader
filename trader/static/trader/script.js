document.addEventListener("DOMContentLoaded", () => {
    var manufacturer_select = document.querySelector("#id_manufacturer");
    if(manufacturer_select){
        for(i=1; i < 53; i++) {
            fetch("https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/car?format=json")
            .then(response => response.json())
            .then(data => {
                data.Results.forEach(manufacturer => {
                    
                    for(i=0; i < manufacturer.VehicleTypes.length; i++){
                        if(manufacturer.VehicleTypes[i].Name == "Passenger Car" && manufacturer.Mfr_CommonName != null ){
                            const option = document.createElement("option");
                            option.textContent = manufacturer.Mfr_CommonName;
                            manufacturer_select.appendChild(option);
                        }
                    }
                });
            })
        }
    }
})
