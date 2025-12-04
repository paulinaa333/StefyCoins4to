from mailAutomation import EmailSender

# ⚙️ Datos del remitente
usuario = "programacion4to26@gmail.com"
contraseña = "vgao udel ynsg neii"  # Contraseña de aplicación

# ✉️ Crear objeto y enviar
correo = EmailSender(usuario, contraseña)
correo.enviar_mail(
    destinatario="piramosbobatto@escuelasproa.edu.ar",
    asunto="Prueba desde Python en ProA La Falda",
    mensaje="Hola! Este es un mail de prueba enviado desde un programa en Python 🐍 dia 3/11"
)
