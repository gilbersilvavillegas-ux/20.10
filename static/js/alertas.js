const alertaswal = (title, text, icon, confirmButtonText, confirmButtonColor = "#007bff") =>{
    const swalConfig = {
        title:title,
        text:text,
        icon:icon,
        confirmButtonText:confirmButtonText
    };

// 🟢 Agrega la propiedad confirmButtonColor SI se proporciona el color
    if (confirmButtonColor) {
        swalConfig.confirmButtonColor = confirmButtonColor
    };
        
        // Nota: Si también usas iconHtml, agrégalo a swalConfig antes de este return.
        return Swal.fire(swalConfig);
    };