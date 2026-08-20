perfil_autor = {
    "nombre": "Jose Mercado",
    "bio": "Estudiante de desarrollo web y creador de contenido sobre programación.",
    "especialidad": "Desarrollo Web",
    "redes_sociales": ["Instagram", "GitHub"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Python", "HTML", "CSS", "JavaScript", "Python"}

posts = [
    {
        "id": 1,
        "titulo": "Mis primeros pasos con Python",
        "autor": perfil_autor,
        "categoria": "Programación",
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
        {
        "id": 2,
        "titulo": "Aprendiendo HTML y CSS",
        "autor": perfil_autor,
        "categoria": "Desarrollo Web",
        "tags": ["HTML", "CSS"],
        "estado": "borrador"
    },
        {
        "id": 3,
        "titulo": "Aprendiendo JavaScript",
        "autor": perfil_autor,
        "categoria": "Programacion",
        "tags": ["JavaScript","Principiantes"],
        "estado":"archivado"
    }
]

print("Autor del segundo post:", posts[1]["autor"]["nombre"])

print("Lista de posts guardados:")
print(posts)